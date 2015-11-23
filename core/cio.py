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
#import wx
#from lang_loader import *


class Configuration():
    def __init__(self, appname, author, version, language):
        self.appname = appname
        self.author = author
        self.version = version
        self.language = language
        
    def update(self):
        if os.path.isfile("config.data"):
            os.remove("config.data")

        with open("config.data"):
            f.write("#!CONFIGDATA:BEGIN_BLOCK")
            f.write("#APPNAME:%s" % self.appname)
            f.write("#AUTHOR:%s" % self.author)
            f.write("#VERSION:%s" % self.version)
            f.write("#LANGUAGE:%s" % self.language)
            f.write("#!CONFIGDATA:END_BLOCK")
            f.close()
            
    def load(self):
        data = {}
        mode = 0
        with open("config.data","rb") as f:
            for x in f.readlines():
                if x.endswith("BEGIN_BLOCK") and x.beginswith("!#"):
                    mode = 1
                    
                elif x.endswith("END_BLOCK") and x.beginswith("!#"):
                    mode = 0
                elif x.endswith("BEGIN_LIST") and x.beginswith("!#"):
                    mode = 2
                elif x.endswith("END_LIST") and x.beginswith("!#"):
                    mode = 0

                if mode == 1:
                        x2 = x.split(":")
                        x2.split("#")
                        data = {x2[0],x2[1]}
			data[str(x2[0])] = x2[1]


        #update values
        self.appname = data['APPNAME']
        self.author = data['AUTHOR']
        self.version = data['VERSION']
        self.language = data['LANGUAGE']
        f.close()
        

                
            
        



def save_data(filename, conlang, zip=True):
    #Start with meta data
    with open("metadata.data", "a") as f:
        f.write("!#METADATA:BEGIN_BLOCK\n")
        f.write("#CONLANG:%s\n" % conlang.Name)
        f.write("#AUTHOR:%s\n"  % conlang.Author)
        f.write("#TTYPE:%s\n" % conlang.T_Type)
        f.write("#ATYPE:%s\n" % conlang.A_Type)
        f.write("#LTYPE:%s\n" % conlang.L_Type)
        f.write("!#METADATA:END_BLOCK\n")
        f.close()

    
    with open("dictionary.data", "a") as f:
        f.write("!#DICTIONARY:BEGIN_LIST\n")
        for x in conlang.words:
            #word;definition;pos;register;class;dialect;src-lang;src;notes
            f.write("#WORD;%s;%s;%s;%s;%s;%s;%s;%s;\n" % (x.word, x.definition, x.pos, x.register, x._class, x.dialect, x.source_lang, x.notes))
        f.write("!#DICTIONARY:END_LIST\n")

        f.write("!#DIALECTS:BEGIN_LIST\n")
        if len(conlang.dialects) != 0:
            for x in conlang.dialects:
                f.write("#DIALECT;%s;%s\n" % (x.Name, x.description))
        f.write("!#DIALECTS:END_LIST\n")


	
        f.write("!#CLASSES:BEGIN_LIST\n")
        if len(conlang.classes) != 0:
            for x in conlang.classes:
	        f.write("#CLASS;%s;%s\n" % (x.Name, x.description))
	f.write("!#CLASS:END_LIST\n")
        f.close()

       
	if zip == True:
            with zipfile.ZipFile(filename, "w") as myconlang:
                myconlang.write("metadata.data")
                myconlang.write("dictionary.data")
                os.remove("metadata.data")
                os.remove("dictionary.data")
            myconlang.close()


def load_data(filename):
    ZDATA = zipfile.ZipFile(filename, 'r')
    METADATA = ZDATA.open('metadata.data', 'r')
    DICTIONARY = ZDATA.open('dictionary.data', 'r')

    mode = 0 # 1 = block mode, 2 = list mode
    cmode = 0
    Meta = {}
    
    for x in METADATA.readlines():
        if x.endswith("BEGIN_BLOCK") and x.beginswith("!#"):
            mode = 1
            
        elif x.endswith("END_BLOCK") and x.beginswith("!#"):
            mode = 0
        elif x.endswith("BEGIN_LIST") and x.beginswith("!#"):
            mode = 2
        elif x.endswith("END_LIST") and x.beginswith("!#"):
            mode = 0
            
        elif mode == 1:
            if cmode == 1:
                x2 = x.split(":")
                x2.split("#")
                Meta[x2[0]] = x2[1]



    C = Conlang(Meta['CONLANG'], Meta['AUTHOR'], Meta['TTYPE'], Meta['ATYPE'], Meta['LTYPE'])

    for x in DICTIONARY.readlines():
        if x.endswith("BEGIN_BLOCK") and x.beginswith("!#"):
            mode = 1
	    if x.startswith("!#DIALECTS"):
	        cmode = 2
        elif x.endswith("END_BLOCK") and x.beginswith("!#"):
            mode = 0
        elif x.endswith("BEGIN_LIST") and x.beginswith("!#"):
            mode = 2
        elif x.endswith("END_LIST") and x.beginswith("!#"):
            mode = 0

        if mode == 1:
            x2 = x.split(";")
            x2.split("#")
            WORD = Word(x2[1],x2[2],x2[3],x2[4],x2[5],x2[6],x2[7],x2[8])
            WORD.add2list(C)
                
            if cmode == 2: #Dialect parse mode
                x2 = x.split(";")
                x2.split("#")
                DIALECT = Dialect[str(x2[1])] = x2[2]
                DIALECT.add2list(C)


    return C


            

        
def wxprompt(parent=None, message='', default_value=''):
    dialog = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    dialog.ShowModal()
    result = dialog.GetValue()
    dialog.Destroy()


