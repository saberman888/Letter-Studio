# The MIT License (MIT)
#
# Copyright (c) 2015 saberman888

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#Main function
import os
from core.language import *
from core.config import *
from core.cio import *
from core.ctools import *
from core.conassets import *
REALPATH = os.path.realpath(__file__)[:len(os.path.realpath(__file__))-len(__file__)]
#Realpath is a nice var
DIRECTORIES = {
	'LANG':REALPATH+"/core/lang",
	'DATA':REALPATH+"/core/data"
}

def main():
	#Check if language and data folders exist
	if os.path.isdir(REALPATH) == False:
		print "Error! Failed to establish REALPATH."
		getchar()
		os._exit()
	elif os.path.isdir(DIRECTORIES['LANG']) == False:
		print "Error! /core/lang/ doesn't exist!"
		getchar()
		os._exit()
	elif os.path.isdir(DIRECTORIES['DATA']) == False:
		print "Error! /core/data doesn't exist!"
		getchar()
		os._exit()
	
	GetConfiguration(REALPATH) #Load configuration of the program
	print PerminantCFG['NAME']
	print "Created by: ",PerminantCFG['AUTHOR']
	print "Version: ",PerminantCFG['Version']
	print "License: ",PerminantCFG['License']
	load_language(Configuration['langdir'])
	
	
main()

