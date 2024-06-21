# Import Buld-in Libraries
import unicodedata



class Accents:
    def __init__(self):
        pass


    def remove_accent(self, text):
        normalized_text = unicodedata.normalize('NFD', text)
        
        text_without_accents = ''.join(character for character in normalized_text if unicodedata.category(character) != 'Mn')
        
        return text_without_accents
    
    
    def __get_rows(self):
        words = []
        
        with open('words.txt', 'r') as file:
            rows = file.readlines()

        for row in rows:
            words.append(row.strip())

        return words
    
    
    def __get_words_by_letter(self, letter, 
                              position=0):
        words = []
        
        for word in self.__get_rows():
            if word[position] == letter:
                words.append(word)
        
        return words


    def __compare_words(self, word, similar_words):
        accented_word = word
        
        for similar_word in similar_words:
            if self.remove_accent(similar_word) == word:
                accented_word = similar_word
                break
        
        return accented_word
        
    
    def add_accent(self, text):
        text = text.lower()
        text = text.split(" ")
        accented_text = []
        
        for word in text:
            similar_words = self.__get_words_by_letter(word[0])
            word = self.__compare_words(word, similar_words)
            accented_text.append(word)
            
        accented_text = " ".join(accented_text)
        return accented_text
            
    
    
if __name__ == "__main__":
    print(Accents().add_accent("O uso, manejo e conservacao do solo sao fundamentais para garantir a saude do meio ambiente e a produtividade agricola. O solo e um recurso natural renovavel, mas pode ser degradado se nao for manejado de forma adequada. Tecnicas como rotacao de culturas, uso de adubacao organica e a preservacao da cobertura vegetal sao essenciais para manter a fertilidade do solo. Alem disso, a conservacao do solo ajuda a prevenir a erosao e a perda de nutrientes, contribuindo para um ecossistema mais equilibrado e sustentavel. Cuidar do solo e garantir um futuro melhor para as proximas geracoes."))