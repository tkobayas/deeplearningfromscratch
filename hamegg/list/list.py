mylist = ["John", "Lennon", 34]

print ("Name = " + mylist[0] + " " + mylist[1])
print ("Age = " + str(mylist[2]))

print ("len = " + str(len(mylist)))

mylist.append("Guitar")

print ("Instrument = " + mylist[3])

list2 = ["A", "B"]

mylist.extend(list2)

print (mylist[5])

list3 = [1, 4, 9]

newlist = mylist + list3

print (newlist)

newlist2 = mylist * 3

print (newlist2)
