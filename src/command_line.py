
import json
import sys

from typing import Any
from typing import NoReturn

class CommandLine :
  def __init__(self) -> NoReturn :
    self._switches = dict()
    self.init_from_argv(sys.argv)

  def init_from_argv(self, argv) -> NoReturn :
    if len(argv) < 2 :
      return

    try :
      file_content = None
      with open(argv[1], 'r') as config_file :
        file_content = config_file.read()

      json_value = json.loads(file_content)
    except :
      return

    if not isinstance(json_value, dict) :
      return

    for key, value in json_value.items() :
      # Don't rewrite real switches
      if self.has_switch(key) :
        continue

      # Add new switch
      self._switches[key] = value

    self.update_cmd_line_switches(argv)

  def update_cmd_line_switches(self, argv) -> NoReturn :
    for arg in argv :
      if not isinstance(arg, str) or len(arg) == 0 :
        continue

      # Check it is a command line switch (e.g. --file=some.txt)
      if len(arg) <= 2 or (arg[0] != '-' and arg[1] != '-') :
        continue

    name_end = 2
    while name_end < len(arg) and arg[name_end] != '=' :
      name_end += 1

    self._switches[arg[2 : name_end]] = arg[name_end + 1 : len(arg)]

  def has_switch(self, name) -> bool :
    return name in self._switches.keys()

  def get_switch(self, name, default = None) -> Any :
    return self._switches.get(name, default)

  def get_switch_as_int(self, name, default = None) -> int :
    result = None
    try:
      result = int(self._switches.get(name, default))
    except :
      result = None

    return result
