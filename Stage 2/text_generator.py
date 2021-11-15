from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams


class TextTokenize:
    def __init__(self,filename):
        self.f = open(filename, "r", encoding="utf-8")
        self.lines = self.f.readlines()
        self.text = " ".join(self.lines)
        self.wct = WhitespaceTokenizer()
        self.words = self.wct.tokenize(self.text)
        self.length = len(self.words)
        self.bigram = bigrams(self.text)
        self.f.close()

    def get_words(self):
        return self.words

    def get_length(self):
        return self.length

    def get_word(self, num, add=0):
        try:
            num = int(num)
            return self.words[num+add]
        except IndexError:
            return "Index Error. Please input an integer that is in the range of the corpus."
        except ValueError:
            return "Type Error. Please input an integer."

if __name__ == "__main__":
    file = input()
    tt = TextTokenize(file)
    print(f"{len(tuple(tt.bigram))}")
    while True:
        num = input()
        if num == "exit":
            break
        print(f"Head: {tt.get_word(num)} Tail: {tt.get_word(num,1)}")

