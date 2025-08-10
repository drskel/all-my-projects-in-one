#made by skel67
import string
import random
import time

letters = string.ascii_letters + " "
target = "Hello World"

def helloworld():
    result = ""
    for char in target:
        while True:
            guess = random.choice(letters)
            print(result + guess, end='\r')
            if guess == char:
                result += guess
                break
            time.sleep(0.05)
    print("\nDone:", result)

if __name__ == '__main__':
    helloworld()
    