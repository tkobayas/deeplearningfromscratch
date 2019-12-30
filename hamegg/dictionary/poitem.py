dict = {"John":3000, "Paul":2800, "George":2500, "Ringo":2000}

del dict["Ringo"]

print (dict)

dict = {"John":3000, "Paul":2800, "George":2500, "Ringo":2000}


val = dict.pop("Paul")

print (val)

print (dict)

print ("-----------")

dict = {"John":3000, "Paul":2800, "George":2500, "Ringo":2000}

while dict:
    tpl = dict.popitem()
    print (tpl)
    

print ("-----------")

dict = {"John":3000, "Paul":2800, "George":2500, "Ringo":2000}

dict.clear()

print (dict)