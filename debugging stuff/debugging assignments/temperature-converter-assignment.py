f = input("Please input a temperature in Celsius. ")
f = round((float(f) * 9/5) + 32 ,0 )
print ("Your temperature in Fahrenheit is: s." %f)

choice = input("Press 1 to convert from Celsius to Fahrenheit or Press 2 to convert from Fahrenheit to Celsius.")
temp = input("What is the number that you would like to convert? )

if float(choice)==1:
    temp = ((temp) * 9/5) + 32
    print ("Your temperature in Fahrenhiet is: %s." %temp)
elif float(choice)==2:
    temp = (float(temp) - 32) * 9/5   
    print ("Your temperature in Celsius is: %s." %temp)
else:
print ("Please input 1 or 2") 