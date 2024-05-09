from time import sleep
sleep(5)
usecret = input("Write your secret word: ")

import os

# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text
print("The platform is: ", os.name)
print("big output\n"* 5)
# wait for 5 seconds to clear screen
sleep(5)
# now call function we defined above
screen_clear()

seclen = len(usecret)
secret = usecret.lower()
print("The secret word is",seclen,"characters long.")

while True:
    ulet = input("Guess a letter: ")
    let = ulet.lower()
    indpos = secret.find(let)
    if indpos >= 0:
        pos = indpos + 1
        print("Yes,",ulet,"is in the secret word in position",pos)
    else:
        print("Sorry, but",ulet,"isn't in the secret word. Try again.")








#spellsec = [secret[0],secret[1],secret[2],secret[3],secret[4],secret[5],secret[6],secret[7],secret[8],secret[9]]
#for character in spellsec:
    #print(character)

#while True:
#    guess = input("Guess the secret word: ")
#    gueslen = len(guess)
#    if guess == secret:
#        break
#    if gueslen != seclen:
#        print("Your guess is not the same length as the secret word! Try again...")
#        continue

#print("You guessed it! The secret word was:", secret)





#while True:
  #line = input('Guess my name: ')
  #if line == 'Marc' :
    #  break
  #if line[0] == 'M' :
    #  print("the first letter's right")
  #if line[1] == 'a' :
    #  print("the second letter's right")
  #if line[2] == 'r' :
    #  print("the third letter's right")
  #if line[3] == 'c' :
    #  print("the fourth letter's right")
  #continue
  #else:
    # print("That's not right at all, try again...")
#print("That's it, well done!")
