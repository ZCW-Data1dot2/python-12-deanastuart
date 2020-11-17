from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """

    Return an even or odd of list in range of start and stop depending on the parity.
    :param start:
    :param stop:
    :param parity:
    :return:
    """
    if parity == Parity.ODD:
        x = [i for i in range(start,stop) if i % 2 != 0]
    elif parity == Parity.EVEN:
        x = [i for i in range(start,stop) if i % 2 == 0]
    return x

def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    For range of start to stop create a dictionary of integer keys of the range and values of the strategy on the value of the range

    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    dict = {i: strategy(i) for i in range(start,stop)}
    return dict

def gen_set(val_in: str) -> Set:
    """
    return a set of capital letters of the lowercase letters in a string from end of the string to the front
    :param val_in:
    :return:
    """
    x = set()
    str1 = str(val_in)
    [x.add(i.capitalize()) for i in str1 if i.islower() is True]
    return x

    #version not as list comprehension...
    # for i in str1:
    #     if i.islower() is True:
    #         x.add(i.capitalize())
