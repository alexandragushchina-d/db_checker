
import datetime
import sys
import json
import mysql_db
import pg_db

from command_line import *
from json_serializer import *
from script_files import *

#
# Constants
#
ARG_DB_TYPE = "db-type"
ARG_DB_HOST = "db-host"
ARG_DB_PORT = "db-port"
ARG_DB_DATABASE = "db-name"
ARG_DB_PASSWORD = "db-psswrd"
ARG_DB_USER = "db-user"
ARG_SCRIPT_DIR = "script-dir"
ARG_RESULT_FILE = "result-file"
ARG_ITERATION_COUNT = "iteration-count"

DB_FUNCTIONS = {
  "pg": [pg_db.connect_to_db, pg_db.run_scripts],
  "mysql": [mysql_db.connect_to_db, mysql_db.run_scripts]
}

def main() :
  # Print log header
  date = datetime.datetime.now()
  print("{:*^80}".format(""))
  print("*" + "{: ^78}".format("") + "*")
  title = "{} {:%Y-%m-%d %H:%M:%S}".format("DB checker", date)
  print("*" + "{: ^78}".format(title) + "*")
  print("*" + "{: ^78}".format("") + "*")
  print("{:*^80}".format(""))

  # Parameters
  cmd_line = CommandLine()
  db_type = cmd_line.get_switch(ARG_DB_TYPE, "")
  db_host = cmd_line.get_switch(ARG_DB_HOST, "")
  db_port = cmd_line.get_switch_as_int(ARG_DB_PORT, -1)
  db_name = cmd_line.get_switch(ARG_DB_DATABASE, "")
  db_user = cmd_line.get_switch(ARG_DB_USER, "")
  db_password = cmd_line.get_switch(ARG_DB_PASSWORD, "")
  script_dir = cmd_line.get_switch(ARG_SCRIPT_DIR, "")
  result_file = cmd_line.get_switch(ARG_RESULT_FILE, "")
  iteration_count = cmd_line.get_switch_as_int(ARG_ITERATION_COUNT, 1)

  if len(script_dir) != 0 :
    script_dir = os.path.abspath(script_dir)

  if len(result_file) != 0 :
    result_file = os.path.abspath(result_file)

  # Print parameters
  str_template = "  {: <16} - {}"
  print(str_template.format(ARG_DB_TYPE, db_type))
  print(str_template.format(ARG_DB_HOST, db_host))
  print(str_template.format(ARG_DB_PORT, db_port))
  print(str_template.format(ARG_DB_DATABASE, db_name))
  print(str_template.format(ARG_DB_USER, db_user))
  # Print stairs instead of password
  print(str_template.format(
      ARG_DB_PASSWORD,
      ("{" + ":*^{:d}".format(len(db_password)) + "}").format("")))
  print(str_template.format(ARG_SCRIPT_DIR, script_dir))
  print(str_template.format(ARG_RESULT_FILE, result_file))
  print(str_template.format(ARG_ITERATION_COUNT, iteration_count))

  # Check parameters
  if not db_type in DB_FUNCTIONS :
    print("DB type isn't valide.")
    return 1

  if len(db_host) == 0 :
    print("DB host can't be empty.")
    return 1

  if db_port <= 0 :
    print("DB port is invalide.")
    return 1

  if len(db_name) == 0 :
    print("DB name can't be empty.")
    return 1

  if len(db_password) == 0 :
    print("DB password can't be empty.")
    return 1

  if len(db_user) == 0 :
    print("DB user can't be empty.")
    return 1

  if len(script_dir) == 0 :
    print("DB scripts can't be empty.")
    return 1

  if len(result_file) == 0 :
    print("Result file path can't be empty.")
    return 1

  if iteration_count < 0 :
    print("DB count is invalide.")
    return 1

  # Get scripts
  scripts = get_scripts(script_dir)

  # Create getter for connection to DB
  get_connector = lambda : DB_FUNCTIONS[db_type][0](
      db_host, db_port, db_name, db_user, db_password)

  # Run scripts
  result = DB_FUNCTIONS[db_type][1](get_connector, scripts, iteration_count)

  # Print result
  # C:\folder\file.sql - time: ...
  for file_path, value in result.items() :
    print("{} - {}".format(file_path, value))

  # Print result to json-file - ?
  json_data = times_to_json(result)

  with open(result_file, "w") as out_file:
    out_file.write(json_data)

  return 0

if __name__ == '__main__':
  sys.exit(main())
