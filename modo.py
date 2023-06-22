'''
MODO
'''

# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=consider-using-enumerate
# pylint: disable=global-statement

DEBUG = False

def change_mode():
    global DEBUG

    DEBUG = not DEBUG

def get_mode():
    return DEBUG
