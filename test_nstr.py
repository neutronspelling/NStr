import nstr

if __name__=="__main__":
    alpa = nstr.NStr()
    print(alpa.new_str())
    print(alpa.new_str_std(5))
    print(alpa.new_str_stdr())

    print(alpa.new_str_with_basic(10))
    print(alpa.new_str_with_value(50))
    print(alpa.new_str_random(5, 30))
    print(alpa.new_str_rst(4, 10, "Programming_"))

    print(alpa.get_new_str_sorted(alpa.new_str()))