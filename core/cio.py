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
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from conassets import *
from ctools import *


def save(filename, conlang):
    """Saves constructed language data, parameters - filename and """
    try:
        # Write all artifical language data into its file
        with open(filename, 'w') as k:
            # Start with language's metadata
            k.write("!METADATA_START\n")
            k.write("\t-->!CONLANG:%s:\n".encode("utf8") % conlang.Name)
            k.write("\t-->!AUTHOR:%s:\n".encode("utf8") % conlang.Author)
            k.write("\t-->!AUTHOR:%s:\n".encode("utf8") % conlang.Family)
            k.write("\t-->!Typology:%s:\n".encode("utf8") % conlang.T_Type)
            k.write("\t-->!Alignment:%s:\n".encode("utf8") % conlang.A_Type)
            k.write("\t-->!Language-Type:%s:\n".encode("utf8") % conlang.L_Type)
            k.write("!METADATA_END\n")

            k.write("!DIALECTS_START\n")
            for dialect in conlang.dialects:
                k.write("\t-->!DIALECT:%s:%s:\n".encode("utf8") % (dialect.Name, Format4Save(dialect.description)))
            k.write("!DIALECTS_END\n")

            k.write("!CLASSES_START\n")
            for CLASS in conlang.classes:
                k.write("\t-->!CLASS:%s:%s:\n".encode("utf8") % (CLASS.Name, Format4Save(CLASS.description)))
            k.write("!CLASSES_END\n")

            k.write("!DICTIONARY_START\n")
            for word in conlang.words:
                k.write("\t-->!word:%s:%s:%s:%s:%s:%s:%s:%s:\n".encode("utf8") % (
                    word.word, word.definition, word.pos, word.register,
                    word.Class, word.dialect, word.source_lang, word.notes))
            k.write("!DICTIONARY_END\n")

            k.close()
            print "Save successful!"
            return
    except IOError:
        print "Error! Save data failed!"
        return


def load(filename):
    """Load artificial language filename, process it and return it to the user"""
    import os.path
    if not os.path.isfile(filename):  # Make sure file is valid
        print "Error! File is not valid."  # If not return back to the user
        return
    meta = []
    classes = []
    dialects = []
    dict_ = []

    try:
        with open(filename, 'r') as l:
            l_read = l.readlines()

            mode = 0
            cmode = 0
            for v in l_read:
                if v.endswith("END\n"):
                    mode = 0
                    cmode = 0
                if mode == 1:
                    if cmode == 1:
                        mline = v.split(":")
                        # print len(mline)
                        # print mline[0]
                        meta.append(mline[1])
                    elif cmode == 2:
                        dline = v.split(":")
                        new_word = Word(dline[1], dline[2], dline[3], dline[4], dline[5], dline[6], dline[7], dline[8])
                        dict_.append(new_word)
                    elif cmode == 3:
                        diline = v.split(":")
                        new_dialect = Dialect(diline[1], diline[2])
                        dialects.append(new_dialect)
                    elif cmode == 4:
                        cline = v.split(":")
                        new_class = Class(cline[1], cline[2])
                        classes.append(new_class)

                elif v.endswith("START\n"):
                    mode = 1
                    if v.startswith("!METADATA"):
                        cmode = 1

                    elif v.startswith("!DICTIONARY"):
                        cmode = 2

                    elif v.startswith("!DIALECTS"):
                        cmode = 3

                    elif v.startswith("!CLASSES"):
                        cmode = 4

        print "metadata total: %s \n" % len(meta)
        print "dictionary total: %s \n" % len(dict_)
        print "dialect total: %s \n" % len(dialects)
        print "class total: %s\n" % len(classes)
        # Assemble the conlang data
        new_conlang = Conlang(meta[0].decode("utf8"), meta[1].decode("utf8"), meta[2].decode("utf8"),
                              meta[3].decode("utf8"),
                              meta[4].decode("utf8"), meta[5].decode("utf8"))
        # Add all the assets to the conlang
        for word in dict_:
            word.add2list(new_conlang)
        for dialect in dialects:
            dialect.add2list(new_conlang)
        for classs in classes:
            classs.add(new_conlang)
        return new_conlang

    except IOError:
        print "Error! Failed to load data from %s" % filename
        return
