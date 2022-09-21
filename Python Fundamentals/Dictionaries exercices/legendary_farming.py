def print_func(reached_item_name, items_dict, junk_dict):
    if reached_item_name == 'shards':
        reached_item_name = 'Shadowmourne'
    elif reached_item_name == 'fragments':
        reached_item_name = "Valanyr"
    elif reached_item_name == 'motes':
        reached_item_name = "Dragonwrath"
    print(f"{reached_item_name} obtained!")

    for key, value in items_dict.items():
        print(f"{key}: {value}")
    for key, value in junk_dict.items():
        print(f"{key}: {value}")


def legendary_item():
    items_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
    junk_dict = {}
    is_reached_item = False
    reached_item_name = ''
    while True:
        items = input().lower().split(' ')
        for i in range(len(items)):
            if i % 2 != 0:
                if items[i] not in items_dict:
                    if items[i] not in junk_dict:
                        junk_dict[items[i]] = int(items[i - 1])
                    else:
                        junk_dict[items[i]] += int(items[i - 1])
                else:
                    items_dict[items[i]] += int(items[i - 1])
                    if items_dict[items[i]] >= 250:
                        items_dict[items[i]] -= 250
                        is_reached_item = True
                        reached_item_name = items[i]
                        break
        if is_reached_item:
            break
    print_func(reached_item_name, items_dict, junk_dict)


legendary_item()
