"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

ENCODING = 'utf-8'
REF_FILE = 'referat.txt'
NEW_REF_FILE = 'referat2.txt'


def read_file(filename):
    try:
        with open(filename, 'r', encoding=ENCODING) as f:
            text = f.read()
    except IOError:
        raise FileExistsError
    return text


def write_file(filename, text):
    try:
        with open(filename, 'w', encoding=ENCODING) as f:
            f.write(text)
    except IOError:
        raise FileExistsError


def main():
    text = ''
    try:
        text = read_file(REF_FILE)
    except FileExistsError:
        print('File read file')
        exit(1)

    print(len(text))
    print(len(text.split()))
    new_text = text.replace('.', '!')

    try:
        write_file(NEW_REF_FILE, new_text)
    except FileExistsError:
        print('File write error')


if __name__ == "__main__":
    main()
