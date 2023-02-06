import string


class Alphabet:
    lang = 'ru'
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    def __init__(self, lang=lang, letters=letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        return self.letters

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26
    def __init__(self):
        super().__init__('eng', string.ascii_uppercase)


    def is_in_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False


    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print(f"English Example:\nDon't judge a book by it's cover.")

if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    print(eng_alphabet.print())
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_in_letter("F"))
    print(eng_alphabet.is_in_letter("Щ"))
    eng_alphabet.example()
