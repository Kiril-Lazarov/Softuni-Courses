from math import floor

processors_count = int(input())
people_count = int(input())
days_count = int(input())

work_hours = people_count * days_count * 8
done_processors = floor(work_hours / 3)
profit = done_processors * 110.1
diff = abs(profit - processors_count * 110.1)
if done_processors >= processors_count:
    print(f"Profit: -> {diff:.2f} BGN")

else:
    print(f"Losses: -> {diff:.2f} BGN")

#Add new comment


