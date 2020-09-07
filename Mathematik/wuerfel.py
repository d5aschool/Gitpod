from typing import Callable

def iterate(seiten: list, anzahl: int, values: list = [], possible = []):
    for seite in seiten:
        tmp: list = values[:]
        tmp.append(seite)
        
        if len(tmp) < anzahl:
            iterate(seiten, anzahl, tmp)
        else:
            # for omega
            possible.append(tmp)

    return possible

def do_check(wuerfe: int, check: Callable[[list], bool]):
    seiten: list = [1, 2, 2, 3, 3, 3]
    ergebnis: list = []

    omega: list = iterate(seiten, wuerfe)

    for o in omega:
        if callable(check) and check(o):
            ergebnis.append(o)
        #if sum(o) <= 6:
        #    ergebnis.append(o)

    pE = len(ergebnis) / len(omega)

    print(f"#würfe = {wuerfe}")
    print(f"|Ω| = {len(omega)}")
    print(f"|E| = {len(ergebnis)}")
    print(f"P(E) = {pE} = {round(pE, 3)}%")

do_check(4, lambda arr: sum(arr) < 6)