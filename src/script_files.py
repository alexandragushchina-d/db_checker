
import os

# Script file extension
FILE_EXTENSION = "sql"

def get_file_list(dir_path) -> list :
  files = list()
  for dir_path, dir_names, file_names in os.walk(dir_path) :
    for name in file_names :
      if not name.endswith(FILE_EXTENSION) :
        continue

      file_path = os.path.abspath(os.path.join(dir_path, name))
      files.append(file_path)

  return files

def get_scripts(dir_path) -> dict :
  file_list = get_file_list(dir_path)

  result = dict()
  for file_path in file_list :
    try :
      file_content = None
      with open(file_path, 'r') as script_file :
        file_content = script_file.read()
    except :
      continue

    result[file_path] = file_content

  return result
