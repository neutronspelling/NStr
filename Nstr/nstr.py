# versi 1.26.11
from string import ascii_lowercase, ascii_uppercase
from random import randint
from datetime import datetime

class NStr:
    def __init__(self):
        self.nstr = ""
        self.dt = datetime.now()

    def cap_random(self, alpa: str, cap: str) -> str:
        # null = ""
        lower_to_upper = {kl: jl for kl, jl in zip(ascii_lowercase, ascii_uppercase)}
        for i in alpa:
            if i == cap:
                i = lower_to_upper.get(cap)
            self.nstr += i
        return self.nstr

    @classmethod
    def get_new_str_sorted(self, val: str, reverse=False) -> str:
        return "".join(sorted(val, reverse=reverse))
    
    def new_str(self) -> str:
        for _ in range(5):
            self.nstr += str(randint(0, 100))
        return self.nstr
    
    @classmethod
    def new_str_std(self, val : str) -> str:
        rstr = str(val)
        for _ in range(5):
            rstr += str(randint(0, 100))
        return rstr

    @classmethod
    def new_str_stdr(self, val="") -> str:
        for _ in range(5):
            val += str(randint(0, 100))
        return val

    def new_str_with_basic(self, basic: int) -> str:
        if basic <= 20:
            for _ in range(basic):
                self.nstr += str(randint(0, 100))
            return self.nstr
        return None

    def new_str_with_value(self, value: int) -> str:
        if value <= 100:
            for _ in range(5):
                self.nstr += str(randint(0, value))
            return self.nstr
        return None

    def new_str_random(self, basic: int, value: int) -> str:
        if basic <= 20 and value <= 100: 
            for _ in range(basic):
                self.nstr += str(randint(0, value))
            return self.nstr
        return None

    def new_str_rst(self, basic: int, value: int, rst: str) -> str:
        var = str(rst)
        if basic <= 20 and value <= 100: 
            for _ in range(basic):
                var += str(randint(0, value))
            return var
        return None

    # str time and date
    def new_str_with_date(self) -> str:
        return "{}_{}_{}".format(self.dt.day, self.dt.month, self.dt.year)

    def new_str_date(self, n: int) -> str:
        if n == 0:
            return "{}".format(self.dt.day)
        elif n == 1:
            return "{}".format(self.dt.month)
        elif n == 2:
            return "{}".format(self.dt.year)
        else:
            return None
            
    def new_str_with_time(self) -> str:
        return "{}_{}_{}".format(self.dt.hour, self.dt.minute, self.dt.second)

    def new_str_time(self, n: int) -> str:
        if n == 0:
            return "{}".format(self.dt.hour)
        elif n == 1:
            return "{}".format(self.dt.minute)
        elif n == 2:
            return "{}".format(self.dt.second)
        else:
            return None

if __name__=="__main__":
    from doctest import testmod
    testmod()