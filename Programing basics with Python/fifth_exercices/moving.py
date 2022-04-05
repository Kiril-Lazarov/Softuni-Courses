# 1.	Широчина на свободното пространство - цяло число;
# 2.	Дължина на свободното пространство - цяло число;
# 3.	Височина на свободното пространство - цяло число;
# 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа

width = int(input())
lenght = int(input())
hight = int(input())

volume = width * lenght * hight
num_boxes = input()
while True:
    volume -= int(num_boxes)
    if volume > 0:

        num_boxes = input()
    else:
        print(f"No more free space! You need {abs(volume)} Cubic meters more.")
        break
    if num_boxes == "Done":
        print(f"{volume} Cubic meters left.")
        break