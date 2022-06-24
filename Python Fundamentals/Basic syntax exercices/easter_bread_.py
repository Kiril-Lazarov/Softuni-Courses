budget = float(input())
price_flour = float(input())
price_eggs = 0.75 * price_flour
price_milk = 1.25 * price_flour
gathered_eggs = 0
price_for_one_bread = price_flour + price_eggs + price_milk/4
current_bread_count = 0
while price_for_one_bread < budget:
    budget -= price_for_one_bread
    current_bread_count +=1
    gathered_eggs +=3
    if current_bread_count % 3==0:
        gathered_eggs -= current_bread_count - 2
print(f"You made {current_bread_count} loaves of Easter bread! Now you have {gathered_eggs} eggs and {budget:.2f}BGN left.")