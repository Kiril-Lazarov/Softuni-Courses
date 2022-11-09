numbers_list = input().split()
rounded_list = []

def rounds(numbers_list):
    for i in numbers_list:
        result = round(float(i))
        rounded_list.append(result)
    return rounded_list


print(rounds(numbers_list))
