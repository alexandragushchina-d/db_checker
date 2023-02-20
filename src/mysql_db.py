
import datetime
import mysql.connector
import sys

def connect_to_db(host, port, name, user, password) :
  try :
    connector = mysql.connector.connect(
      host = host,
      port = port,
      database = name,
      user = user,
      password = password)
  except :
    print("DB's connection failed - {}".format(sys.exc_info()[1]))
    return None

  return connector

class ScriptRunResult :
  def __init__(self) :
    self.error_count = 0
    self.time = datetime.timedelta()
    self.min_time = datetime.timedelta()
    self.avg_time = datetime.timedelta()
    self.max_time = datetime.timedelta()

  def __str__(self) :
    return "time: {}; min time: {}; avg time: {}; max time: {}; " \
           "error count: {:d}".format(
               self.time.total_seconds(), self.min_time.total_seconds(),
               self.avg_time.total_seconds(), self.max_time.total_seconds(),
               self.error_count)

def run_script(get_connector, script, count) -> ScriptRunResult :
  result = ScriptRunResult()
  for i in range(count) :
    begin_time = datetime.datetime.now() # also count errors

    try :
      connector = get_connector()
    except :
      print("DB's exception occurred - {}".format(sys.exc_info()[1]))
      result.error_count += 1
      continue

    connector.can_consume_results = True
    try :
      cursor = connector.cursor()
      cursor.execute(script) # read records from the db to execute statements
      cursor.close()
    except :
      print("DB's exception occurred - {}".format(sys.exc_info()[1]))
      result.error_count += 1

    try :
      connector.close()
    except :
      print("DB's exception occurred - {}".format(sys.exc_info()[1]))

    time_delta = datetime.datetime.now() - begin_time
    result.time += time_delta
    result.max_time = max(result.max_time, time_delta)
    if i > 0 :
      result.min_time = min(result.min_time, time_delta)
    else :
      result.min_time = time_delta

  result.avg_time = result.time / count
  return result

def run_scripts(connector, scripts, count) -> dict :
  result = dict()
  for file_path, script in scripts.items() :
    result[file_path] = run_script(connector, script, count)

  return result
