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



import os
import conassets
from language import *
from wx.alert import *


def getchar(i=""):
	return raw_input(i)

def delete_word(word):
    """Deletes a word"""
    del word


def delete_dialect(d):
    """Deletes a dialect"""
    del d


def delete_dialects(conlang, mode):
    """Deletes all dialects from conlang listed from parameter.
       mode is used to display a message, if mode is 0 then the message will display
       otherwise it wont.
    """
    if len(conlang.dialects) != 0:
        for x in conlang.dialects:
            del x

    else:
        if mode == 0:
	    Show(Dictionary['ND2BDeleted'], Dictionary['NDF'])
        return 0


def delete_words(conlang, mode):
    if len(conlang.words) != 0:
        for x in conlang.words:
            del x


    else:
        if mode == 0:
	    Show(Dictionary['NW2BDeleted'], Dictionary['NWF'])
        return 0


def dump_conlang(conlang, exit=0):
    """Used to delete conlang currently loaded in the program"""
    delete_dialects(conlang, 1)
    delete_words(conlang, 1)
    del conlang
    if exit == 1:
        #print "Conlang terminated. Press enter to exit program"
        #p = raw_input()
        os._exit(0)
    return


def edit(item):
    prev = item
    i = raw_input()
    return (i, prev)


def Format4Save(description):
    """Replaces \n characters with __N__"""
    return description.replace('\n', '__N__')


def Format4Load(description):
    """Replaces __N__ characters with \n"""
    return description.replace('__N__', '\n')


def GetDesc(C):
    """Gets Dialect or Class description"""
    return C.description


def GetName(C):
    """Gets Dialect or Class name"""
    return C.Name

def ReturnPOSName(ps, pos):
    """Returns the a pos term"""
    for k, e in pos.iter:
        if e == ps:
            return k
