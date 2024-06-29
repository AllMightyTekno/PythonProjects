import random
import os

# Shuffling function handler
def Shuffle(String):
    templist = list(String)  # Convert the input String into a list of characters
    random.shuffle(templist)  # Shuffle the list of characters randomly
    return "".join(templist)  # Join the shuffled list back into a string and return it

#Character And Integer Randomizer section
upperCaseLetter1 = chr(random.randint(65,90))  # Generate a random uppercase letter in ASCII
upperCaseLetter2 = chr(random.randint(65,90)) 
lowerCaseLetter1 = chr(random.randint(97,122))
lowerCaseLetter2 = chr(random.randint(97,122))

# Generating Password an    d Reshufflement
password = upperCaseLetter1 + upperCaseLetter2 + lowerCaseLetter1 + lowerCaseLetter2
password = Shuffle(password)


#Specify path to the desktop where file will be stored
desktop_path = os.path.join(os.path.expanduser('~'),'Desktop')

#Creating a new  File in the system
file_path = os.path.join(desktop_path, 'password.txt')
with open(file_path, 'w') as f:
    f.write(password)

# Program Output
print(password)
