# def best_student(submissions_dict):
#     best_score = 0
#     student = ''
#     for name, value in submissions_dict.items():
#         score = 0
#         for values in submissions_dict[name].values():
#             score += values
#         if score > best_score:
#             best_score = score
#             student = name
#     print(f"Best candidate is {student} with total {best_score} points.")
#     sorted_list = sorted(submissions_dict)
#     sorted_points_list = []
#     print('Ranking:')
#     for name in sorted_list:
#         points_list = list(submissions_dict[name].values())
#         course = list(submissions_dict[name])
#         final_dict = dict(zip(points_list, course))
#         sorted_points_list = sorted(points_list)
#         sorted_points_list = sorted_points_list[::-1]
#         print(f'{name}')
#         course = list(submissions_dict[name])
#         for points in sorted_points_list:
#             print(f'#  {final_dict[points]} -> {points}')
#
#
# def submissions_validate(contest_dict):
#     submissions_dict = {}
#     text = input()
#     while text != "end of submissions":
#         text = text.split('=>')
#         contest, password, username, points = text[0], text[1], text[2], int(text[3])
#         if contest in contest_dict:
#             if password in contest_dict.values():
#                 if len(submissions_dict) == 0:
#                     submissions_dict[username] = {contest: points}
#                 if username not in submissions_dict:
#                     submissions_dict[username] = {contest: points}
#                 else:
#                     if contest not in submissions_dict[username]:
#                         submissions_dict[username][contest] = points
#                     else:
#                         if points > submissions_dict[username][contest]:
#                             submissions_dict[username][contest] = points
#
#         text = input()
#     best_student(submissions_dict)
#     return submissions_dict
#
#
# def contests():
#     contest_dict = {}
#     text = input()
#     while text != 'end of contests':
#         text = text.split(':')
#         if text[0] not in contest_dict:
#             contest_dict[text[0]] = text[1]
#         text = input()
#
#     submissions_validate(contest_dict)
#
#
# contests()
# contests = {}  # contests {contest: password}
# submissions = {}  # submissions {user: {contest: points}}
#
# while True:
#     input_line = input()
#     if input_line == 'end of contests':
#         break
#     contest, password = input_line.split(':')
#     contests[contest] = password
#
# while True:
#     input_line = input()
#     if input_line == 'end of submissions':
#         break
#     contest, password, user, pts = input_line.split('=>')
#     if contest in contests and contests.get(contest) == password:
#         if user in submissions:
#             submissions[user][contest] = max(submissions[user].get(contest, 0), int(pts))
#         else:
#             submissions[user] = {contest: int(pts)}
#
# user_total_pts = sorted([(sum(submissions[user].values()), user) for user in submissions.keys()], reverse=True)
# print(f"Best candidate is {user_total_pts[0][1]} with total {user_total_pts[0][0]} points.")
#
# print('Ranking:')
# for user in sorted([user for user in submissions.keys()]):
#     user_submissions = [u_s for u_s in sorted(submissions[user].items(), key=lambda item: -item[1])]
#     output = [f'#  {contest} -> {points}' for (contest, points) in user_submissions]
#     print(user)
#     print(*output, sep='\n')
contest_dict = {}
users = {}
while True:
    data = input()
    if data == "end of contests":
        break
    info = data.split(":")
    contest_dict[info[0]] = info[1]

while True:
    data = input()
    if data == "end of submissions":
        break
    contest, password, username, points = data.split("=>")
    if contest in contest_dict and password == contest_dict[contest]:
        if username in users:
            if contest in users[username]:
                users[username][contest] = max(users[username][contest], int(points))
            else:
                users[username][contest] = int(points)
        else:
            users[username] = {contest: int(points)}
best_student = {"Name": '', "Points": 0}
users = {k: v for k, v in sorted(users.items(), key = lambda x: x[0])} #sorting users by name in ascend order
for name in users:
    users[name]= {k:v for k, v in sorted(users[name].items(), key = lambda x: x[1], reverse= True)}
    total = 0
    for key, value in users[name].items():
        total += value
    if total > best_student["Points"]:
        best_student["Name"] = name
        best_student['Points'] = total
print(f'Best candidate is {best_student["Name"]} with total {best_student["Points"]} points.')
print("Ranking:")
for name in users:
    print(name)
    for contest, points in users[name].items():
        print(f"#  {contest} -> {points}")