# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is the bass class
class Vehicle:
  pass

#Vehicle is parent to GroundVehicle
class GroundVehicle(Vehicle):
  pass

#GroundVehicle is parent to Car
class Car(GroundVehicle):
  pass

#GroundVehicle is parent to Motorcycle
class Motorcycle(GroundVehicle):
  pass

#Vehicle is parent to FlightVehicle
class FlightVehicle(Vehicle):
  pass

#FlightVehicle is parent to Starship
class Starship(FlightVehicle):
  pass

# FlightVehicle is parent to Airplane
class Airplane(FlightVehicle):
  pass