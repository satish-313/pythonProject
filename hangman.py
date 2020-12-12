import random
from wordListForHangman import words

def valid_word(words):
  word = random.choice(words)
  while " " in word or "-" in word:
    word = random.choice(words)
  word = word.upper()
  return word

def display_user_inputs(x):
  print("USER USED CHAR : ",end="")
  for i in x:
    if i != None:
      print(i,end=" ")

def valid_user_input(x):
  if " " in x:
    x = x.replace(" ","")
  if len(x) == 1:
    return x
  else:
    x = valid_user_input(input("Guess any correct letter : ").upper())

""" def if_letter_exit_word(b,i,w):
  for index,value in enumerate(w):
    if value == i:
      ind = str(index)
      if value in b:
        b[i] += ind
      else:
        b[i] = ind
  return b """

def replace_letter(b,w):
  _ = "_"
  final_string_list = [_ for i in range(len(w))]
  for a in b:
    for i,v in enumerate(w):
      if a == v:
        final_string_list[i] = v

  return final_string_list

def main():
  word = valid_word(words)
  user_input = set ()
  #blank = {}
  present_in_word = set ()
  T = True
  life = len(word)
  
  while T:
    inputs = valid_user_input(input("Guess any letter : ").upper())
    
    if inputs in word:
      present_in_word.add(inputs)
      #if_letter_exit_word(blank,inputs,word)
    else:
      if len(present_in_word) == 0:
        life = len(word)
      else:
        life -= 1
  
    strings = replace_letter(present_in_word,word)
    user_input.add(inputs)
    display_user_inputs(user_input)
    print("\n"," ".join(strings))
    print("LIFE : ",life)
    if "_" in strings:
      T = True
    else:
      T = False
    
    if life == 0:
      print("You loose the game !!!")
      print("Word is : ",word)
      break

if __name__ == "__main__":
  main()