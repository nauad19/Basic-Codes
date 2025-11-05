import math
import random
import os

print("Module 1: math (Square Root and Pi)")
number = 144
root = math.sqrt(number)
print(f"Square root of {number} is: {root}")
print("Value of Pi is:", math.pi)

print("\nModule 2: random (Dice Roll)")
roll = random.randint(1, 6)
print(f"Rolling a 6-sided die: {roll}")
random_float = random.random()
print("Random float between 0.0 and 1.0:", random_float)

print("\nModule 3: os (Current Working Directory)")
current_dir = os.getcwd()
print("Current working directory is:", current_dir)
