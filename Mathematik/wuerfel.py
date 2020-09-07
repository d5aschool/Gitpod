from typing import Callable

"""
This function returns all possible cube combinations for the given sides and number of throws
"""
def iterate(dice_pages: list, num_throws: int, values: list = [], possible = []):
    for page in dice_pages:
        tmp: list = values[:]
        tmp.append(page)
        
        if len(tmp) < num_throws:
            iterate(dice_pages, num_throws, tmp)
        else:
            # for omega
            possible.append(tmp)

    return possible

"""
This function checks all results of iterate against the given check function.
Check should be a callable (anonymous) function.
"""
def do_check(num_throws: int, check: Callable[[list], bool]):
    dice_pages: list = [1, 2, 2, 3, 3, 3]
    result: list = []

    omega: list = iterate(dice_pages, num_throws)

    for o in omega:
        if callable(check) and check(o):
            result.append(o)

    pE = len(result) / len(omega)

    print(f"#würfe = {num_throws}")
    print(f"|Ω| = {len(omega)}")
    print(f"|E| = {len(result)}")
    print(f"P(E) = {pE} = {round(pE, 3)}%")

do_check(4, lambda arr: sum(arr) < 6)