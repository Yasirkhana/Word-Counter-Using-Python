#                              WORD COUNTER WITH PYTHON
def counter(filename):                                      # Couter Function
    with open(f"{filename}","r") as f:                      # Opening File to read
        data = f.read()
        new = data.split()                                  # spliting each word and saving in a list
        #print(new)
        print(f" Total Words in File are : {len(new)}")     #Printing the length of list (i.e total words)

counter("bigdata.txt")                                      # Calling function 