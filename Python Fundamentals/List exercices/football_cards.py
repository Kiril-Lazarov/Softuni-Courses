cards = input()
list_cards = []
list_teamA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_teamB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
string = ''
player_out = 0
number_list = []
number = ''
test_number = ''
letter_list = []
for i in range(len(cards)):
    if cards[i] != ' ':
        string += cards[i]

    else:
        list_cards.append(string)
        string = ''
list_cards.append(string)
for j in range(len(list_cards)):
    number = list_cards[j]
    letter_list.append(number[0])
    if len(number) == 3:
        number_list.append(int(number[2]))
    elif len(number) == 4:
        test_number += number[2]
        test_number += number[3]
        number_list.append(int(test_number))
        test_number = ''


for i in range( len(letter_list)):
    if letter_list[i] == 'A':
        player_out = number_list[i]
        if player_out in list_teamA:
            list_teamA.remove(player_out)
    elif letter_list[i] == 'B':
        player_out = number_list[i]
        if player_out in list_teamB:
            list_teamB.remove(player_out)

    if len(list_teamA) < 7 or len(list_teamB) < 7:
        break
print(f"Team A - {len(list_teamA)}; Team B - {len(list_teamB)}")
if len(list_teamA) < 7 or len(list_teamB) < 7:
    print("Game was terminated")