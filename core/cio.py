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
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
        
import zipfile
import os
import conassets
import wx
from lang_loader import *

lang = load_lang_data('config.xml')
def load_configuration(filename):
    settings = ET.parse(filename)
    root = settings.getroot()
    return (root.find('appname').text, root.find('author').text, root.find('version').text)



def save_data(filename, conlang):
    #Start with meta data
    with open("metadata.data", "a") as f:
        f.write("!#METADATA:BEGIN_BLOCK")
        f.write("#CONLANG:%s") % conlang.Name
        f.write("#AUTHOR:%s") % conlang.Author
        f.write("#TTYPE:%s") 
        f.write("!#METADATA:END_BLOCK")
        f.close()

    
    with open("dictionary.data", "a") as f:
        f.write("!#DICTIONARY:BEGIN_LIST")
        for x in conlang.words:
            #word;definition;pos;register;class;dialect;src-lang;src;notes
            f.write("#WORD;%s;%s;%s;%s;%s;%s;%s;%s;%s") % (x.word, x.definition, x.pos, x.register, x._class, x.dialect, x.source_lang, x.source, x.notes)
        f.write("!#DICTIONARY:END_LIST")

        f.write("!#DIALECTS:BEGIN_LIST")
        if len(conlang.dialects) != 0:
            for x in conlang.dialects:
                f.write("#DIALECT;%s;%s")% (x.Name, x.description)
        f.write("!#DIALECYS:END_LIST")
        f.close()

        with zipfile.ZipFile(filename, "w") as myconlang:
            myconlang.write("metadata.data")
            myconlang.write("dictionary.data")
            os.remove("metadata.data")
            os.remove("dictionary.data")


def load_data(filename):
    ZDATA = zipfile.Zipfile(filname, 'r')
    METADATA = open(zipdata.open('metadata.data', 'r'))
    DICTIONARY = open(zipdata.open('dictionary.data', 'r'))
    mode = 0 # 1 = Block mode, 2 = list mode
    for x in METADATA.readlines():
        if x.endswith("BEGIN_LIST") and x.beginswith("!#"):
            mode = 1
        if x.endswith("END_LIST") and x.beginswith("!#"):
            mode = 0

        if mode == 1:
            
            
            

        (conlang.T_Type,conlang.A_Typemconlang.:_Type)
            
            

        
def wxprompt(parent=None, message='', default_value=''):
    dialog = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    dialog.ShowModal()
    result = dialog.GetValue()
    dialog.Destroy()
    return result


