# 1.	Брой монети по 1лв. - цяло положително число;
# 2.	Брой монети по 2лв. - цяло положително число;
# 3.	Брой банкноти по 5лв. - цяло положително число;
# 4.	Сума - цяло положително число в интервала [1…1000];

one_num = int(input())
two_num = int(input())
five_num = int(input())
total_sum = int(input())

# count_one = 0
# count_two = 0
# count_five = 0

for one in range(one_num+1):
    # count_one = one
    for two in range(two_num+1):
        # count_two = two
        for five in range(five_num+1):
            # count_five = five
            if one + two * 2 + five * 5 == total_sum:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {total_sum} lv.")
