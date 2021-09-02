#We are going to write a program that either disables or engages a burglar alarm, depending on if the correct PIN (1234) is entered or not
f = input("Please enter PIN password.")
f = (float(f))
print("PIN entered: %s " %f)

if float(f)==1234:
    print("CORRECT - ALARM DEACTIVATED")
else:
    print("INCORRECT - ALARM ENGAGED ")