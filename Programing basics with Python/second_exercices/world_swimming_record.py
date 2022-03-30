
record = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter + (distance // 15) * 12.5
if total_time < record:
    print(f" Yes, he succeeded! The new world record is {abs(total_time):.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(total_time - record):.2f} seconds slower.")


