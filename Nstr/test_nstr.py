import nstr

if __name__=="__main__":
    alpa = nstr.NStr()
    print(alpa.new_str())
    print(alpa.new_str_std(5))
    print(alpa.new_str_stdr())
    print()

    print(alpa.new_str_with_basic(10))
    print(alpa.new_str_with_value(50))
    print(alpa.new_str_random(5, 30))
    print(alpa.new_str_rst(21, 10, "Programming_"))
    print(alpa.new_str_rst(9, 10, "Programming_"))
    print()

    print(alpa.get_new_str_sorted(alpa.new_str()))
    print()

    # new function
    print("#######################################")
    print(alpa.new_str_with_date())
    print(alpa.new_str_date(0)) # day
    print(alpa.new_str_date(1)) # month
    print(alpa.new_str_date(2)) # year
    day = alpa.new_str_date(0)
    month = alpa.new_str_date(1)
    year = alpa.new_str_date(2)
    dates = "{}-{}-{}".format(day, month, year)
    print(dates)
    print()


    print("######################################")
    print(alpa.new_str_with_time())
    print(alpa.new_str_time(0)) # hour
    print(alpa.new_str_time(1)) # minute
    print(alpa.new_str_time(2)) # second
    hour = alpa.new_str_time(0)
    minute = alpa.new_str_time(1)
    second = alpa.new_str_time(2)
    timer = "{} hour : {} minute : {} second".format(hour, minute, second)
    print(timer)