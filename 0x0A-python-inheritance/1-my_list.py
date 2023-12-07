#!/usr/bin/python3
''' Module that defines a class that print sroted list
'''


class MyList(list):
    ''' class modelizing MyList
    '''

    def print_sorted(self):
        '''
        prints the list in a sorted manner
        '''
        print(sorted(self))
