dict = {"John":3000, "Paul":2800}

print (dict)

value = dict["Paul"]

print (value)

dict["Paul"] = 2900

print (dict)

print ("len(dict) = " + str(len(dict)))

dict2 = {"George":2500, "Ringo":2000}

dict.update(dict2)

print (dict)

