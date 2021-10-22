#!/usr/bin/python3
'''class that rejects __dict__ and uses the slots instead'''


class LockedClass:
    '''this is what defines a locked class'''

    __slots__ = "first_name"
