# •	Последния сектор от секторите - символ (B-Z)
# •	Броят на редовете в първия сектор - цяло число (1-100)
# •	Броят на местата на нечетен ред - цяло число (1-24)

last_sector = input()
rows_first_sector = int(input())
seats_odd_row = int(input())

first_symbol = ''
second_symbol = 0
third_symbol = ''
last_sector_count = 0
seats_count = 0
for sector in range(ord('A'), ord(last_sector) + 1):
    first_symbol = chr(sector)
    if sector <= ord('A'):
        for rows in range(1, rows_first_sector + 1):
            second_symbol = rows
            if rows % 2 == 1:
                seats = seats_odd_row
            else:
                seats = seats_odd_row + 2
            for i in range(1, seats + 1):
                third_symbol = chr(i + 96)
                seats_count += 1
                print(f'{first_symbol}{second_symbol}{third_symbol}')
    else:
        last_sector_count +=1
        for rows in range(1, rows_first_sector + 1 + last_sector_count):
            second_symbol = rows
            if rows % 2 == 1:
                seats = seats_odd_row
            else:
                seats = seats_odd_row + 2
            for i in range(1, seats + 1):
                third_symbol = chr(i + 96)
                seats_count += 1
                print(f'{first_symbol}{second_symbol}{third_symbol}')
print(seats_count)
