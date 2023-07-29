print("Choose from below options:")
print("1.Celsius to Fahrenheit.")
print("2.Fahrenheit to Celsius.")
o=int(input("Enter choice:"))
if(o==1):
    c=float(input("Temperature in Celsius:"))
    f=1.8*(c)+32.0
    f=round(f,1) 
    print("Temperature in Fahrenheit:",f)
elif(o==2):
    f=float(input("Temperature in Fahrenheit:"))
    c=(f-32)/1.8
    c=round(c,1) 
    print("Temperature in Celsius:",c)
else:
    print("Wrong input")
