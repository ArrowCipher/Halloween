import random
import time
print('Error, the code is undefined')
def prank():
  message = random.choice([
    "I see you!",
    "The ghost of Halloween past is here!",
    "The witch is coming to get you!",
    "The headless horseman is riding through the night!",
    "The vampires are out tonight!",
    "You thought you escaped"
  ])

  time.sleep(8)
  print(message)

if __name__ == "__main__":
  prank()
