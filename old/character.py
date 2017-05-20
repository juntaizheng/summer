import dice

class Character:
    def __init__(self, stats, race):
        self.stats = stats
        self.race = race
        self.job = None

class Job(Character):
    def __init__(self, job):
        self.job
