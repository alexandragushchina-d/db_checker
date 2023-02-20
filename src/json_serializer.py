
def _escape_json_string(raw_str) :
  result = ""
  index = 0
  begin_index = 0
  for char in raw_str :
    escaped = None
    if char == '\b' :
      escaped = "\\b"
    elif char == '\f' :
      escaped = "\\f"
    elif char == '\n' :
      escaped = "\\n"
    elif char == '\r' :
      escaped = "\\r"
    elif char == '\t' :
      escaped = "\\t"
    elif char == '\\' :
      escaped = "\\\\"
    elif char == '\"' :
      escaped = "\\\""

    if escaped is not None :
      result += raw_str[begin_index : index]
      result += escaped
      begin_index = index + 1

    index += 1

  result += raw_str[begin_index :]
  return result

def times_to_json(times) -> str :
  result = "[\n"
  add_comma = False
  for key, value in times.items() :
    if add_comma :
      result += ",\n"

    result += "  {\n"
    result += "    \"file_name\": \"{}\",\n".format(_escape_json_string(key))
    result += "    \"time\": \"{:.6f}\",\n".format(value.time.total_seconds())
    result += \
        "    \"min_time\": \"{:.6f}\",\n".format(value.min_time.total_seconds())
    result += \
        "    \"avg_time\": \"{:.6f}\",\n".format(value.avg_time.total_seconds())
    result += \
        "    \"max_time\": \"{:.6f}\",\n".format(value.max_time.total_seconds())
    result += "    \"error_count\": \"{}\"\n".format(value.error_count)
    result += "  }"
    add_comma = True
  result += "\n]"
  return result
