from dronekit import connect
import serial
# Connect to the Vehicle.
vehicle = connect('/dev/cu.usbserial-DN00BA8M', wait_ready=True,baud=57600)
# Import DroneKit-Python

# Get some vehicle attributes (state)
print "connected to %s" % vehicle.version
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


'''
 Vehicle.version
 Vehicle.location.capabilities
 Vehicle.location.global_frame
 Vehicle.location.global_relative_frame
 Vehicle.location.local_frame
  Vehicle.attitude
  Vehicle.velocity
  Vehicle.gps_0
  Vehicle.gimbal
  Vehicle.battery
  Vehicle.rangefinder
  Vehicle.last_heartbeat
  Vehicle.home_location
  Vehicle.rangefinder
  Vehicle.ekf_ok
  Vehicle.last_heartbeat
   Vehicle.home_location
   Vehicle.system_status
   Vehicle.heading
   Vehicle.is_armable
   Vehicle.airspeed
   Vehicle.groundspeed
   Vehicle.armed
   Vehicle.mode

   All of the attributes can be read,
   but only the Vehicle.home_location,
   Vehicle.gimbal Vehicle.airspeed,
   Vehicle.groundspeed,
   Vehicle.mode and Vehicle.armed  status can be set.'''
