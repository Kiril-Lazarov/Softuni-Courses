cards = input().split(' ')
n = int(input())
initial_cards_list = []
slice_list = []
listA = []
listB = []
final_list =[]
for i in range(len(cards)):
    if cards[i] != ' ':
        initial_cards_list.append(cards[i])
slice_list = initial_cards_list[1:len(initial_cards_list) - 1]
listA = slice_list[:int(len(slice_list)/2)]
listB = slice_list[int(len(slice_list)/2):]
for i in range(n):
    for j in range(int(len(slice_list)/2)):
        final_list.append(listB[j])
        final_list.append(listA[j])
    slice_list = final_list
    listA = slice_list[:int(len(slice_list) / 2)]
    listB = slice_list[int(len(slice_list) / 2):]
    final_list = []
slice_list.insert(0,initial_cards_list[0])
slice_list.append(initial_cards_list[-1])
print(slice_list)