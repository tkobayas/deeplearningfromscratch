dict_input = {"data":"AAA"}

try:
    f = open("./non-existingFile.txt", 'r')
    data = dict_input['data']
    f.write(data)
    f.close()
except KeyError:
    print ("KeyError!")
except (IOError, TypeError) as e:
    print ("cannot open file")
    print("type(e):{0}".format(type(e)))
    print("e.args:{0}".format(e.args))
    print("e:{0}".format(e))
except Exception as e:
    print ("other errors")
    print("type(e):{0}".format(type(e)))
    print("e.args:{0}".format(e.args))
    print("e:{0}".format(e))