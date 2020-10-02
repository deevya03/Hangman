import random
import time as t
t.perf_counter()


name = input("What's your good name? ")

print(f"Good Luck ! {name}")

def randomWords():

  words = ['rainbow', 'computer', 'science', 'programming', 
          'python', 'mathematics', 'player', 'condition', 
          'reverse', 'water', 'board', 'geeks'] 
  word=random.choice(words)
  print(word)
  return word


def playGame(word):
  print("Guess the characters")

  guesses = ''
  turns = 10
  tic = t.perf_counter()
  ls = []
  while turns > 0:


      failed = 0 # counts the number of times a user fails
      for char in word:

          if char in guesses:
              print(char, end=' ')

          else:
              print("_  ", end='')

              failed += 1

      if failed == 0:
          print("\n-----------")
          print("You Won")
          print("-----------")
          
          print("The word is: ", word)
          break

      guess = input("\n\nguess a character:")[0]
      if guess in ls:
          print("Character already given")
          continue;
      ls.append(guess)
      guesses += guess

      if guess not in word:

          turns -= 1
          print("Wrong")
          print("You have", +turns, 'more guesses')

          if turns == 0:
              print("You Loose")
              print("The word was: ", word)
      
      toc = t.perf_counter()
  print(f"Total time taken: {toc - tic:0.2f} seconds")

word=randomWords()
playGame(word)
