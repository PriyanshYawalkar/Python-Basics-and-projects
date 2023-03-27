print("hello please enter your age to see you are eligliable to drive or not")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if(age>=18):
    print(name, "Yes, you can drive")
elif(age==2):
    print(name, "sorry, you are not eligliable")
else:
    print(name, "No")

print("Thank you")
