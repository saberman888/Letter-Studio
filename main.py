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

#Import core files
from core.cio import *
from core.conassets import *
from core.ctools import *
from core.language import *
from core.config import *
import os, sys

REALPATH = os.path.realpath(__file__)[:len(os.path.realpath(__file__))-len(__file__)]
Setup = True
Update = False
directories = {
	'lang':REALPATH+'/data/lang',
	'data':REALPATH+'/data/'
}

#Import Gui stuff
try:
	import wx
except ImportError:
	with open("Error.txt", 'w') as e:
		e.write("Error! The wx module was not found!")
		e.close()
		os._exit()

from core.wx.alert import *
from core.wx.setup import *
from core.wx.mainwindow import *
A = wx.App()
if os.path.isfile(directories['data']+"config.cfg"):
	Setup = False
elif not os.path.isdir(directories['data']):
	mkdir(directories['data'])
	Setup = True
elif not os.path.isdir(directories['lang']):
	Warn("Warning!","/data/lang/ didn't exist, creating...")
	mkdir(directories['lang'])
	Setup = True

S = Setup(None, "Letter Studio v1.00 Setup")
#W = MainWindow(None, "Letter Studio v1.00")

A.MainLoop()
