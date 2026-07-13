import random
# Generate random number between 50 to 100
random_number=random.randint(50,100)
print(random_number)

# Generate 6 digit otp
otp = random.randint(100000,999999)
print(otp)

# Create a list of five fruits and randomly print one fruit
fruits = ["Banana","Kevi","Apple","Cherry","Grapes"]
print(random.choice(fruits))