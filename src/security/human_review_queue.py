class HumanReviewQueue:

    def __init__(self):

        self.queue = []

    def add(self, item):

        self.queue.append(item)

    def get_all(self):

        return self.queue
