import random

choice = random.choice(['m','f'])
if choice == 'm':
    f = open('male.txt','r')
elif choice == 'f':
    f = open('female.txt','r')

c = 0
for line in f:
    c += 1
c -= 1
pick = random.randint(0,c)
f.seek(0)
i = 0
for line in f:
    if i == pick:
        print line
        break
    else:
        i+=1
