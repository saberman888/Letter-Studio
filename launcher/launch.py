import sys
import os
def main():
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
        response = urllib.urlretrieve('null', 'core.zip')
        print "Done."
        print "Press enter to continue."
        i = raw_input()
        os.system('cls')
        main()


if __name__ == "__main__":
    main()
    
    
