# WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours
# up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour
# to test the  program (the pay should be 498.75). You should use input to read a string and float to convert the
# string to a number.

hours = int(input("Input the hours"))
rate = float(input("Input rate per hour"))

if hours > 40:
    extra_hours = (hours - 40)
    bonus = extra_hours * 1.5 * rate
    gross_pay = bonus + ((hours - extra_hours) * rate)
    print(f"The gross pay with bonus of {bonus} is {gross_pay}")
else:
    gross_pay = hours * rate
    print(f"The gross pay is {gross_pay}")

