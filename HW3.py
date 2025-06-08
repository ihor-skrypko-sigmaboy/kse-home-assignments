#part one ----------------------------------------------------------------------------

#task 1
a = [1,2,3,4,5,-6,7,8,9,10,52]
print(sum(a))

#task 2
print(min(a))

#task 3
print(a[ : : -1])

#task 4
for i in a:
    if i%2 != 0:
        print(i)

#task 5
n = int(input("Enter your crazy number: "))
for i in a:
    i*= n
    print(i)

#part two -----------------------------------------------------------------------------

#task 6
for i in a:
   if i>4:
       print(i)

#task 7
b=[]
for i in a:
    if i>0:
        b.append(i)
print(sum(b)/len(b))

#task 8
c=[]
for i in a:
    if i<10:
        c.append(i)
print(c)
print(len(c))

#task 9
a = [1,2,3,4,5,-6,7,8,9,10,52]
z = []
y = int(input("Enter your skibidi number: "))
for i in a:
    if i%y == 0:
        z.append(i)
print(sum(z))

#task 10
listkvadrat = []
for i in a:
    i**=2
    listkvadrat.append(i)
print(listkvadrat)

#task 11
a = [-11,23,-11,245,67,89,-120,-23,24]
b =[]
for i in a:
    if i>0:
        b.append(i)
print(b)

#task 12
list =["remind","recollect","remaster","replay","slavery","elon mask"]
listnew = []
for word in list:
   if 're' in word:
       listnew.append(word)
print(listnew)

#task 13
a = [-11,23,-11,245,67,89,-120,-23,24]
n = int(input("number: "))
print(sum(a[:n]))

#task 14
a = ['mom','taco cat','level','kayak','watermellon','wow','diddy']
anew = []
for word in a:
    if word == word[::-1]:
        anew.append(word)
print(anew)

#task 15
a = [12,23,45,56,57,17,20,78,124,905,84,92,52]
b = int(input("Enter number: "))
c = []
for i in a:
    if i%b == 0:
        i = True
        c.append(i)
    else:
        i = False
        c.append(i)
print(a)
print(c)

#part three --------------------------------------------------------------------------

#task 16
a = [12,23,34,54,45,67,76,32,90,120,597,47,343,91]
b = []
for i in a:
    if i%2 == 0:
        if i%3 != 0:
            b.append(i)
print(b)

#task 17
list = [["Чому у павука немає трусів?"], ["Бо він плете павутину і йому тепло"],  ["Автор ідеї МС Петя"]]
listnew = []
for i in list:
    for a in i:
        listnew.append(a)
print(list)
print(listnew)

#task 18
a = "NaSH sLoN"
a_list_of_capitals = []
for i in a:
    if i.isupper():
        a_list_of_capitals.append(i)
print(a_list_of_capitals)

#task 19
a = [1,2,3,4,5,6,7,8,9,2,6,3,1,2,4,5,2,7,4,8,1,9,4,5,3,2,1]
a_zaspadanyam = []
a_zaspadanyam = sorted(a, reverse = True)
print(a_zaspadanyam)
a_bezpovtoriv = []
a_bezpovtoriv = set(a_zaspadanyam)
print(a_bezpovtoriv)
a_frequency = {}
for i in a:
    if i not in a_frequency:
        a_frequency[i] = 1
    else:
        a_frequency[i] += 1
print(a_frequency)

#task 20 вивід дублікатів із двох списків
a = [1,2,3,4,5,6]
b = [4,5,6,7,8]
combined_list = []
for i in a:
    if i in b and i not in combined_list:
        combined_list.append(i)
print(combined_list)

#task 21 the first pain 
dihtionary = [
    {"a": 2, "b": 3},
    {"a": 4, "b": 2}
]
agregovaniy = {}
for i in dihtionary:
    for key, value in i.items():
        if key in agregovaniy:
            agregovaniy[key] += value
        else:
            agregovaniy[key] = value
print(agregovaniy)
    
#task 22
list_of_students = {"stundet_one": 90, "student_two": 95, "student_three": 86, "student_four": 65}
for key in list_of_students:
    if list_of_students[key] >= 90:
        list_of_students[key] = 'nash slon'
    elif 80 <= list_of_students[key] < 90:
        list_of_students[key] = 'nepogano'
    else:
        list_of_students[key] = 'zakryv i dobre'
print(list_of_students)

#task 23
a = ['Germany', 'Poland', 'Great Britain', 'Finland', 'Czech Republic', 'Spain', 'Danemark']
x = 6
count = 0
for i in a:
    if len(i) > 6:
        count += 1
print(count)

#task 24 the second pain
a = [12, 34, 56]
b = [21, 43, 65]
new_ab = []
for i in range(len(a)):
    new_ab.append(a[i])
    new_ab.append(b[i])
print(new_ab)

#task 25
a = [15,24,35,65,78,90,34,32,1,2,3,4,5,70,54,129]
X = 50
Y = 5
res = []
for i in a:
    if i > X:
        i *= Y
        res.append(i)
print(res)