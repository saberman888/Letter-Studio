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
import xml.etree.ElementTree as ET
import os
import conassets
import wx
from lang_loader import *

lang = load_lang_data('config.xml')
def load_configuration(filename):
    settings = ET.parse(filename)
    root = settings.getroot()
    return (root.find('appname').text, root.find('author').text, root.find('version').text)



def save_data(filename, conlang, zpack=0):
    xml_metadata = ET.Element("metadata")
    xml_dictionary = ET.Element("dictionary")
    xml_dialect = ET.Element("dialects")


    #Set up metadata first
    ET.SubElement(xml_metadata, "conlang").text = conlang.Name
    ET.SubElement(xml_metadata, "author").text = conlang.Author
    ET.SubElement(xml_metadata, "family").text = conlang.Family
    ET.SubElement(xml_metadata, "T_Type").text = conlang.T_Type
    ET.SubElement(xml_metadata, "A_Type").text = conlang.A_Type
    ET.SubElement(xml_metadata, "L_Type").text = conlang.L_Type

    mtree = ET.ElementTree(xml_metadata)
    mtree.write("metadata.xml")

    #Set up dictionary
    if len(conlang.words) != 0:
            for x in conlang.words:
                word = ET.SubElement(xml_dictionary,"word")
                ET.SubElement(word, "word").text = x.word
                ET.SubElement(word, "definition").text = x.definition 
                ET.SubElement(word, "pos").text = x.pos
                ET.SubElement(word, "register").text = x.register
                ET.SubElement(word, "class").text = x._class
                ET.SubElement(word, "dialect").text = x.dialect
                ET.SubElement(word, "source lang").text = x.source_lang
                ET.SubElement(word, "source").text = x.source
                ET.SubElement(word, "notes").text = x.notes


            dtree = ET.ElementTree(xml_dictionary)
            dtree.write("dictionary.xml")
    if len(conlang.dialects) != 0:
        #Write dialects
        for x in conlang.dialects:
            dialect = ET.SubElement(xml_dialect, "dialect")
            ET.SubElement(dialect, "name").text = x.Name
            ET.SubElement(dialect, "description").text = x.description

        ditree = ET.ElementTree(xml_dialect)
        ditree.write("dialects.xml")
    if zpack == 0 or zpack == 3:
        with zipfile.ZipFile(filename, "w") as myconlang:
            myconlang.write("metadata.xml")
            myconlang.write("dictionary.xml")
            myconlang.write("dialects.xml")
            myconlang.close()
        if zpack == 3:
            os.remove('metadata.xml')
            os.remove('dictionary.xml')
            os.remove('dialects.xml')
                
        

def load_data(filename):
    zipdata = zipfile.ZipFile(filename, 'r')
    meta = ET.parse(zipdata.open('metadata.xml', 'r'))
    dictionary = ET.parse(zipdata.open('dictionary.xml', 'r'))
    dialect = ET.parse(zipdata.open('dialect.xml', 'r'))

    meta_root = meta.getroot()
    dict_root = dictionary.getroot()
    dial_root = dialect.getroot()
    
    #Get metadata
    C = Conlang(meta_root.find('conlang').text, meta_root.find('author'), meta_root.find('family').text, meta_root.find('T_Type').text, meta_root.find('A_Type').text, meta_root.find('L_Type').text)
    
    #Get dictionary data
    for word in dict_root.findall('word'):
        W = Word(word.find('word').text, word.find('definition').text, word.find('ipa').text, word.find('register').text, word.find('class').text, word.find('dialect'), word.find('source_lang').text, word.find('source').text, word.find('notes').text)
        W.add2list(C)

    #Load all dialect data
    for dialect in dial_root.findall('dialect'):
        D = Dialect(dialect.find('name').text, dialect.find('description').text)
        D.add2list(C)
        

    return C
        
        
def wxprompt(parent=None, message='', default_value=''):
    dialog = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    dialog.ShowModal()
    result = dialog.GetValue()
    dialog.Destroy()
    return result


