import random

def create_pos_lists():
    return [
        (x:=[random.randint(0, 1) for _ in range(4)])+x[::-1] for _ in range(8)
    ]