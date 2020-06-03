#!/usr/bin/python3
'''MyInt class from int class'''


class MyInt(int):
    '''MyInt class'''
    def __eq__(self, other):
        '''MyInt equal equivalent'''
        return super().__ne__(other)

    def __ne__(self, other):
        '''MyInt equal equivalent'''
        return super().__eq__(other)
