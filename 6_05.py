# Напишите программу, которая любой введенный казахский текст из кириллицы переводит в латиницу.

# Задаем таблицу соответствия кириллических символов и их латинских аналогов
conversion_table = {
    'А': 'A', 'Ә': 'Á', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Ғ': 'Ǵ', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'J', 'З': 'Z',
    'И': 'I', 'Й': 'Y', 'К': 'K', 'Қ': 'Q', 'Л': 'L', 'М': 'M', 'Н': 'N', 'Ң': 'Ń', 'О': 'O', 'Ө': 'Ó', 'П': 'P',
    'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'Ý', 'Ұ': 'U', 'Ү': 'Ú', 'Ф': 'F', 'Х': 'H', 'Һ': 'H', 'Ц': 'Ts', 'Ч': 'Ch',
    'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'І': 'I', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya', 'ҰҢ': 'W', 'ӘІ': 'Ai',
    'ӘУ': 'Au', 'ӨҢ': 'Ong', 'ҮІ': 'Ui', 'ҮҰ': 'Uw', 'ҚЫ': 'Qy', 'ҚЫЙ': 'Qiy', 'НҮ': 'Nw', 'ҰҚ': 'Uq', 'ҰЫ': 'Uy',
    'ҰЙ': 'Uı', 'ІЙ': 'Iy', 'ЕҢ': 'Eng', 'НГ': 'Ng', 'ЖЫ': 'Jy', 'ШЫ': 'Shy', 'ЧЫ': 'Chy', 'ҒЫ': 'Ǵy', 'ЫЙ': 'Yı'
}

# Считываем казахский текст на кириллице
qaz = input("Введите казахский текст на кириллице: ")
text = qaz.upper()

# Преобразуем текст в латиницу с помощью таблицы соответствия символов
latin_text = ''
for symbol in text:
    if symbol in conversion_table:
        latin_text += conversion_table[symbol]
    else:
        latin_text += symbol

# Выводим преобразованный текст на латинице
print("Текст на латинице:", latin_text)

# Қазақстан Республикасы Орталық Еуразиядағы ең үлкен елдерден бірі