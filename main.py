"""
The code below is just representative of the implementation of a Bot. 
However, this code was not meant to be compiled as it. It is the responsability 
of all the students to modifify this code such that it can fit the 
requirements for this assignments.
"""

import discord
import os
from discord.ext import commands
from models import *

#TODO:  add your Discord Token as a value to your secrets on replit using the DISCORD_TOKEN key
TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command(name="active_sorties", description="show only active sorties")
async def _activesorties(ctx, *args):
  active_sorties = SortieModel.get_active()
  response = f""
  if active_sorties:
    for sortie in active_sorties:
      response += f"Drone Model: {sortie.drone_model}\n"
      response += f"Pilot: {sortie.pilot_name}\n"
      response += f"Mission Task: {sortie.mission_task}\n"
      response += f"Launch Time: {sortie.launch_time}\n\n"
      message = discord.Embed(title="Displaying Active Sorties", description=response, color=0x00ff00)
      await ctx.send(embed=message)
  else:
    await ctx.send("No active sorties found.")

@bot.command(name="all_sorties", description="show all sorties")
async def _allsorties(ctx, *args):
  all_sorties = SortieModel.get_all()
  response = f""
  if all_sorties:
    for sortie in all_sorties:
      response += f"Drone Model: {sortie.drone_model}\n"
      response += f"Pilot: {sortie.pilot_name}\n"
      response += f"Mission Task: {sortie.mission_task}\n"
      response += f"Launch Time: {sortie.launch_time}\n"
      response += f"Recovery Time: {sortie.recovery_time}\n\n"
    message = discord.Embed(title="Displaying All Sorties", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No sorties found.")

@bot.command(name="pilots", description="show all pilots")
async def _getpilots(ctx, *args):
  pilots = PilotModel.get_pilots()
  response = f""
  if pilots:
    for pilot in pilots:
      response += f"Username: {pilot.username}\n"
      response += f"Full Name: {pilot.full_name}\n"
      response += f"Organization: {pilot.organization}\n"
      response += f"Status: {pilot.status}\n"
      response += f"Last Training: {pilot.last_training}\n\n"
    message = discord.Embed(title="Displaying Pilots", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No pilots found.")

@bot.command(name="sensors", description="show all sensor operators")
async def _getsensors(ctx, *args):
  sensors = SensorModel.get_sensors()
  response = f""
  if sensors:
    for sensor_operator in sensors:
      response += f"Username: {sensor_operator.username}\n"
      response += f"Full Name: {sensor_operator.full_name}\n"
      response += f"Organization: {sensor_operator.organization}\n"
      response += f"Status: {sensor_operator.status}\n"
      response += f"Last Training: {sensor_operator.last_training}\n\n"
    message = discord.Embed(title="Displaying Sensor Operator", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No sensor operators found.")

@bot.command(name="maintainers", description="show all maintainers")
async def _getmaintainers(ctx, *args):
  maintainers = MaintainerModel.get_maintainers()
  response = f""
  if maintainers:
    for maintainer in maintainers:
      response += f"Username: {maintainer.username}\n"
      response += f"Full Name: {maintainer.full_name}\n"
      response += f"Organization: {maintainer.organization}\n"
      response += f"Base: {maintainer.base}\n"
      response += f"Status: {maintainer.status}\n"
      response += f"Last Training: {maintainer.last_training}\n\n"
    message = discord.Embed(title="Displaying Maintainers", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No maintainers found.")

@bot.command(name="planners", description="show all planners")
async def _getplanners(ctx, *args):
  planners = PlannerModel.get_planners()
  response = f""
  if planners:
    for planner in planners:
      response += f"Username: {planner.username}\n"
      response += f"Full Name: {planner.full_name}\n"
      response += f"Organization: {planner.organization}\n"
      response += f"Status: {planner.status}\n\n"
    message = discord.Embed(title="Displaying Planners", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No planners found.")

@bot.command(name="bases", description="show all bases")
async def _getbases(ctx, *args):
  bases = BaseModel.get_bases()
  response = f""
  if bases:
    for base in bases:
      response += f"The {base.location} base has {base.rpa_count} RPA(s) and {base.maintainer_count} maintainer(s)\n"
    message = discord.Embed(title="Displaying Bases", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No bases found.")

@bot.command(name="organizations", description="show all organizations")
async def _getorganizations(ctx, *args):
  organizations = OrganizationModel.get_organizations()
  response = f""
  if organizations:
    for organization in organizations:
      response += f"{organization.name} based out of {organization.base}\n"
    message = discord.Embed(title="Displaying Organization", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No organizations found.")

@bot.command(name="active_appointments", description="show only in-progress maintainance appointments")
async def _activeappointments(ctx, *args):
  active_appointments = AppointmentModel.get_active()
  response = f""
  if active_appointments:
    for appointment in active_appointments:
      response += f"Drone Model: {appointment.drone_model}\n"
      response += f"Maintainer: {appointment.maintainer_name}\n"
      response += f"Start Time: {appointment.start_time}\n\n"
    message = discord.Embed(title="Displaying In-Progress Appointments", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No active maintenance appointments found.")

@bot.command(name="all_appointments", description="show all maintainance appointments")
async def _allappointments(ctx, *args):
  all_appointments = AppointmentModel.get_all()
  response = f""
  if all_appointments:
    for appointment in all_appointments:
      response += f"Drone Model: {appointment.drone_model}\n"
      response += f"Maintainer: {appointment.maintainer_name}\n"
      response += f"Start Time: {appointment.start_time}\n"
      response += f"End Time: {appointment.end_time}\n\n"
    message = discord.Embed(title="Displaying All Appointments", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No maintenance appointments found.")

@bot.command(name="flight_plans", description="show all flight plans")
async def _allplans(ctx, *args):
  all_plans = PlanModel.get_plans()
  response = f""
  if all_plans:
    for plan in all_plans:
      response += f"Planned By: {plan.planner_name}\n"
      response += f"Waypoints: {plan.waypoints}\n"
      response += f"Launch from {plan.launch_base} and recover at {plan.recovery_base}\n"
      response += f"Payload weight of {plan.weight} pounds with {plan.pylons} pylons\n\n"
    message = discord.Embed(title="Displaying All Flight Plans", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No flight plans found.")

@bot.command(name="users", description="show all users")
async def _allaccounts(ctx, *args):
  all_accounts = AccountModel.get_accounts()
  response = f""
  if all_accounts:
    for account in all_accounts:
      response += f"Username {account.username} belongs to {account.full_name}\n"
    message = discord.Embed(title="Displaying All Accounts", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No accounts found.")

@bot.command(name="devices", description="show all devices for a user")
async def _alldevices(ctx, arg1):
  all_devices = DeviceModel.get_all(arg1)
  response = f""
  if all_devices:
    for device in all_devices:
      response += f"{device.username} has {device.device_count} devices linked\n"
    message = discord.Embed(title="Displaying All Devices", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No devices found.")

@bot.command(name="devices_loggedin", description="show all devices that are logged in for a user")
async def _activedevices(ctx, arg1):
  all_devices = DeviceModel.get_active(arg1)
  response = f""
  if all_devices:
    for device in all_devices:
      response += f"{device.username} has {device.device_count} devices logged in\n"
    message = discord.Embed(title="Displaying All Logged-In Devices", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No logged in devices found.")

@bot.command(name="fleet", description="show all drones")
async def _alldrones(ctx, *args):
  all_drones = DroneModel.get_drones()
  response = f""
  if all_drones:
    for drone in all_drones:
      response += f"{drone.manufacturer} {drone.model_name}\n"
      response += f"Pilot: {drone.pilot_name}\n"
      response += f"Sensor Operator: {drone.sensor_name}\n"
      response += f"Maintainer: {drone.maintainer_name}\n\n"
    message = discord.Embed(title="Displaying Drone Fleet", description=response, color=0x00ff00)
    await ctx.send(embed=message)
  else:
    await ctx.send("No drones found.")

bot.run(TOKEN)
