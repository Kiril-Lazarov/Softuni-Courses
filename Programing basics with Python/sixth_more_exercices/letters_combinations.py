# Ред 1.	Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
# Ред 2.	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
# Ред 3.	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.

start_letter = input()
final_letter = input()
forbidden_letter = input()

first_letter = ''
second_letter = ''
third_letter = ''
combinations_counter = 0
for i1 in range(ord(start_letter), ord(final_letter) + 1):
    if i1 != ord(forbidden_letter):
        first_letter = chr(i1)
        for i2 in range(ord(start_letter), ord(final_letter) + 1):
            if i2 != ord(forbidden_letter):
                second_letter = chr(i2)
                for i3 in range(ord(start_letter), ord(final_letter) + 1):
                    if i3 != ord(forbidden_letter):
                        third_letter = chr(i3)
                        combinations_counter += 1
                        print(f'{first_letter}{second_letter}{third_letter}', end=' ')
print(f'{combinations_counter}')
