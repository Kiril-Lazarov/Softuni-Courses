gifts_list = input().split(' ')
command = input()

while command != "No Money":
    gift_state = command.split(' ')
    if gift_state[0] == "OutOfStock":
        while gift_state[-1] in gifts_list:
            index = gifts_list.index(gift_state[-1])
            gifts_list[index] = "None"
    elif gift_state[0] == "Required":
        if 0 <= int(gift_state[-1]) < len(gifts_list):
            gifts_list[int(gift_state[-1])] = gift_state[1]
    elif gift_state[0] == "JustInCase":
        gifts_list[-1] = gift_state[-1]
    command = input()
if "None" in gifts_list:
    while "None" in gifts_list:
        gifts_list.remove("None")
print(' '.join(gifts_list))