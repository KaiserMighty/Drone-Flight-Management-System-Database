from database import *


class ModelInterface:

  def __init__(self) -> None:
    self.was_deleted = False

  def syncronize():
    pass

  def signin(organization):
    pass

  def update(self, attribute, value):
    pass

  def delete(self):
    pass

  @staticmethod
  def add(data):
    pass

  @staticmethod
  def get(value):
    pass


class BaseModel(ModelInterface):

  def __init__(self, base_id=None):
    super().__init__()
    self.base_id = base_id
    self.location = None
    self.rpa_count = None
    self.maintainer_count = None
  
  @staticmethod
  def get_bases():
    try:
      bases = []
      base_data = Database.select(Query.GET_BASES)
  
      if base_data:
        for values in base_data:
          base = BaseModel()
          base.location = values['location']
          base.rpa_count = values['rpa_count']
          base.maintainer_count = values['maintainer_count']
          bases.append(base)
        return bases
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving maintainers: {db_err}")
      return None

class OrganizationModel(ModelInterface):

  def __init__(self, organization_id=None):
    super().__init__()
    self.organization_id = organization_id
    self.name = None
    self.base = None

  @staticmethod
  def get_organizations():
    try:
      organizations = []
      organization_data = Database.select(Query.GET_ORGANIZATIONS)

      if organization_data:
        for values in organization_data:
          organization = OrganizationModel()
          organization.name = values['name']
          organization.base = values['base']
          organizations.append(organization)
        return organizations
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving maintainers: {db_err}")
      return None

class SortieModel(ModelInterface):

  def __init__(self, sortie_id=None):
    super().__init__()
    self.sortie_id = sortie_id
    self.drone_model = None
    self.pilot_name = None
    self.sensor_operator_name = None
    self.mission_task = None
    self.launch_time = None
    self.recovery_time = None

  @staticmethod
  def get_active():
    try:
      sorties = []
      sortie_data = Database.select(Query.GET_ACTIVESORTIES)

      if sortie_data:
        for values in sortie_data:
          sortie = SortieModel()
          sortie.drone_model = values['drone_model']
          sortie.pilot_name = values['pilot_name']
          sortie.mission_task = values['mission_task']
          sortie.launch_time = values['launch_time']
          sorties.append(sortie)
        return sorties
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving active sorties: {db_err}")
      return None

  @staticmethod
  def get_all():
    try:
      sorties = []
      sortie_data = Database.select(Query.GET_ALLSORTIES)

      if sortie_data:
        for values in sortie_data:
          sortie = SortieModel()
          sortie.drone_model = values['drone_model']
          sortie.pilot_name = values['pilot_name']
          sortie.mission_task = values['mission_task']
          sortie.launch_time = values['launch_time']
          sortie.recovery_time = values['recovery_time']
          sorties.append(sortie)
        return sorties
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving all sorties: {db_err}")
      return None

class AppointmentModel(ModelInterface):

  def __init__(self, appointment_id=None):
    super().__init__()
    self.appointment_id = appointment_id
    self.drone_model = None
    self.maintainer_name = None
    self.start_time = None
    self.end_time = None
  
  @staticmethod
  def get_active():
    try:
      appointments = []
      appointment_data = Database.select(Query.GET_ACTIVEAPPOINTMENTS)
  
      if appointment_data:
        for values in appointment_data:
          appointment = AppointmentModel()
          appointment.drone_model = values['drone_model']
          appointment.maintainer_name = values['maintainer_name']
          appointment.start_time = values['start_time']
          appointments.append(appointment)
        return appointments
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving active sorties: {db_err}")
      return None
  
  @staticmethod
  def get_all():
    try:
      appointments = []
      appointment_data = Database.select(Query.GET_ALLAPPOINTMENTS)

      if appointment_data:
        for values in appointment_data:
          appointment = AppointmentModel()
          appointment.drone_model = values['drone_model']
          appointment.maintainer_name = values['maintainer_name']
          appointment.start_time = values['start_time']
          appointment.end_time = values['end_time']
          appointments.append(appointment)
        return appointments
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving all sorties: {db_err}")
      return None

class PilotModel(ModelInterface):

  def __init__(self, pilot_id=None):
    super().__init__()
    self.pilot_id = pilot_id
    self.username = None
    self.full_name = None
    self.organization = None
    self.status = None
    self.last_training = None

  @staticmethod
  def get_pilots():
    try:
      pilots = []
      pilot_data = Database.select(Query.GET_PILOTS)
  
      if pilot_data:
        for values in pilot_data:
          pilot = PilotModel()
          pilot.username = values['username']
          pilot.full_name = values['full_name']
          pilot.organization = values['organization']
          pilot.status = values['status']
          pilot.last_training = values['last_training']
          pilots.append(pilot)
        return pilots
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving pilots: {db_err}")
      return None

class SensorModel(ModelInterface):

  def __init__(self, sensor_id=None):
    super().__init__()
    self.sensor_id = sensor_id
    self.username = None
    self.full_name = None
    self.organization = None
    self.status = None
    self.last_training = None
  
  @staticmethod
  def get_sensors():
    try:
      sensors = []
      sensor_data = Database.select(Query.GET_SENSORS)
  
      if sensor_data:
        for values in sensor_data:
          sensor = PilotModel()
          sensor.username = values['username']
          sensor.full_name = values['full_name']
          sensor.organization = values['organization']
          sensor.status = values['status']
          sensor.last_training = values['last_training']
          sensors.append(sensor)
        return sensors
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving pilots: {db_err}")
      return None

class MaintainerModel(ModelInterface):

  def __init__(self, maintainer_id=None):
    super().__init__()
    self.maintainer_id = maintainer_id
    self.username = None
    self.full_name = None
    self.organization = None
    self.base = None
    self.status = None
    self.last_training = None
  
  @staticmethod
  def get_maintainers():
    try:
      maintainers = []
      maintainer_data = Database.select(Query.GET_MAINTAINERS)
  
      if maintainer_data:
        for values in maintainer_data:
          maintainer = MaintainerModel()
          maintainer.username = values['username']
          maintainer.full_name = values['full_name']
          maintainer.organization = values['organization']
          maintainer.base = values['base']
          maintainer.status = values['status']
          maintainer.last_training = values['last_training']
          maintainers.append(maintainer)
        return maintainers
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving maintainers: {db_err}")
      return None

class PlannerModel(ModelInterface):

  def __init__(self, planner_id=None):
    super().__init__()
    self.planner_id = planner_id
    self.username = None
    self.full_name = None
    self.organization = None
    self.base = None
    self.status = None
  
  @staticmethod
  def get_planners():
    try:
      planners = []
      planner_data = Database.select(Query.GET_PLANNERS)
  
      if planner_data:
        for values in planner_data:
          planner = PlannerModel()
          planner.username = values['username']
          planner.full_name = values['full_name']
          planner.organization = values['organization']
          planner.base = values['base']
          planner.status = values['status']
          planners.append(planner)
        return planners
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving maintainers: {db_err}")
      return None

class PlanModel(ModelInterface):
  
  def __init__(self, plan_id=None):
    super().__init__()
    self.plan_id = plan_id
    self.planner_name = None
    self.waypoints = None
    self.launch_base = None
    self.recovery_base = None
    self.weight = None
    self.pylons = None
  
  @staticmethod
  def get_plans():
    try:
      plans = []
      plan_data = Database.select(Query.GET_FLIGHTPLANS)
  
      if plan_data:
        for values in plan_data:
          plan = PlanModel()
          plan.planner_name = values['planner_name']
          plan.waypoints = values['waypoints']
          plan.launch_base = values['launch_base']
          plan.recovery_base = values['recovery_base']
          plan.weight = values['weight']
          plan.pylons = values['pylons']
          plans.append(plan)
        return plans
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving maintainers: {db_err}")
      return None

class AccountModel(ModelInterface):

  def __init__(self, account_id=None):
    super().__init__()
    self.account_id = account_id
    self.username = None
    self.full_name = None
    self.password = None

  @staticmethod
  def get_accounts():
    try:
      accounts = []
      account_data = Database.select(Query.GET_USERS)

      if account_data:
        for values in account_data:
          account = AccountModel()
          account.username = values['username']
          account.full_name = values['full_name']
          accounts.append(account)
        return accounts
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving accounts: {db_err}")
      return None


class DeviceModel:

  def __init__(self, username):
    super().__init__()
    self.username = username
    self.device_count = None

  @staticmethod
  def get_all(username):
    try:
      devices = []
      device_data = Database.select(Query.GET_DEVICESALL, (username))
  
      if device_data:
        for values in device_data:
          device = DeviceModel(username)
          device.device_count = values['device_count']
          devices.append(device)
        return devices
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving accounts: {db_err}")
      return None

  @staticmethod
  def get_active(username):
    try:
      devices = []
      device_data = Database.select(Query.GET_DEVICESACTIVE, (username))

      if device_data:
        for values in device_data:
          device = DeviceModel(username)
          device.device_count = values['device_count']
          devices.append(device)
        return devices
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving accounts: {db_err}")
      return None

class DroneModel(ModelInterface):

  def __init__(self, rpa_id=None):
    super().__init__()
    self.rpa_id = rpa_id
    self.model_name = None
    self.manufacturer = None
    self.pilot_name = None
    self.sensor_name = None
    self.maintainer_name = None
    self.status = None
    self.base = None

  @staticmethod
  def get_drones():
    try:
      RPAs = []
      RPA_data = Database.select(Query.GET_FLEET)

      if RPA_data:
        for values in RPA_data:
          RPA = DroneModel()
          RPA.model_name = values['model_name']
          RPA.manufacturer = values['manufacturer']
          RPA.pilot_name = values['pilot_name']
          RPA.sensor_name = values['sensor_name']
          RPA.maintainer_name = values['maintainer_name']
          RPAs.append(RPA)
        return RPAs
      return None
    except DatabaseError as db_err:
      print(f"Error retrieving drones: {db_err}")
      return None
