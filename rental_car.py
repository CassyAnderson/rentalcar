import sys
import sys
'''
Section 1: Collect customer input
'''
#Rental Code
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
#Rental Period
if rentalCode == "W":
  rentalPeriod = int(input("Number of Weeks Rented:\n"))
else:
  rentalPeriod = int(input("Number of Days Rented:\n"))
#Starting odometer
odoStart = int(input("Starting Odometer Reading:\n"))
#Ending odometer
odoEnd = int(input("Ending Odometer Reading:\n"))
#Miles Driven             
totalMiles = odoEnd - odoStart
#Amount Due
baseCharge = 0
if rentalCode == "B":
  mileCharge = totalMiles * 0.25

if rentalCode == "D":
  averageDayMiles = totalMiles/rentalPeriod
  mileCharge = rentalPeriod * 60
  if averageDayMiles > 100:
    extraMiles = averageDayMiles - 100
    extraCharge = extraMiles * 0.25
    mileCharge = mileCharge + extraCharge
  else:
    extraMiles = 0

  
if rentalCode == "W":
  averageWeekMiles = totalMiles/rentalPeriod
  mileCharge = rentalPeriod * 190
  if averageWeekMiles > 900:
    extraCharge = 100 * rentalPeriod
    mileCharge = mileCharge + extraCharge
  else:
    extraCharge = 0

#Rental Summary
print("Rental Summary")
print("Rental Code:" + "  " + rentalCode)
print("Rental Period:" + "  " + str(rentalPeriod))
print("Starting Odometer:" + "  " + str(odoStart))
print("Ending Odometer:" + "  " + str(odoEnd))
print("Miles Driven:" + "  " + str(totalMiles))
print("Amount Due:" + "  $" + "%.2f" %mileCharge)