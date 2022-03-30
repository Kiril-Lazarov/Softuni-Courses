# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"

juniors_count = int(input())
seniors_count = int(input())
trace = input()

juniors_tax= 0
seniors_tax= 0
discount = 1
if trace == "trail":
    juniors_tax = 5.5
    seniors_tax = 7

elif trace == "cross-country":
    juniors_tax = 8
    seniors_tax = 9.5
    if juniors_count + seniors_count >= 50:
        discount = 0.75

elif trace == "downhill":
    juniors_tax = 12.25
    seniors_tax = 13.75

elif trace == "road":
    juniors_tax = 20
    seniors_tax = 21.50

total_sum = (juniors_tax * juniors_count + seniors_count * seniors_tax) * discount * 0.95
print(f'{total_sum:.2f}')