# .svg Data Extractor

+ To run this yourself, review <a href="https://github.com/scraptechguy/.svgDataExtractor/blob/main/requirements.md" target="_blank">requirements.md</a> file and do the following in terminal: 

```zh
cd <path of the project on your computer>
```

```zh
python main.py
```

+ Note: requirements.txt do NOT need to be run as no libraries are required. If you do, following error will occur...

```zh
ERROR: You must give at least one requirement to install (see "pip help install")
```

## How it works?

Programmed for extracting raw data (<a href="https://en.wikipedia.org/wiki/Text_file" target="_blank">.txt</a>) from <a href="https://en.wikipedia.org/wiki/Scalable_Vector_Graphics" target="_blank">.svg</a> files with a common pattern. 

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

Program is written in Python 3.10
