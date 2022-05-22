primes_sum = 0
non_primes_sum = 0
command = input()


while command != 'stop':
    number = int(command)

    if int(command) < 0:
        print("Number is negative.")

    else:
        for i in range(2, number + 1):

            if number % i == 0:

                if number // i > 1:
                    non_primes_sum += number
                    break
                else:
                    primes_sum += number
                    break

    command = input()
print(f"Sum of all prime numbers is: {primes_sum}")
print(f"Sum of all non prime numbers is: {non_primes_sum}")
