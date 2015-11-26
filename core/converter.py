#The MIT License (MIT)
#
#Copyright (c) 2015 saberman888

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import cio
import os.path
import sys
import conassets
import zipfile

__version__ = 1.0.0
__author__ = "Andres Vazquez"
#Conworkshop .CSV converter to QuickLang format!
#By Sai22/saberman888
#Version 1.0.0

def MainMenu():
    print "1.Start convert"
    print "2.Requirements"
    print "3.Exit"
    I = raw_input()

    if I == 1:
        print "Specify file path to .csv"
        path = raw_input()
	enc = raw_input("Specify Encapsulation:")
	delim = raw_input("Specify Delimeter:")
        if os.path.isfile(path) == True:
            convert(path, enc, delim)
        else:
	    print "Invalid path!"
	    return MainMenu()

    elif  I == 2:
	print "Requirements:\n"
	print "1.Make sure you have "Include header?" enabled to yes"
	print "2.Make sure its in .csv format and not .rtf format"

    elif I == 3:
	sys.exit()


def convert(Path, Encapsulation, Delimeter):
    fields = {}
    words  = []
    classes_ = []
    syntax = 0
    
    os.system('cls" if os.name == 'nt' else 'clear')
    p = open(Path, "r")
    plines = p.readlines()

    print "Reading header..."
    header = plines[0]
    print header
    header.split(Delimeter)
    header.split(Encapsulation)
    for x in header:
	if x == 'ipa' or x == 'x-sampa' or x == 'image link':
	    pass
	else:
	    fields = {x:fields.index(x)}
	    syntax+=1

    
    current_line = 1
    while(current_line<=(len(plines)-1)):
	cline = plines[current_line]
	print "Converting at %s" str(cline)
	cline.split(Delimeter)
	cline.split(Encapsulation)
	for word in cline:
	    if cline.index(word) == 1:
		
	    elif cline.index(word) == 2:
	    elif cline.index(word) == 3:
	    elif cline.index(word) == 4:
	    elif cline.index(word) == 5:
	    elif cline.index(word) == 6:
	    elif cline.index(word) == 7:
	    elif cline.index(word) == 8:
	    elif cline.index(word) == 9:
	    elif cline.index(word) == 10:
	    elif cline.index(word) == 11:

		
    	    

    
    

    
