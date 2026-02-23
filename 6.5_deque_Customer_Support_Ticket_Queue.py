# 5️⃣ deque– Real-Time Processing System
# ️ Exercise: Customer Support Ticket Queue
# Simulate a ticket handling system.
# ️ Requirements:
# 1. Add tickets to the queue.
# 2. Process tickets (FIFO behavior).
# 3. Add VIP tickets to the front.
# 4. Limit queue size to 5:
# o If full, auto-remove oldest ticket.
# 5. Simulate undo operation using deque as a history stack.
# 6. Rotate queue to simulate shift change.
# ️ Real-world relevance:
# Task queues, messaging systems, streaming pipelines.

from collections import deque


ticket = deque()


class Ticket:

    def __init__(self, ticket):
        self.ticket = ticket
        self.size = 5
        self.track = deque()

    def add_tickets(self, name, status=False):
        if len(self.ticket) >= self.size:
            self.processed = self.ticket.popleft()
            self.track.append((self.processed, "auto_reduct"))
            print(f"{self.processed} your turn!")
        if status:
            self.ticket.appendleft(name)
            self.track.append((name, "vip_add"))
            print(f"{name} VIP added to front!")
        else:
            self.ticket.append(name)
            self.track.append((name, "normal_add"))
            print(f"{name} added to queue!")

    def process(self):
        processed = self.ticket.popleft()
        print(f"Precessing ... {processed}")
        self.track.append((processed, "process"))

    def rotate(self, rt_value):
        self.ticket.rotate(rt_value)
        print(self.ticket)
        self.track.append((rt_value, "rotate"))

    def undo(self):
        if self.track:
            if self.track[-1][1] == "vip_add":
                self.ticket.popleft()
                self.track.pop()
                if self.track and self.track[-1][1] == "auto_reduct":
                    self.ticket.appendleft(self.track[-1][0])
                    self.track.pop()
            elif self.track[-1][1] == "normal_add":
                self.ticket.pop()
                self.track.pop()
                if self.track and self.track[-1][1] == "auto_reduct":
                    self.ticket.appendleft(self.track[-1][0])
                    self.track.pop()
            elif self.track[-1][1] == "process":
                self.ticket.appendleft(self.track[-1][0])
                self.track.pop()
            elif self.track[-1][1] == "rotate":
                self.ticket.rotate(self.track[-1][0]*-1)
                self.track.pop()
        else:
            print("Nothing to Undo!")

        print(self.ticket)

    def display(self):
        print(self.ticket)
        # print(self.track)


tk = Ticket(ticket)

tk.undo()
tk.add_tickets("Don")
tk.undo()
tk.add_tickets("Joe")
tk.process()
# tk.display()
tk.add_tickets("Abel")
tk.add_tickets("Chris")
tk.add_tickets("Betty", True)
# tk.display()
tk.process()
tk.add_tickets("Anna")
# tk.undo()
tk.add_tickets("Caleb")
tk.add_tickets("Kiki")
tk.add_tickets("Duo")
tk.add_tickets("Davis", True)
tk.display()
tk.undo()
tk.undo()
tk.rotate(1)
tk.undo()
