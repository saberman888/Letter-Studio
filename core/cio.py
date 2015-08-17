import zipfile
import xml.etree.ElementTree as ET
import os

def load_configuration(filename):
    #todo
    pass

def save_data(conlang, zpack=0):
    xml_metdata = ET.Element("metadata")
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
    mtree.close()

    #Set up dictionary
    if len(conlang.words) != 0:
            for x in conlang.words:
                word = ET.SubElement(xml_dictionary,"word")
                ET.SubElement(word, "word").text = x.word
                ET.SubElement(word, "definition").text = x.definition
                ET.SubElement(word, "ipa").text = x.ipa
                Et.SubElement(word, "pos").text = x.pos
                ET.SubElement(word, "register").text = x.register
                ET.SubElement(word, "class").text = x._class
                ET.SubElement(word, "source lang").text = x.source_lang
                ET.SubElement(word, "source").text = x.source
                ET.SubElement(word, "notes").text = x.notes


            dtree = ET.ElementTree(xml_dictionary)
            dtree.write("dictionary.xml")
            dtree.close()
    if len(conlang.dialects) != 0:
        #Write dialects
        for x in conlang.dialects:
            dialect = ET.SubElement(xml_dialect, "dialect")
            ET.SubElement(dialect, "name").text = x.Name
            ET.SubElement(dialect, "description").text = x.description

        ditree = ET.ElementTree(xml_dialect)
        ditree.write("dialects.xml")
        ditree.close()
    if op == 0 or op == 3:
        with open(filename, 'w') as myconlang:
            myconlang.write('metadata.xml')
            myconlang.write('dictionary.xml')
            myconlang.write('dialects.xml')
            myconlang.close()
            if op != 3:
                os.remove('metadata.xml')
                os.remove('dictionary.xml')
                os.remove('dialects.xml')
                
        

def load_data(filename):
    zipdata = ZipFile(filename, 'r')
    meta = ET.parse(zipdata.open('metadata.xml', 'r'))
    dictionary = ET.parse(zipdata.open('dictionary.xml', 'r'))
    dialect = ET.parse(zipdata.open('dialect.xml', 'r'))

    meta_root = meta.getroot()
    dict_root = dictionary.getroot()
    dial_root = dialect.getroot()
    
        
    #todo
    pass
        
        
