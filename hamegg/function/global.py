var1 = "global"

def myfunc():
    var2 = "local"
    print("myfunc var1 = {0}".format(var1))
    print("myfunc var2 = {0}".format(var2))
    
myfunc()
print("var1 = {0}".format(var1))
print("var2 = {0}".format(var2))
