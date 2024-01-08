from exceptions import MustContainedAtSymbolError, NameTooShortError, InvalidDomainError
allowed_domains = 'com, bg, org, net'
while True:
    email =[x for x in input().split('@')]


    if email[0] == "End":
        break
    if len(email) != 2:
        raise MustContainedAtSymbolError("Email must contain @")
    name = email[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    domain = email[1].split('.')[-1]
    if domain not in allowed_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print('Email is valid')