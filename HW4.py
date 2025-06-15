import random

words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
x = random.random()
y = x * len(words)
z = int(y)
secret_word = words[z]

tries = 6
word_length = len(secret_word)
word = secret_word

print("Welcome to Wordle!")
print("Guess the",word_length,"-letter word. You have", tries, "tries.")

while tries!=0:
    guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
    
    if len(guess)!=word_length:
        print("Wrong length. Expected", word_length)
        continue

    if guess==word:
        print("You win!!!")
        break

    result=[]; i=0
    while i<word_length:
        ch = guess[i]
        if ch==word[i]:
            result.append('correct')
        elif ch in word:
            result.append('present')
        else:
            result.append('absent')
        i+=1

    display=[]
    j=0
    while j<word_length:
        s = guess[j]
        res = result[j]
        if res=='correct':
            display.append("["+s.upper()+"]")
        elif res=='present':
            display.append("("+s+")")
        else:
            display.append(" "+s+" ")
        j+=1

    junk = ''.join([c for c in display if c])
    print("Result:", ' '.join(display))
    tries = tries - 1
else:
    final = secret_word
    print("You lose! The word was:", final)