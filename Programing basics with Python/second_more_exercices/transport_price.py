# •	Първият ред съдържа числото n – брой километри – цяло число в интервала [1…5000]
# •	Вторият ред съдържа дума “day” или “night” – пътуване през деня или през нощта

kilometers = int(input())
period_for_travel = input()

total_sum_taxi_day = kilometers * 0.79 + 0.70
total_sum_taxi_night = kilometers * 0.90 + 0.70
total_sum_bus = kilometers * 0.09
total_sum_train = kilometers * 0.06

if kilometers < 20:
    if period_for_travel == "day":
        print(f'{total_sum_taxi_day:.2f}')
    else:
        print(f'{total_sum_taxi_night:.2f}')
elif kilometers >= 100:
    print(f'{total_sum_train:.2f}')
else:
    print(f'{total_sum_bus:.2f}')


