# •	На първия ред е броят на закупените хризантеми – цяло число в интервала [0 ... 200]
# •	На втория ред е броят на закупените рози – цяло число в интервала [0 ... 200]
# •	На третия ред е броят на закупените лалета – цяло число в интервала [0 ... 200]
# •	На четвъртия ред е посочен сезона – [Spring, Summer, Аutumn, Winter]
# •	На петия ред е посочено дали денят е празник – [Y – да / N - не]

chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_celebration_day = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
discount = 1
general_discount = 1
celebration_discount = 1

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
    if season == "Spring" and tulips_count > 7:
        discount = 0.95

elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
    if season == "Winter" and roses_count >= 10:
        discount = 0.9
if chrysanthemums_count + roses_count + tulips_count > 20:
    general_discount = 0.8
else:
    discount = discount
if is_celebration_day == "Y":
    celebration_discount = 1.15
total_price = (chrysanthemums_count * chrysanthemums_price + roses_count * roses_price\
    + tulips_count * tulips_price ) * celebration_discount * general_discount * discount + 2
print(f'{total_price:.2f}')
