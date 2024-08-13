# your code goes here!
def countdown(numb):
    while numb > 0:
        print(f"{numb} SECOND(S)!")
        numb -= 1
    print("HAPPY NEW YEAR!")
import time

def countdown_with_sleep(numb):
    while numb > 0:
        print(f"{numb} SECOND(S)!")
        time.sleep(1)  # Pause for 1 second
        numb -= 1
    print("HAPPY NEW YEAR!")
