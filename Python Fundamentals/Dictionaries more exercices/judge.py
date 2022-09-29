def print_func(judge_dict, contest_dict):
    for contest, value in contest_dict.items():
        final_dict = {}
        final_dict = value
        final_dict = {k: v for k, v in sorted(final_dict.items(), key=lambda k: k[0])}
        final_dict = {k: v for k, v in sorted(final_dict.items(), key=lambda k: k[1], reverse=True)}
        number = len(final_dict)
        print(f"{contest}: {number} participants")
        index = 1
        for name, points in final_dict.items():
            print(f'{index}. {name} <::> {points}')
            index += 1
    standings_dict = {}
    for name in judge_dict:
        for value in judge_dict[name].values():
            sum_points = sum(judge_dict[name].values())
            standings_dict[name] = sum_points
    standings_dict = {k: v for k, v in sorted(standings_dict.items(), key=lambda k: k[0])}
    standings_dict = {k: v for k, v in sorted(standings_dict.items(), key=lambda k: k[1], reverse=True)}
    print('Individual standings:')
    index = 1
    for name, points in standings_dict.items():
        print(f'{index}. {name} -> {points}')
        index += 1


def sort_func(judge_dict, contest_by_order):
    contest_dict = {}
    final_contest_dict = {}
    for user in judge_dict:
        for contest, points in judge_dict[user].items():
            if contest not in contest_dict:
                contest_dict[contest] = {user: points}
            else:
                contest_dict[contest][user] = points
    for contest in contest_by_order:
        final_contest_dict[contest] = contest_dict[contest]
    contest_dict = final_contest_dict
    print_func(judge_dict, contest_dict)


def judge():
    judge_dict = {}
    contest_by_order = list()
    data = input()
    while data != "no more time":
        data = data.split(' -> ')
        username, contest, points = data[0], data[1], int(data[2])
        if contest not in contest_by_order:
            contest_by_order.append(contest)
        if len(judge_dict) == 0:
            judge_dict[username] = {contest: points}
        else:
            if username not in judge_dict:
                judge_dict[username] = {contest: points}
            else:
                if contest not in judge_dict[username]:
                    judge_dict[username][contest] = points
                else:
                    if points > judge_dict[username][contest]:
                        judge_dict[username][contest] = points
        data = input()
    sort_func(judge_dict, contest_by_order)


judge()
