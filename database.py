# In this file you must implement your main query methods
# so they can be used by your database models to interact with your bot.

import os
from pymysql import DatabaseError
import pymysql.cursors

#TODO: add the values for these database keys in your secrets on replit
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


class Database:

  # This method was already implemented for you
  def connect(self, close_connection=False):
    try:
      conn = pymysql.connect(host=db_host,
                             port=3306,
                             user=db_username,
                             password=db_password,
                             db=db_name,
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)
      print("Bot connected to database {}".format(db_name))
      if close_connection:
        return True
      return conn
    except ConnectionError as err:
      print(f"An error has occurred: {err.args[1]}")
      print("\n")

  #TODO: needs to implement the internal logic of all the main query operations
  def get_response(self, query, values=None, fetch=False, many_entities=False):
    response = None
    connection = self.connect()
    # your code here
    cursor = connection.cursor()
    if values:
      if many_entities:
        cursor.executemany(query, values)
      else:
        cursor.execute(query, values)
    else:
      cursor.execute(query)
    connection.commit()
    connection.close()
    if fetch:
      response = cursor.fetchall()
    # your code here
    return response

  # the following methods were already implemented for you.
  @staticmethod
  def select(query, values=None, fetch=True):
    database = Database()
    return database.get_response(query, values=values, fetch=fetch)

  @staticmethod
  def insert(query, values=None, many_entities=False):
    database = Database()
    return database.get_response(query, values=values, many_entities=many_entities)

  @staticmethod
  def update(query, values=None):
    database = Database()
    return database.get_response(query, values=values)

  @staticmethod
  def delete(query, values=None):
    database = Database()
    return database.get_response(query, values=values)


class Query:
  
  GET_ACTIVESORTIES = """SELECT rpa.model_name AS drone_model, CONCAT(act.first_name, ' ', act.last_name) AS pilot_name, mis.task AS mission_task, srt.launch_time FROM sortie srt JOIN mission mis ON srt.mission = mis.mission_id JOIN remotely_piloted_aircraft rpa ON srt.rpa = rpa.rpa_id LEFT JOIN pilot plt ON mis.rpa = plt.pilot_id LEFT JOIN accounts act ON plt.pilot_id = act.account_id WHERE srt.recovery_time IS NULL;"""

  GET_ALLSORTIES = """SELECT rpa.model_name AS drone_model, CONCAT(act.first_name, ' ', act.last_name) AS pilot_name, mis.task AS mission_task, srt.launch_time, srt.recovery_time FROM sortie srt JOIN mission mis ON srt.mission = mis.mission_id JOIN remotely_piloted_aircraft rpa ON srt.rpa = rpa.rpa_id LEFT JOIN pilot plt ON mis.rpa = plt.pilot_id LEFT JOIN accounts act ON plt.pilot_id = act.account_id;"""

  GET_ACTIVEAPPOINTMENTS = """SELECT rpa.model_name AS drone_model, CONCAT(act.first_name, ' ', act.last_name) AS maintainer_name, log.start_time FROM maintenance_log log JOIN remotely_piloted_aircraft rpa ON log.rpa = rpa.rpa_id JOIN maintenance_appointment apt ON log.appointment = apt.appointment_id LEFT JOIN maintainer mnt ON apt.maintainer = mnt.maintainer_id LEFT JOIN accounts act ON mnt.maintainer_id = act.account_id WHERE log.end_time IS NULL;"""

  GET_ALLAPPOINTMENTS = """SELECT rpa.model_name AS drone_model, CONCAT(act.first_name, ' ', act.last_name) AS maintainer_name, log.start_time, log.end_time FROM maintenance_log log JOIN remotely_piloted_aircraft rpa ON log.rpa = rpa.rpa_id JOIN maintenance_appointment apt ON log.appointment = apt.appointment_id LEFT JOIN maintainer mnt ON apt.maintainer = mnt.maintainer_id LEFT JOIN accounts act ON mnt.maintainer_id = act.account_id;"""

  GET_PILOTS = """SELECT act.username, CONCAT(act.first_name, ' ', act.last_name) AS full_name, org.name AS organization, plt.status AS status, plt.last_training AS last_training FROM pilot plt JOIN accounts act ON plt.pilot_id = act.account_id JOIN organization org ON plt.organization = org.organization_id;"""
 
  GET_SENSORS = """SELECT act.username, CONCAT(act.first_name, ' ', act.last_name) AS full_name, org.name AS organization, sen.status AS status, sen.last_training AS last_training FROM sensor_operator sen JOIN accounts act ON sen.sensor_id = act.account_id JOIN organization org ON sen.organization = org.organization_id;"""

  GET_MAINTAINERS = """SELECT act.username, CONCAT(act.first_name, ' ', act.last_name) AS full_name, org.name AS organization, bas.location AS base, mnt.status AS status, mnt.last_training AS last_training FROM maintainer mnt JOIN accounts act ON mnt.maintainer_id = act.account_id JOIN organization org ON mnt.organization = org.organization_id JOIN base bas ON mnt.base = bas.base_id;"""

  GET_PLANNERS = """SELECT act.username, CONCAT(act.first_name, ' ', act.last_name) AS full_name, org.name AS organization, pln.status AS status FROM planner pln JOIN accounts act ON pln.planner_id = act.account_id JOIN organization org ON pln.organization = org.organization_id;"""

  GET_BASES = """SELECT * FROM base;"""
  
  GET_ORGANIZATIONS = """SELECT org.name AS name, bas.location AS base FROM organization org JOIN base bas ON org.base = bas.base_id;"""

  GET_FLIGHTPLANS = """SELECT CONCAT(act.first_name, ' ', act.last_name) AS planner_name, flt.waypoints, lbas.location AS launch_base, rbas.location AS recovery_base, pay.weightlbs AS weight, pay.pylon_count AS pylons FROM flight_plan flt JOIN payload pay ON flt.payload = pay.payload_id JOIN base lbas ON flt.launch_base = lbas.base_id JOIN base rbas ON flt.recovery_base = rbas.base_id LEFT JOIN planner pln ON flt.planner = pln.planner_id LEFT JOIN accounts act ON pln.planner_id = act.account_id;"""

  GET_USERS = """SELECT username, CONCAT(first_name, ' ', last_name) AS full_name FROM accounts;"""

  GET_DEVICESALL = """SELECT COUNT(dev.device_id) AS device_count FROM devices dev JOIN accounts act ON dev.account = act.account_id WHERE act.username = %s;"""

  GET_DEVICESACTIVE = """SELECT COUNT(dev.device_id) AS device_count FROM devices dev JOIN accounts act ON dev.account = act.account_id WHERE act.username = %s AND still_authorized = 1;"""

  GET_FLEET = """SELECT rpa.model_name, rpa.manufacturer, CONCAT(plt.first_name, ' ', plt.last_name) AS pilot_name, CONCAT(sen.first_name, ' ', sen.last_name) AS sensor_name, CONCAT(mnt.first_name, ' ', mnt.last_name) AS maintainer_name FROM remotely_piloted_aircraft rpa LEFT JOIN accounts plt ON rpa.pilot = plt.account_id LEFT JOIN accounts sen ON rpa.sensor_operator = sen.account_id LEFT JOIN accounts mnt ON rpa.maintainer = mnt.account_id;"""
