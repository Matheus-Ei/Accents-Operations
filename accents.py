# Import Buld-in Libraries
import unicodedata
from datetime import datetime


class Accents:
    def __init__(self):
        pass


    @classmethod
    def remove(cls, text):
        normalized_text = unicodedata.normalize('NFD', text)
        
        text_without_accents = ''.join(character for character in normalized_text if unicodedata.category(character) != 'Mn')
        
        return text_without_accents
    

    @classmethod    
    def __get_words_by_letter(cls, letter, all_words,
                              position=0):
        words = []
        
        for word in all_words:
            try:
                if cls.remove(word[position]) == letter:
                    words.append(word)
            
            except:
                pass
                
        return words


    @classmethod
    def __compare_words(cls, word, similar_words):
        accented_word = word
        
        for similar_word in similar_words:
            if cls.remove(similar_word) == word:
                accented_word = similar_word
                break
        
        return accented_word
        
    
    @classmethod
    def __get_rows(cls, letter):
        words = []
        
        letter = cls.remove(letter)
        
        with open(f'dictionary/{letter}.txt', 'r') as file:
            rows = file.readlines()
            
            for row in rows:
                words.append(row.strip())
                
        return words
    
    
    @classmethod
    def add(cls, text): 
        text = text.lower()
        text = text.split(" ")
        
        accented_text = []
        
        for text_word in text:
            if len(text_word) == 1:
                similar_words = cls.__get_rows(letter = text_word[0])
                
            else:
                similar_words = cls.__get_rows(letter = text_word[0] + text_word[1])            
            
            text_word = cls.__compare_words(text_word, similar_words)
            accented_text.append(text_word)
            print(text_word)
            
        accented_text = " ".join(accented_text)
        return accented_text
    

    @classmethod
    def get_time(cls, text):
        start = datetime.now()
        
        text = cls.add(text)
        
        end = datetime.now()
        print(f"Time: {end - start}")
        
        return text
            
    
    
if __name__ == "__main__":
    print(Accents.get_time("o uso, manejo e conservação do solo são fundamentais para garantir a saúde do meio ambiente e a produtividade agricola. o solo e um recurso natural renovavel, mas pode ser degradado se não for manejado de forma adequada. tecnicas como rotação de culturas, uso de adubação organica e a preservação da cobertura vegetal são essenciais para manter a fertilidade do solo. além disso, a conservação do solo ajuda a prevenir a erosão e a perda de nutrientes, contribuindo para um ecossistema mais equilibrado e sustentavel. cuidar do solo e garantir um futuro melhor para as proximas geracoes."))