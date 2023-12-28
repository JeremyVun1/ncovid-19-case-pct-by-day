def enforce_int(x):
    if x == None:
        return 0

    if type(x) is str:
        x = x.strip()
        return 0 if len(x) == 0 else int(x)
    else:
        return int(x)

def get_pct(cases, pop):
    if (pop):
        return float(cases) * 100 / float(pop)
    else:
        return pop