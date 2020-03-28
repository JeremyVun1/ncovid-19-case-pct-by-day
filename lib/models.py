import numpy as np

def enforce_int(x):
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

class Country:
    def __init__(self, name, pop, cases):
        self.country_name = name
        self.pop = enforce_int(pop)
        self.cases = []
        self.case_total = 0
        self.pct = []

        self.add_cases(enforce_int(cases))

    def finalise(self):
        self.cases.reverse()
        self.cases = np.trim_zeros(self.cases, 'f')
        self.build_case_pct_by_day()
        return self

    def build_case_pct_by_day(self):
        pct_total = 0
        for n in self.cases:
            pct_total = pct_total + get_pct(n, self.pop)
            self.pct.append(pct_total)

    def add_cases(self, new_cases):
        new_cases = enforce_int(new_cases)
        self.cases.append(new_cases)
        self.case_total = self.case_total + new_cases