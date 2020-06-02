#!/usr/bin/python3
'''print_sorted file'''


class MyList(list):
    '''MyList class'''
    def print_sorted(self):
        '''public instance method'''
        print(sorted(self))
