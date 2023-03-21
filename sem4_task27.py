"""
Задача N27. Пользователь вводит текст(строка).
Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним
или большим числом пробелов. Определите,
сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore
The shells that she sells are sea shells
I'm sure.So if she sells sea shells on the
sea shore I'm sure that the shells are sea shore shells
Output: 13
15 минут

"""

string = """She sells sea shells on the sea shore The shells 
that she sells are sea shells I'm sure.So if she sells sea 
shells on the sea shore I'm sure that the shells are sea 
shore shells"""


def word_counter(string: str):
    result = {i for i in string
                        .lower()
                        .replace(".", " ")
                        .split()}

    print(result)
    return f"There is - {len(result)} different words"


print(word_counter(string))

# решение от Виталия

text = input("Введите текст: ")

# разбиваем текст на слова
words = text.split()

# создаем множество для хранения уникальных слов
unique_words = set()

# проходимся по каждому слову и добавляем его в множество уникальных слов
for word in words:
    unique_words.add(word)

# выводим количество уникальных слов в тексте
print("Количество различных слов в тексте:", len(unique_words))