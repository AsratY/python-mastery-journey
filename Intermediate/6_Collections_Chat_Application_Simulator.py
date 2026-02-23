# Advanced Combined Challenge (Highly Recommended)
# Build a Chat Application Simulator
# Use:
# deque → Store last 10 messages
# Counter → Count most active users
# defaultdict → Group messages by user
# namedtuple → Message structure (user, timestamp, text)
# OrderedDict → Maintain users in order of last activity
# Requirements:
# 1. Store messages.
# 2. Keep only last 10 messages.
# 3. Display top 3 most active users.
# 4. Show chat history of specific user.
# 5. Track users by recent activity.

from collections import Counter, deque, defaultdict, namedtuple, OrderedDict
from datetime import datetime


class Chat_App():
    def __init__(self):
        self.size = 10
        self.message = deque(maxlen=self.size)
        self.user = defaultdict(list)
        Message = namedtuple('Message', 'user,timestamp,text')
        self.message_tuple = Message
        self.activity = OrderedDict()

    def send(self, user, text):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        msg = self.message_tuple(user, time, text)
        self.message.appendleft(msg)
        self.user[user].append(msg)
        if user in self.activity:
            self.activity.update({user: time})
            self.activity.move_to_end(user)
        else:
            self.activity.update({user: time})

    def frequent_three(self):
        if self.user:
            active_count = Counter({key: len(value)
                                   for key, value in self.user.items()})
            top_three = active_count.most_common(3)
            print(f"**********   Top three most active users  **********")
            for key, value in top_three:
                print(f"{key} : {value}")

    def history(self, user=''):
        if user in self.user:
            print(f"**********   {user}'s Chat History    *********")
            for msg in self.user[user]:
                print(f"{msg.user} : {msg.timestamp} : {msg.text}")
        else:
            print("*********   Chat History    *********")
            for key, value in self.user.items():
                for msg in value:
                    print(f"{key} : {msg.timestamp} : {msg.text}")

    def recent_users(self):
        if self.activity:
            print("*********    Users By Recent Activity    **********")
            for i, user in enumerate(reversed(self.activity), start=1):
                if i == 1:
                    print(f"{i}. {user} (most recent)")
                elif i == len(self.activity):
                    print(f"{i}. {user} (least recent)")
                else:
                    print(f"{i}. {user}")


message = Chat_App()
message.send("David", "Hi! How are you doing?")
message.send("Peter", "I am fine. and you?")
message.send("David", "Doing good!")
message.send("Peter", "where are the others?")
message.send(
    "David", "They are comming. By the way I saw your brother at the police station today. Is everything good?")
message.send("Anna", "How are you guys doing?")
message.send(
    "David", "we are doing good but I don\'t know about peter\'s brother.")
message.send("Salem", "What happened to peter\'s brother?")
message.send("Anna", "David saw him at the police station.")
message.frequent_three()
message.history("David")
message.history()
message.send("David", "Peter are you there?")
message.send("Peter", "Yup I am here.")
message.send(
    "Peter", "Everything is fine! He was visting the police station for research purposes.")
message.frequent_three()
message.history("David")
message.history()
message.recent_users()
