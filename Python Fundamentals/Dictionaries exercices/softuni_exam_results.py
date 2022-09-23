def data_processing(data_dict, name, points):
    if name not in data_dict:
        data_dict[name] = points
    if data_dict[name] <= points:
        data_dict[name] = points


def langague_processing(language, language_submissions_dict):
    if language not in language_submissions_dict:
        language_submissions_dict[language] = 0
    language_submissions_dict[language] += 1


def banned(data_dict, name, language, language_submissions_dict):
    for key, value in data_dict.items():
        if key == name:
            del data_dict[key]
            break



def print_func(data_dict, language_submissions_dict):
    print('Results:')
    for key, value in data_dict.items():
        print(f'{key} | {value}')
    print('Submissions:')
    for key, value in language_submissions_dict.items():
        print(f'{key} - {value}')


def exams():
    data_dict = {}
    language_submissions_dict = {}
    command = input()
    while command != 'exam finished':
        data = command.split('-')
        name = data[0]
        if data[1] != 'banned':
            language = data[1]
            points = int(data[2])
            data_processing(data_dict, name, points)
            langague_processing(language, language_submissions_dict)
        else:
            language = data[1]
            banned(data_dict, name, language, language_submissions_dict)

        command = input()
    print_func(data_dict, language_submissions_dict)


exams()
