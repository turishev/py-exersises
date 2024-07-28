#!/usr/bin/python

global_var = 123

def print_sum(x):
    print("sum: " + str(global_var + x))


def set_glob_var(x):
    global global_var
    global_var = x
    print(global_var + 1000)


def var_args_test(x, *args):
    print(x)
    print(args)
    print(args[0])
    print(args[1])

def key_args_test(x, **kwargs):
    print(x)
    print(kwargs)
    print(kwargs['a'])
    print(kwargs['b'])


def main():
    print("main")
    print_sum(3)
    set_glob_var(5)
    print_sum(3)
    var_args_test(111, 222, 33)


main()

