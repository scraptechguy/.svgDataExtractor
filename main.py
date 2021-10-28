def main():  

    # lists holding values of x and y coordinates, in pixels 

    pixels_x = []
    pixels_y = [] 

    l = []
    i = 0

    
    # opens your .svg file

    f = open("<.svg file path>", "r")

    
    # for loop that goes over every line in code, deletes unwanted "C" at the beginning & '"' at the end, and stores line's values in lists 
    # (x to pixels_x, y to pixels_y)
    
    for line in f.readlines():

        l = line.split()


        if len(l) == 0:
            continue 


        if l[0] == "C":
            i = 1
            l = l[1:]


        if i == 0:
            continue


        if l[-1] == "/>":
            i = 0
            l = l[:-1]
            l[-1] = l[-1][:-1]


        for j in range(0, len(l)):
            x, y = l[j].split(",") 

            pixels_x.append(x)
            pixels_y.append(y)

            
    f.close()

    e = open("<.txt file path where pixels' x and y coordinates will be extracted>", "w")
    e.write("# x, y in pixels")

    for j in range(0, len(pixels_x)):
        e.write("%s %s\n" % (pixels_x[j], pixels_y[j]))

        
    e.close()


if __name__ == '__main__':
    main()
