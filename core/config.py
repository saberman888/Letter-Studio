


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
from wx.alert import *
import time
from core.ctools import *
import os
import ConfigParser
#Config redone as of 2/2/16
Configuration = {

}

PermanintCFG = {
    "NAME": "Letter Studio",
    "AUTHOR": "Andres O. Vazquez",
    "Version": "1.0.0",
    "License": "MIT License"
}

def FTC(cwd): #first time configuration
    print "Welcome to Letter Studio %s first time configuration!" % (PermanintCFG['Version'])
    time.sleep(2)
    print "Would you like to set default language as English (Y/N)?\n"
    answer = getchar(">>")
    answer.upcase()
    if answer == "Y":
        print ".."
        Configuration['lang'] = "en_US"
    elif answer == "N":
        print "Please specify the path to a translation file for LS %s" % (PermanintCFG['Version'])
        answer = getchar(">>")
        Configuration['language_location'] = answer
    print "Configuration setup! Exiting in 10 seconds.\n"
    time.sleep(10)
    os._exit()    
    

def ObtainSettings(RLPC):
    if os.path.isfile(RLPC):
        conf = ConfigParser.ConfigParser()
        conf.read(RLPC)
        Configuration["lang"] = conf.get('Main', 'setlanguage')
        Configuration['language_location'] = conf.get("Main", "language_location")
        return 0
    WARN("ls.conf not found!")
    return 1
            
def UpdateSettings(RLPC):
    conf = ConfigParser.RawConfigParser()

    conf.add_section("Main")
    conf.set("Main", "lang", Configuration['lang'])
    conf.set("Main", "language_location", Configuration['language_location'])
    try:
        with open(RLPC, 'w') as cfgp:
            cfgp.write(conf)
            cfgp.close()
            return 0
    except IOError:
        Panic("Unable to save configuration settings to ls.conf")
        return 1
