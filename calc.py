print("~~~~A SIMPLE CALCULATOR~~~~")
import pyttsx3
engine=pyttsx3.init()
engine.say("welcome to the simple calculator")
engine.runAndWait()

num1= float(input("enter your first number: "))
num2= float(input("enter your second number: "))

print('''press "+" for addition.
press "-" for subtraction
press "*" for multiplication 
press "/" for division''')

choice= input("choose an option: ")
 
if(choice== "+"):
    result= num1+num2
    

elif(choice== "-"):
    result= num1-num2

elif(choice== "*"):
    result= num1*num2

elif(choice== "/"):
    result= num1/num2

else:
    print("invalid operator found")

print("the result of the operation is",result)