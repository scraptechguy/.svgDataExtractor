def main():  

    # lists holding values of x and y coordinates, in pixels 

    pixels_x = []
    pixels_y = [] 

    
    # l is a list of lines and i is used to tell whether current line is a line with wanted data (0 -> it's not, 1 -> it is)  
    
    l = []
    i = 0

    
    # f represents the .svg file, don't forget to specify your own path! :)

    f = open("<.svg file path>", "r")

    
    # for loop that goes over every line in code, deletes unwanted "C" at the beginning & '"' at the end, and stores line's values in lists 
    # (x to pixels_x, y to pixels_y)
    
    for line in f.readlines():

        
        # l represents one line, as the loop goes, every line becomes l for one cycle
        
        l = line.split()


        # if that skips line when it's empty 
        
        if len(l) == 0:
            continue 


        # if that looks for unwanted "C". If found, value of i is changed to one -> if with i == 0 is no longer true -> 
        # -> whole loop is executed and data extraction begins
        
        if l[0] == "C":
            i = 1
            l = l[1:]

            
        # if unwanted "C" (the beginning of data) hasn't been found yet, the loop checks the next line without doing anything

        if i == 0:
            continue

            
        # if that looks for "/>" (the end of data) and removes it together with '"' when found. The value of i is changed back to 0 
        # to skip whatever follows after the data

        if l[-1] == "/>":
            i = 0
            l = l[:-1]
            l[-1] = l[-1][:-1]


        # the data is further split into x and y values, that are then appended to lists pixels_x and pixels_y
        # j represents index in l list 
            
        for j in range(0, len(l)):
            x, y = l[j].split(",") 

            pixels_x.append(x)
            pixels_y.append(y)

    
    # f (the .svg file) gets closed as we don't need it anymore 
    
    f.close()

    
    # e represents .txt file where the extracted data will be written, don't forget to specify your own path!
    
    e = open("<.txt file path where pixels' x and y coordinates will be extracted>", "w")
    
    
    # the text in the brackets get's displayed at the beginning of the .txt file, to help users understand its contents
    
    e.write("# x, y in pixels")

    
    # for loops that writes every pair of coordinates with the same index next to each other in the .txt file
    # j is the number of coordinates that will be written to the .txt file
    
    for j in range(0, len(pixels_x)):
        e.write("%s %s\n" % (pixels_x[j], pixels_y[j]))

    
    # as we no longer need e, it gets closed
    
    e.close()


# this little trick makes an accessible library from code above and executes main() 
# (code will work even when line n. 99 gets removed and line n. 100 unintended, dw)
    
if __name__ == '__main__':
    main()
