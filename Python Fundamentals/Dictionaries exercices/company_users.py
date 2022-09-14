def print_func(company_data_dict):
    for key in company_data_dict.keys():
        number = len(company_data_dict[key])
        print(f'{key}')
        for i in range(number):
            print(f'-- {company_data_dict[key][i]}')

def company_users():
    company_data_dict = dict()
    command = input().split(' -> ')
    while command[0] != 'End':
        company_name = command[0]
        id = command[1]
        if company_name not in company_data_dict:
            company_data_dict[company_name] = []
        if id not in company_data_dict[company_name]:
            company_data_dict[company_name].append(id)

        command = input().split(' -> ')
    print_func(company_data_dict)
company_users()