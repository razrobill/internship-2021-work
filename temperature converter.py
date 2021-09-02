#We are going to write a program that asks the user for a temperature in Celsius and prints out the same temperature in Fahrenheit
f = input("Please input a temperature in Celsius. ")
f = (float(f) * 9/5) + 32
print ("Your temperature in Fahrenheit is: %s." %f)

#To make things neater, we are going to round the temperature to the nearest whole number.
f = input("Please input a temperature in Celsius. ")
f = round((float(f) * 9/5) + 32 ,0 )
print ("Your temperature in Fahrenheit is: %s." %f)

#Now we will give the user the choice to convert from Celsius to Fahrenheit or vice versa.
choice = input("Press 1 to convert from Celsius to Fahrenheit or Press 2 to convert from Fahrenheit to Celsius.")
temp = input("What is the number that you would like to convert? ")

if float(choice)==1:
    temp = (float(temp) * 9/5) + 32
    print ("Your temperature in Fahrenhiet is: %s." %temp)
elif float(choice)==2:
    temp = (float(temp) - 32) * 5/9   
    print ("Your temperature in Celsius is: %s." %temp)
else:
    print ("Please input 1 or 2")    