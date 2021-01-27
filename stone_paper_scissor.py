import random
a= random.randint(1,3)
print("computer's turn : stone,paper,scissor")
if a==1:
    com='stone'
elif a==2:
    com='paper'
elif a==3:
    com='scissor'
you=input("your turn : stone,paper,scissor :   ")

print(f"computer chose   {com}")
print(f"you chose   {you}")


if com==you:
        print('match tie')
elif com=='stone':
    if you=='paper':
            print('you win')
    elif you=='scissor':
            print('you loss')
elif com=='paper':
    if you=='stone':
            print('you loss')
    elif you=='scissor':
            print('you win')
elif com=='scissor':
    if you=='stone':
            print('you win')
    elif you=='paper':
            print('you loss')




