def flights(*args):
    flight_dict = {}
    for data in range(0, len(args), 2):

        if args[data] == 'Finish':
            break
        if args[data] not in flight_dict:
            flight_dict[args[data]] =  args[data+1]
        else:
            flight_dict[args[data]] += args[data+1]
    return flight_dict
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))