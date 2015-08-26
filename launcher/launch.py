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



import sys
import os
def main():
    if sys.argv[1] != '-u': #-u stands for update.
        
        try:
            sys.path.insert(0, 'core.zip')
            from core.conassets import *
            from core.conassets import *
            from core.ctools import *
            #Todo
        except IOError:
            print "Core not found."
            print "Downloading core..."
            import urllib
            response = urllib.urlretrieve(url, 'core.zip')
            print "Done."
            print "Press enter to continue."
            i = raw_input()
            os.system('cls')
            main()
    elif sys.argv[1] == '-u':
        print "Updating..."
        try:
            import urlib
            response = urllib.urlretrieve(url, 'core.zip')
            print "Done!"
            print "Press enter to exit."
            i = raw_input()
            del i
            os._exit()


if __name__ == "__main__":
    main()
    
    
