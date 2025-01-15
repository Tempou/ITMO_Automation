a: int=5
b: str='строка'
c: list=[1,2]

def indent(s: str,width: int) -> int:
    return '' * (max(0, width - len(s))) + s

print(indent('13', 5))


def func(s:str='') -> int:
    return len(s)

def min_list(a:list, b:list) -> int:
    return max(len(a), len(b))