# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_send = False
#
#     def send(self):
#         self.is_send = True
#
#     def get_info(self):
#         return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}'
#
#
# emails = []
#
# while True:
#     command = input().split(' ')
#     if command[0] == 'Stop':
#         break
#     sender = command[0]
#     receiver = command[1]
#     content = command[2]
#     email = Email(sender, receiver, content)
#     emails.append(email)
#
# indexes = input().split(', ')
#
# for i in indexes:
#     emails[int(i)].send()
#
# for k in emails:
#     print(k.get_info())
# class Email:
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# emails = []
# command = input().split(' ')
#
# while command[0] != 'Stop':
#     sender = command[0]
#     receiver =command[1]
#     content = command[2]
#     email = Email(sender, receiver, content)
#     emails.append(email)
#     command = input().split(' ')
# indexes = input().split(', ')
#
# for i in indexes:
#     emails[int(i)].send()
#
# for k in emails:
#     print(k.get_info())
class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"



emails = []
command = input()
while command != "Stop":
    command = command.split(' ')
    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()
index = list(map(int, input().split(", ")))
send_email = [emails[i].send() for i in index]

for i in emails:
    print(i.get_info())
