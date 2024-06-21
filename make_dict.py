# Import Buid-in Libraries
import string
import os



def create_file(filename, text_list):
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            for text in text_list:
                file.write(text + '\n')
        
    else:
        with open(filename, 'w') as file:
            for text in text_list:
                file.write(text + '\n')


def get_combinations():
    letters = []

    for first_letter in string.ascii_lowercase:
        for second_letter in string.ascii_lowercase:
            if first_letter != second_letter:
                letters.append(first_letter + second_letter)
            
            else:
                letters.append(first_letter)
            
    return letters


def delete_null_files(letter):
    with open(f"dictionary/{letter}.txt", 'r') as file:
        rows = file.readlines()
        
    if rows == []:
        os.remove(f"dictionary/{letter}.txt")
    

def get_rows_with_letter(letter, master_file='dictionary.txt'):
    words = []
        
    with open(master_file, 'r') as file:
        rows = file.readlines()
        
        for row in rows:
            if len(row.strip()) == 1:
                if row.strip()[0] == letter:
                    words.append(row.strip())
                
            else:
                if row.strip()[0] + row.strip()[1] == letter:
                    words.append(row.strip())
                
    return words



if __name__ == '__main__':
    letters = get_combinations()

    for letter in letters:
        text_list = get_rows_with_letter(letter)
        create_file(f'dictionary/{letter}.txt', text_list)
        delete_null_files(letter)

