# versi 1.0 from order.py
from random import randint

class NStr:
    def __init__(self) -> str:
        self.nstr = ""

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
        if basic <= 20 or value <= 100: 
            for _ in range(basic):
                self.nstr += str(randint(0, value))
            return self.nstr
        return None

    def new_str_rst(self, basic: int, value: int, rst: str) -> str:
        var = str(rst)
        if basic <= 20 or value <= 100: 
            for _ in range(basic):
                var += str(randint(0, value))
            return var
        return None

# if __name__=="__main__":
#     alpa = NStr()
#     print(alpa.new_str())
#     print(alpa.new_str_std(5))
#     print(alpa.new_str_stdr())

#     print(alpa.new_str_with_basic(10))
#     print(alpa.new_str_with_value(50))
#     print(alpa.new_str_random(5, 30))
#     print(alpa.new_str_rst(4, 10, "Programming_"))

#     print(alpa.get_new_str_sorted(alpa.new_str()))

