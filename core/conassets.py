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


class Conlang():
    def __init__(self, Name, Author, Family, T_Type, A_Type, L_Type):
        self.Name = Name
        self.Author = Author
        self.Family = Family
        self.T_Type = T_Type #Typology type
        self.A_Type =A_Type #Alignment type
        self.L_Type = L_Type #Language type
        self.dialects = []
        self.words = []


class Dialect():
    def __init__(self, Name, description):
        self.Name = Name
        self.description = description

    def add2list(self, conlang):
        conlang.dialects.append(self)

        
class Word():
    def __init__(self, word, definition, ipa, pos, register, _class, dialect, source_lang, source, notes):
        
        self.word = word
        self.definition = definition
        self.pos = pos
        self.register = register
        self._class = _class
        self.dialect = dialect
        self.source_lang = source_lang
        self.source = source
        self.notes = notes

    def add2list(self, conlang):
        conlang.words.append(self)

