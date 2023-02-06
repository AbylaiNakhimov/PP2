import string

class Alphabet:
    def __init__(self, language:str, letters:str):
        self.lang = language
        self.letters = list(letters)
        
    def __repr__(self):
        return repr(self.letters)
        
    def size():
        return len(self.letters)
    
    
class EngAlphabet(Alphabet):
    __size = len(string.ascii_uppercase)
    
    def __init__(self):
        super().__init__(language='En', letters=string.ascii_uppercase)
        
    def is_english_letter(self, letter):
        return letter.upper() in self.letters
            
    def size(self):
        return type(self).__size
    
    @staticmethod
    def example():
        print('English Example:\nDon\'t judge a book by it\'s cover.')

if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    print(eng_alphabet)
    print(eng_alphabet.size())
    print(eng_alphabet.is_english_letter('F'))
    print(eng_alphabet.is_english_letter('Ё'))
    EngAlphabet.example()