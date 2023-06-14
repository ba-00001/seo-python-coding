#!/usr/bin/python3
def is_same_class(obj, a_class):
    return type(obj) is a_class


a = 1
if is_same_class(a, int):
    answer = "{} is an instance of the class {}".format(a, int.__name__)
    print(answer)
if is_same_class(a, float):
    answer2 = "{} is an instance of the class {}".format(a, float.__name__)
    print(answer2)
if is_same_class(a, object):
    answer3 = "{} is an instance of the class {}".format(a, object.__name__)
    print(answer3)
