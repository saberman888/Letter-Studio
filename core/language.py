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


from config import *
from wx.alert import *
Dictionary = {

}

# syntax KEY:TRANSLATION


def load_language(configurate_file_name):
    """Loads language translation into a dictionary"""
    with open(configurate_file_name, 'r') as cfl:
        for line in cfl.readlines():
            linez = line.split("=")
            Dictionary[linez[0].decode("utf16")] = linez[1].decode("utf16"))
    cfl.close()


def ChoseLang(REALDIR):
    REALDIR = REALDIR+"/core/lang/"
    import os
    for x in os.listdir(REALDIR):
        print x
        i = raw_input()
        for x in os.listdir(REALDIR):
            if i == x:
                Show("Please restart for it to take effect.")
                Update('langdir', REALDIR+x)
                UpdateSettings(REALDIR)
                i = raw_input()
                os._exit()

def listLanguages(REALDIR):
	REALDIR = REALDIR+"/core/lang/"
	import os
	for x in os.listdir(REALDIR):
		if x.endswith(".lang"):
			print x[:len(x)-5]
	
