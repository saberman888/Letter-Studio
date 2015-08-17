import wx
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
            wx.MessageBox("There are no dialects to delete", wx.OK)
        return 0



def delete_words(conlang, mode):
    if len(conlang.words) != 0:
        for x in conlang.words:
            del x


    else:
        if mode == 0:
            wx.MessageBox("There are no words to delete", wx.OK)
        return 0

def delete_conlang(conlang):
    delete_dialects(conlang, 1)
    delete_words(conlang, 1)
    del conlang
    wx.MessageBox('Conlang has been deleted', wx.OK)
    

