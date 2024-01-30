import os
from random import randint

def generate_words(word_count=500):
    words = ["apple", "banana", "cherry", "grape", "lemon", "orange", "peach", "mango", "pineapple", "raspberry"]
    return [words[randint(0, len(words) - 1)] for _ in range(word_count)]

def edit_files():
    for file in os.listdir('/mnt/c'):
        if file.endswith('.txt'):
            file_path = os.path.join('/mnt/c', file)
            with open(file_path, 'w') as file_obj:
                random_words = generate_words()
                new_content = " ".join(random_words)
                file_obj.write(new_content)
            print(f"File {file} has been edited.")

if __name__ == "__main__":
    edit_files()
