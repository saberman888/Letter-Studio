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

from ck3 import *
import conassets
import zipfile


def save_data(conlang, filename, compress=True):
    #Start with Conlang metadata
    META = CMWriter("metadata.dats")
    META.NewBlock("Metadata")
    META.WriteVar("Conlang_Name", conlang.Name, "Metadata")
    META.WriteVar("Conlang_Author", conlang.Author, "Metadata")
    META.WriteVar("Conlang_Family", conlang.Family, "Metadata")
    META.WriteVar("Conlang_Typology", conlang.TType, "Metadata")
    META.WriteVar("Conlang_Alignment", conlang.AType, "Metadata")
    META.WriteVar("Conlang_Language_Type", conlang.LType, "Metadata")

    META.EndBlock("Metadata") #End writing metadata
    META.Close()

    #Next write Dialect data
    DIALECT = CMWriter("dialects.dats")
    DIALECT.NewList("Dialects")

    for dialect in conlang.dialects:
        DIALECT.AddToList(dialect.Name, "dialects")
        DIALECT.WriteSubVar(dialect.description)
        

    DIALECT.EndList("dialects")
    DIALECT.Close()

    #Finally write dictionary data
    DICT = CMWriter("dictionary.dats")
    DICT.NewList("Words")
    for word in conlang.words:
        DICT.AddToList(";%s;%s;%s;%s;%s;%s;%s;%s;" % (x.word, x.definition, x.pos, x.register, x._class, x.dialect, x.source_lang, x.notes), "Words")
    DICT.EndList("Words")
    DICT.Close()

    #Very last thing, write Class data
    CLASS_ = CMWriter("classes.dats")
    CLASS_.NewList("CLASSES")
    for classes_ in conlang.classes:
        CLASS_.AddToList(";%s;%s" % (classes_.Name, classes_.dictionary, "CLASSES"))

    CLASS_.EndList("CLASSES")
    CLASS_.Close()

    if compress == True:
        ZIP = zipfile.ZipFile(filename+".qlc", "w")

        ZIP.write("metadata.dats")
        ZIP.write("dialects.dats")
        ZIP.write("dictionary.dats")
        ZIP.close()
        if os.path.isfile("metadata.dats"):
            os.remove("metadata.dats")

        elif os.path.isfile("dialects.dats"):
            os.remove("dialects.dats")

        elif os.path.isfile("dictionary.dats"):
            os.remove("dictionary.dats")


        
    
