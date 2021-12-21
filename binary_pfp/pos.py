import random

def create_pos_lists():
    list1 = [random.randint(0, 1) for _ in range(4)]
    list2 = [random.randint(0, 1) for _ in range(4)]
    list3 = [random.randint(0, 1) for _ in range(4)]
    list4 = [random.randint(0, 1) for _ in range(4)]
    list5 = [random.randint(0, 1) for _ in range(4)]
    list6 = [random.randint(0, 1) for _ in range(4)]
    list7 = [random.randint(0, 1) for _ in range(4)]
    list8 = [random.randint(0, 1) for _ in range(4)]

    return [
        list1 + list(reversed(list1.copy())),
        list2 + list(reversed(list2.copy())),
        list3 + list(reversed(list3.copy())),
        list4 + list(reversed(list4.copy())),
        list5 + list(reversed(list5.copy())),
        list6 + list(reversed(list6.copy())),
        list7 + list(reversed(list7.copy())),
        list8 + list(reversed(list8.copy()))
    ]