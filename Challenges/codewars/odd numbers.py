def find_outlier(integers: list):
    odd = [n for n in integers if n % 2 != 0]
    only_odd = odd[0] if len(odd) == 1 else None
    odd2 = [n for n in integers if n % 2 == 0]
    only_odd2 = odd2[0] if len(odd2) == 1 else None
    return only_odd or only_odd2
