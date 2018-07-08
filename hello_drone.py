
from dronekit import connect
import serial
# Connect to the Vehicle.
vehicle = connect('/dev/cu.usbserial-DN00BA8M', wait_ready=True,baud=57600)
# Import DroneKit-Python

# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print " Battery: %s" % vehicle.battery
print " Last Heartbeat: %s" % vehicle.last_heartbeat
print " Is Armable?: %s" % vehicle.is_armable
print " System status: %s" % vehicle.system_status.state
print " Mode: %s" % vehicle.mode.name    # settable

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
print("Completed")
