

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
    def __init__(self, word, definiton, ipa, pos, register, _class, source_lang, source, notes):
        
        self.word = word
        self.defintion = definition
        self.ipa = ipa
        self.pos = pos
        self.register = register
        self._class = _class
        self.source_lang = source_lang
        self.source = source
        self.notes = notes

    def add2list(self, conlang):
        conlang.words.append(self)
