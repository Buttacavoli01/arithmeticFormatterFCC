import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num_balls_drawn):
        if int(num_balls_drawn) > len(self.contents):
            picked = []
            for i in range(num_balls_drawn):
                picked.append(random.choice(self.contents))
            return picked
        else:
            return self.contents



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    picks = []
    # print(hat.contents)
    counter = 0
    yes = 0
    no = 0

    for k, v in expected_balls.items():
        for i in range(v):
            picks.append(k.lower())

    M = 0
    content_copy = copy.deepcopy(hat.contents)
    for i in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        hat.contents = copy.deepcopy(content_copy)
        count = 0
        for i in picks:
            for j in drawn:
                if i == j:
                    count += 1
                    drawn.pop(drawn.index(j))
                    break
            if count == len(picks):
                M += 1
    return M / num_experiments