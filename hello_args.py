"""Say Hi"""
import sys
def say_hi(name):
    return f'\nHello, {name}!\n'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = 'MUSA 509'
    print(say_hi(name))
