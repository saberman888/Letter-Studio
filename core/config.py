

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

Configuration = {

}

PerminantCFG = {
    "NAME": "QuickLang",
    "AUTHOR": "Andres O. Vazquez",
    "Version": "1.0.0",
    "License": "MIT License"
}


def GetConfiguration(dir):
  
    try:
        _ = dir+"/core/data/config.cfg"
    except IOError:
        import os
        print "Error! Unable to find Configuration file! Error code 11-22"
        i = raw_input()
        os._exit(0)

    try:
        with open(_) as f:
            for line in f.readlines():
                linez = line.split("=")
                Configuration[linez[0]] = linez[1]
        f.close()
    except IOError:
        import os
        print "Error! Unable to load Configuration! ErrorCode: 11"
	print dir, " is not a valid directory."
        i = raw_input()
        os._exit(0)

def Update(e, v):
	Configuration[e] = v


def UpdateSettings(dir):
	dir = dir+"/core/data/config.cfg"
	for x, y in Configuration:
		for x in Configuration:
			f.write(x+"="+y)
	f.close()
