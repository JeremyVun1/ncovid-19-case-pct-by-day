import numpy as np
from datetime import datetime, timedelta

from lib.utility import enforce_int, get_pct

class Country:
    def __init__(self, name, pop, cases, date):
        self.country_name = name
        self.pop = enforce_int(pop)
        self.cases = []
        self.case_total = 0
        self.pct = []
        self.date = date

        self.add_cases(cases, date)

    def finalise(self, start_date, trim_start=True):
        # order daily case numbers chronologically from beginning -> end
        self.cases.reverse()

        # pad cases from the start_date to the current date
        while(start_date < self.date):
            self.cases.insert(0, 0)
            self.date = self.date - timedelta(days=1)

        # trim zero data at the start
        if trim_start:
            self.cases = np.trim_zeros(self.cases, 'f')

        self.build_case_pct_by_day()

        return self

    def build_case_pct_by_day(self):
        pct_total = 0
        for n in self.cases:
            pct_total = pct_total + get_pct(n, self.pop)
            self.pct.append(pct_total)

    def pad_missing_case_dates(self, date):
        d = date + timedelta(days=1)
        while (d < self.date):
            d = d + timedelta(days=1)
            self.cases.append(0)

    def add_cases(self, new_cases, date):
        self.pad_missing_case_dates(date)

        new_cases = enforce_int(new_cases)
        self.cases.append(new_cases)
        self.case_total = self.case_total + new_cases
        self.date = date


class Axis_range:
    def __init__(self, window=0, max_padding_pct=0):
        self.min = 0
        self.max = 0
        self.max_padding_pct = max_padding_pct
        self.window = window

    def get_max(self):
        return self.max * (1 + self.max_padding_pct)

    def get_min(self):
        return self.min
    
    def set_max(self, new_max):
        if new_max > self.max:
            self.max = new_max
            if self.window and (self.max - self.min) > self.window:
                self.min = self.max - self.window

    def set_min(self, new_min):
        if new_min < self.min:
            self.min = new_min
            if self.window and (self.max - self.min) > self.window:
                self.max = self.min + self.window