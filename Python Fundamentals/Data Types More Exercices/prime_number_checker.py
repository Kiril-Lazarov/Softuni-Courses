number = int(input())
isPrime = True
for i  in range(2,int(number/2)):
    if number % i==0:
        isPrime = False
        break
if isPrime:
    print('True')
else:
    print('False')