def length():
    remainder = len(string) % rail
    if remainder == 0:
        rail1range = (len(string) // rail)
        rail2range = (len(string) // rail)
        rail3range = (len(string) // rail)
    if remainder == 1:
        rail1range = (len(string) // rail) + 1
        rail2range = (len(string) // rail)
        rail3range = (len(string) // rail)
    if remainder == 2:
        rail1range = (len(string) // rail) + 1
        rail2range = (len(string) // rail) + 1
        rail3range = (len(string) // rail)
    global rail1range
    global rail2range
    global rail3range

def encrupt():
    # Rail 1
    rail1count = -1 * rail
    for i in range(rail1range):
        rail1count += rail
        print(string[rail1count], end = "")
        
    # Rail 2
    rail2count = -1 * rail + 1
    for i in range(rail2range): 
        rail2count += rail
        print(string[rail2count], end = "")
    
    # Rail 3
    if rail == 3:
        rail3count = -1 * rail + 2
        for i in range(len(string) // rail):
            rail3count += rail
            print(string[rail3count], end = "")
    print()

            
def decrupt():
    repeat = 0
    count1 = 1
    count2 = rail1range + 1
    count3 = rail1range + rail2range + 1
    
    while repeat != len(string) + 500:
        repeat += 1
        
        # Rail 1
        if count1 != rail1range + 1:
            for i in range(count1 - 1, count1):
                count1 += 1
                rail1 = string[i]
                print(rail1, end = "")
        
        # Rail 2
        if count2 != rail1range + rail2range + 1:
            for i in range(count2 - 1, count2):
                count2 += 1
                rail2 = string[i]
                print(rail2, end = "")
        
        # Rail 3
        if rail == 3:
            if count3 != rail1range + rail2range + rail3range + 1:
                for i in range(count3 - 1, count3):
                    count3 += 1
                    rail3 = string[i]
                    print(rail3, end = "")
    print()
#-----------------------------------------------
while True:
    # get string from user
    string = str(input())
    string = string.strip()
    
    # if no input, end the program
    if string == "":
        break
    
    # decrupt    
    if string[0] == "D" or string[0] == "d":
        
        if string[-1] != '2' and string[-1] != '3' and string[-1] != '"':
            print ("invalid number of rails")
            
        elif string[-1] == '2' or string[-1] == '"':
            rail = 2
            string = string.strip()
            string = string.split('"')[1]
            length()
            decrupt()                
        
        elif string[-1] == '3':
            rail = 3
            string = string.strip()
            string = string.split('"')[1]
            length()
            decrupt()        
    
    # encrupt
    elif string[0] == "E" or string[0] == "e":
        
        if string[-1] != '2' and string[-1] != '3' and string[-1] != '"':
            print ("invalid number of rails")
            
        elif string[-1] == '2' or string[-1] == '"':
            rail = 2
            string = string.strip()
            string = string.split('"')[1]
            length()
            encrupt()        
        
        elif string[-1] == '3':
            rail = 3
            string = string.strip()
            string = string.split('"')[1]
            length()
            encrupt()        
            
    else:
        print("invalid encryption command")