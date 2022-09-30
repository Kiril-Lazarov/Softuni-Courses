# def print_func(players_tie_dict, summation_players_dict):
#     for name, points in summation_players_dict.items():
#         print(f"{name}: {points} skill")
#         for position, skills in players_tie_dict[name].items():
#             print(f'- {position} <::> {skills}')
#
#
# def sort_players(players_tie_dict):
#     summation_players_dict = {}
#     # rearrange by alphabetical order
#     players_tie_dict = {k: v for k, v in sorted(players_tie_dict.items(), key=lambda k: k[0])}
#     for name, tie in players_tie_dict.items():
#         # rearrange by alphabetical order
#         tie = {k: v for k, v in sorted(tie.items(), key=lambda k: k[0])}
#         # rearrange by points in descending order
#         tie = {k: v for k, v in sorted(tie.items(), key=lambda v: v[1], reverse=True)}
#         players_tie_dict[name] = tie
#         sum_points = sum(list(players_tie_dict[name].values()))
#         summation_players_dict[name] = sum_points
#     # rearrange by alphabetical order
#     summation_players_dict = {k: v for k, v in sorted(summation_players_dict.items(), key=lambda k: k[0])}
#     # rearrange by points in descending order
#     summation_players_dict = {k: v for k, v in
#                               sorted(summation_players_dict.items(), key=lambda v: v[1], reverse=True)}
#     print_func(players_tie_dict, summation_players_dict)
#
#
# def battle(player1, player2, players_tie_dict):
#     has_ended = False
#     total_points_player1 = 0
#     total_points_player2 = 0
#     for position_first_player, points_first_player in players_tie_dict[player1].items():
#         for position_second_player, points_second_player in players_tie_dict[player2].items():
#             if position_first_player == position_second_player:
#                 total_points_player1 += points_first_player
#                 total_points_player2 += points_second_player
#                 if total_points_player1 != total_points_player2:
#                     if total_points_player1 > total_points_player2:
#                         del players_tie_dict[player2]
#                         has_ended = True
#                         break
#                     elif total_points_player1 < total_points_player2:
#                         del players_tie_dict[player1]
#                         has_ended = True
#                         break
#         if has_ended:
#             break
#     return players_tie_dict
#
#
# def challenger_inputs():
#     players_tie_dict = {}
#     data = input()
#     while data != 'Season end':
#         if '->' in data:
#             data = data.split(' -> ')
#             player, position, skills = data[0], data[1], int(data[2])
#             if len(players_tie_dict) == 0:
#                 players_tie_dict[player] = {position: skills}
#             if player not in players_tie_dict:
#                 players_tie_dict[player] = {position: skills}
#             else:
#                 if position not in players_tie_dict[player]:
#                     players_tie_dict[player][position] = skills
#                 else:
#                     if skills > players_tie_dict[player][position]:
#                         players_tie_dict[player][position] = skills
#         elif 'vs' in data:
#             data = data.split(' vs ')
#             player1 = data[0]
#             player2 = data[1]
#             if player1 in players_tie_dict and player2 in players_tie_dict:
#                 battle(player1, player2, players_tie_dict)
#         data = input()
#     sort_players(players_tie_dict)
#
#
# challenger_inputs()

players_pool = {}
while True:
    data = input()
    if data == "Season end":
        break
    if "->" in data:
        player, position, skill = data.split(" -> ")
        if player not in players_pool:
            players_pool[player] = {position: int(skill)}
        else:
            if position not in players_pool[player]:
                players_pool[player][position] = int(skill)
            else:
                players_pool[player][position] = max(players_pool[player][position], int(skill))
    else:
        player1, player2 = data.split(" vs ")
        is_battle = False
        if player1 in players_pool and player2 in players_pool:
            for position in players_pool[player1]:
                if position in players_pool[player2]:
                    is_battle = True
            if is_battle:
                if sum(players_pool[player1].values()) > sum(players_pool[player2].values()):
                    del players_pool[player2]
                elif sum(players_pool[player1].values()) < sum(players_pool[player2].values()):
                    del players_pool[player1]
total_points_dict = {}
for name in players_pool:
    total_points_dict[name] = sum(players_pool[name].values())
total_points_dict = {k:v for k, v in sorted(total_points_dict.items(), key= lambda x:x[0])}
total_points_dict = {k: v for k, v in sorted(total_points_dict.items(), key=lambda x: x[1], reverse=True)}
for name in total_points_dict:
    players_pool[name] = {k: v for k, v in sorted(players_pool[name].items(), key=lambda x: x[0])}
    players_pool[name] = {k: v for k, v in sorted(players_pool[name].items(), key=lambda x: x[1], reverse=True)}
    print(f"{name}: {total_points_dict[name]} skill")
    for position, skill in players_pool[name].items():
        print(f"- {position} <::> {skill}")
