# Программа использует модуль string и сторонний модуль requests
import string
import requests
import random

def get_random_string(length):
    """
    Генерирует случайную строку заданной длины из символов ascii_letters
    """
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def get_quote():
    """
    Получает цитату дня с сайта forismatic.com
    """
    response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
    quote = response.json()['quoteText']
    return quote

def remove_punctuation(text):
    """
    Удаляет все знаки пунктуации из текста
    """
    return text.translate(str.maketrans('', '', string.punctuation))

def count_letters(text):
    """
    Считает количество букв в тексте
    """
    return sum(c.isalpha() for c in text)

def main():
    """
    Получает цитату дня, удаляет из неё знаки пунктуации, считает количество букв и выводит результат
    """
    quote = get_quote()
    quote_no_punct = remove_punctuation(quote)
    num_letters = count_letters(quote_no_punct)
    print(f"Цитата дня: {quote}")
    print(f"Количество букв в цитате: {num_letters}")
    
if __name__ == '__main__':
    main()
