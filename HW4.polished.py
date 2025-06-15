import random

all_tries = 6 #виніс константу вище за всі, бо є чітке цифрове значення
words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker'] #прибра зайві пробіли
def word_choice(): #зробив функцію, яка вибирає випадкове число зі списку
    return random.choice(words) #прибрав змінні x, y, z  

def game_start(): #додав функцію, що означає запуск гри
  secret_word = word_choice() #додав зміну із цільовим словом 
  word_length = len(secret_word)
  ingame_tries = all_tries  #тут додав інгейм для розуміння типу спроб. їх загалом 6, але в середині гри їх стає менше і менше.
  
  print("Welcome to Wordle!")
  print("Guess the", word_length, "-letter word. You have", ingame_tries, "tries.")

  while ingame_tries > 0:
      try:    #функція приймає будь-які значення (від цифр до спеціальних символів)
        guess = input("Attempt "+str(7 - ingame_tries)+"/6 – Enter guess: ").lower()
      except TypeError:   #така перевірка ніщо не змінила, тут потрібно створити перевірку на спеціальні символи та цифри
         print("You must type in a word, not number(s)") 
      if len(guess) != word_length:
        print("Wrong length. Expected", word_length)
        continue

      if guess == secret_word:
        print("You win!!!")
        break

      result=[]; i=0
      while i < word_length:
        character = guess[i]          #ch відповідає за літеру, character для кращого розуміння
        if character == secret_word[i]:
            result.append('correct')
        elif character in secret_word:
            result.append('present')
        else:
            result.append('absent')
        i+=1

      display=[]
      j=0
      while j < word_length:
        s = guess[j]
        res = result[j]
        if res =='correct':
            display.append("["+s.upper()+"]")
        elif res =='present':
            display.append("("+s+")")
        else:
            display.append(" "+s+" ")
        j+=1

      junk = ''.join([c for c in display if c])
      print("Result:", ' '.join(display))
      ingame_tries = ingame_tries - 1
  else:
    final = secret_word
    print("You lose! The word was:", final)

while True:         #loop який закриває або перезапускає гру
    game_start()
    again = input("Let's play again? Yes/No: ")
    if again != "Yes":
        print("See you soon!")
        break