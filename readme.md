# Customizable Performance Database Monitor

## Contents
* [General](#general-info)
* [Technologies](#technologies)
* [Installation](#installation)
  * [Ubuntu](#installation-ubuntu)
  * [Windows](#installation-windows)
* [Start the Program](#start-program)
* [FAQs](#faqs)
* [Improvements](#improvements)

## General <a name="general-info"></a>

The monitor helps you measure the performance of any DB on regular base.
To use the tool you need to create a new file **_config.json_** with description
and credentials to DB such as DB's type, DB's name, host, port, user, password,
test script folder and output file. As example, you are able to use the created
files for PostgreSQL, MySQL.

***
## Technologies <a name="technologies"></a>

A list of technologies used for the project:
* [Python 3](https://www.python.org/)
* JSON
* PostgreSQL
* MySQL

***
## Installation <a name="installation"></a>
### Ubuntu <a name="installation-ubuntu"></a>

- Keep your environment up to date

```json
$ sudo apt-get update
$ sudo apt-get upgrade
```
- Install python3, pip

```json
$ sudo apt install python3
$ python3 -m pip install --upgrade pip
```

- Install a psycopg2 library

```json
$ python3 -m pip install psycopg2-binary
```
- Install a mysql library

```json
$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

```

### Windows <a name="installation-windows"></a>
- Install [Python 3](https://www.python.org/download/releases/3.0/)
- Install a psycopg2 library

```json
$ pip install psycopg2
```
- Install a mysql library

```json
$ pip install mysqlclient
```

## Start the program <a name="start-program"></a>

```json
$ python3 main.py ./mysql_scripts/config.json
```
or
```json
$ python3 main.py ./pg_scripts/config.json --db-psswrd=<password>
```
or
```json
$ python3 main.py ./pg_scripts/config.json --db-user=<user> --db-psswrd=<password>
```

***
## FAQs <a name="faqs"></a>
**A list of frequently asked questions:**

- <u>Can the performance monitor be extended for other databases?</u><br/>
Yes, you need to write a new config-file and add folder of measuring queries.

- <u>Can any parameter from json-file be rewritten by command line?</u><br/>
Yes, you need to use a parameter's name from json-file. For example:
```json
$ python3 main.py ./pg_scripts/config.json --result-file=my_result.json
```

- <u>What can affect the execution time of requests?</u><br/>
  - Where the database is located - locally or on a server.
  - How high DB is loaded

***
## Improvements <a name="improvements"></a>

- Save results in different files for comparing ones. For example it's useful
to find how performance changes during week.
- Add support of new DB types.
- Add a notification system about exceeding extreme values that can be set
in the config-file.
