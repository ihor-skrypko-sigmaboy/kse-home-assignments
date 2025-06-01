#task 1
part_one = "Заходить равлик у бар"
print(part_one + ', а бармен каже, що равликів не обслуговують')

#task 2
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
sum = x + y
substract = x - y
divide = x/y
divide_int = x//y
print(sum)
print(substract)
print(divide)
print(divide_int)

#task 3
phrase_one = "Why we are still here?"
phrase_two = "Just to suffer..."
print(f'{phrase_one} {phrase_two}')
print("{} {}".format(phrase_one, phrase_two))

#task 4
z = int(input("Enter any number: "))
if z%2 == 0:
    print("Odd")
else:
    print("Even")

#task 5
b = 1
while b <= 10:
    print(b)
    b+=1

#task 6
c = int(input("Enter your number: "))
if c>0:
    print("Positive")
elif c<0:
    print("Negative")
else:
    print("zero")

#task 7, завдання просто брутфорсом брав. Не одразу зрозумів, що треба починати лічбу з двійки.
for b in range (2,11,2):
    print(b)

#task 8 -----------------------------------------------------------------
a = 1
total = 0
n = int(input("Enter any number: "))
for i in range (1, 1 + n):
    total += i
print(total)

#task 9
r = 10
while r>=1:
    print(r)
    r-=1

#task 10  у цьому завданні найважче було зрозуміти яким чином вибудувати умову(розміщення іфок). 
for i in range(1,11):
    if i ==5:
        continue
    if i == 7:
        break
    print(i)

    