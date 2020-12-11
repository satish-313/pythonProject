import random

def checkInput(x):
  while True:
    if x == 'r':
      return x
    elif x == 'p':
      return x
    elif x == 's':
      return x
    else:
      return checkInput(input("for rock : r , for paper : p , for scissors : s check\n").lower())

def rockpaper(x,y):
  if x == 'r':
    if y == 'p':
      return False
    else:
      return True
  elif x == 'p':
    if y == 's':
      return False
    else:
      return True
  else:
    if y == 'r':
      return False
    else:
      return True

def main():
  rps = ['r','p','s']
  user = checkInput(input("for rock : r , for paper : p , for scissors : s\n").lower()) 
  computer = random.choice(rps)
  
  if user != computer:
    if (rockpaper(user,computer)):
      print(f"User is Won the Match, Computer uses {computer} ")
    else:
      print(f"User Lost the Match, Computer uses {computer} ")
  else:
    print("Both side are equal play again")
    main()


if __name__ == "__main__":
  main()