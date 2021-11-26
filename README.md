# Simple and fast way to extract raw data (.txt) from .svg files

Programmed for extracting raw data (<a href="https://en.wikipedia.org/wiki/Text_file" target="_blank">.txt files</a>) from <a href="https://en.wikipedia.org/wiki/Scalable_Vector_Graphics" target="_blank">.svg</a> files with a common pattern. <b>This project contains <a href="https://github.com/scraptechguy/.svgDataExtractor/blob/main/sample.svg" targer="_blank">sample.svg file</a> and blank <a href="https://github.com/scraptechguy/.svgDataExtractor/blob/main/sample.txt" target="_blank">sample.txt file</a> to make it easier for you to try it!</b>

+ To run this yourself, review <a href="https://github.com/scraptechguy/.svgDataExtractor/blob/main/requirements.md" target="_blank">requirements.md</a> file and do the following in terminal: 

```sh
cd <path of the project on your computer>
```

```sh
python main.py
```

+ Note: requirements.txt do NOT need to be run as no libraries are required. If you do, following error will occur...

```sh
ERROR: You must give at least one requirement to install (see "pip help install")
``` 

### Table of contents

+ <a href="https://github.com/scraptechguy/.svgDataExtractor#understand-the-output">Understand the output</a>
+ <a href=""></a>
+ <a href=""></a>

## Understand the output

Output is pixels' x and y coordinates in this format: 

```zh
    x, y in pixels 

    1240, 1099

    2975, 2834

    ...
```

+ Note: The data HAVE TO begin with "C" and end with "/>" while having unwanted ' " ' at the end for this to work as intended 

## Understand the code 

The program is written in Python 3.10

### Code structure with snippets of code 

+ The program opens your .svg file 

```py
def main():

    f = open("sample.svg", "r")
```

+ For loop that goes over every line in your .svg file and does all the magic 

```py
    for line in f.readlines():
```

+ l represents a line in the cycle, if its length is 0, program skips the line and move onto the next one 

```py
        l = line.split()
    
        if len(l) == 0:
            continue 
```

+ The data we want start with "C", only after the "C" is found, program starts storing the data to lists

```py
        if l[0] == "C":
            i = 1
            l = l[1:]
            
        if i == 0:
            continue
```

+ Some unwanted elements ("/>" and '"') are present near the data we want, this removes them!

```py 
        if l[-1] == "/>":
            i = 0
            l = l[:-1]
            l[-1] = l[-1][:-1]
```

+ Now "uninterupted" data is further split into x and y values, those are then appended to lists 

```py
        for j in range(0, len(l)):
            x, y = l[j].split(",") 

            pixels_x.append(x)
            pixels_y.append(y)
```

+ The program opens .txt file as e where the extracted data will be stored and writes info about the contents of the file  

```py
    e = open("sample.txt", "w")
    e.write("# x, y in pixels")
```

+ x and y values are then written into the text file in the format seen above

```py
    for j in range(0, len(pixels_x)):
        e.write("%s %s\n" % (pixels_x[j], pixels_y[j]))
```
