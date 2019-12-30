try:
    a = 10 / 0
    print("{0}".format(a))
except ZeroDivisionError as e:
    print ("ZeroDivisionError!!")
    print("type(e):{0}".format(type(e)))
    print("e.args:{0}".format(e.args))
    print("e:{0}".format(e))
finally:
    print ("do something last")