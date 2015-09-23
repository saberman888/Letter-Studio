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



import wx
import cio


#Ctools.py


def delete_word(word):
    del word

def delete_dialect(d):
    del d

def delete_dialects(conlang, mode):
    if len(conlang.dialects) != 0:
        for x in conlang.dialects:
            del x

    else:
        if mode == 0:
            wx.MessageBox(lang['NO_DIALECTS_DELETE'], wx.OK)
        return 0



def delete_words(conlang, mode):
    if len(conlang.words) != 0:
        for x in conlang.words:
            del x


    else:
        if mode == 0:
            wx.MessageBox(lang['NO_WORDS_DELETE'], wx.OK)
        return 0

def dump_conlang(conlang):
    delete_dialects(conlang, 1)
    delete_words(conlang, 1)
    del conlang
    wx.MessageBox(lang['CONLANG_DELETED'], wx.OK)
    
    
def edit(item):
    prev = item
    new = wxprompt(None, lang['EDIT'], prev)
    return new

