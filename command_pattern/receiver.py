class Receiver:

    def __init__(self, task):
        self.task = task

    def do_task(self):
        print("Receiver called. Executing", self.task)
