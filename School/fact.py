import pipes
import functools
def get_int(msg=''):
    return int(input(msg))

def main():
    def factorial(n):
        return n, functools.reduce(lambda x, y: x * y, range(1, n + 1))

    def indata():
        def validate(n):
            if not isinstance(n,int):
                raise TypeError("ЧИСЛО ДОЛЖНО БЫТЬ ЦЕЛЫМ")
            if not n>=0:
                raise ValueError("ЧИСЛО МЕНЬШЕ НУЛЯ ")
            return n
        msg="Ведите неотрицательное целое число"
        return pipes.pipe(get_int(),validate())
