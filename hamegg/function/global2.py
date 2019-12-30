var1 = "global"

def myfunc():
    global var1
    var1 = "new value"
    print("myfunc var1 = {0}".format(var1))
    
myfunc()
