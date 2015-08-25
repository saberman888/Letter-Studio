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
            sys.exit(0)


if __name__ == "__main__":
    main()
    
    
