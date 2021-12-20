import random

def create_pos_lists():
    list1 = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    list2 = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    list3 = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    list4 = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    list5 = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    list6 = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    list7 = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
    list8 = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]

    list1_rev = list(reversed(list1.copy()))
    list2_rev = list(reversed(list2.copy()))
    list3_rev = list(reversed(list3.copy()))
    list4_rev = list(reversed(list4.copy()))
    list5_rev = list(reversed(list4.copy()))
    list6_rev = list(reversed(list4.copy()))
    list7_rev = list(reversed(list4.copy()))
    list8_rev = list(reversed(list4.copy()))

    return [list1 + list1_rev, list2 + list2_rev, list3 + list3_rev, list4 + list4_rev, list5 + list5_rev, list6 + list6_rev, list7 + list7_rev, list8 + list8_rev]