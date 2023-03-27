import os

if __name__ == '__main__':
    print("Welcome to Robo Speaker Created by Ghost")
    while True:
        x = input("Enter what you want me to speak: ")
        if x== "q":
            os.system("Say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)

