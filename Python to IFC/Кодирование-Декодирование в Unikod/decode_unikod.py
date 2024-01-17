import re
import os


# Перевод символов unikod в кирилицу
def line_change_to_rus(line):
    pattern = r"\\X2\\(\w{4,})\\X0\\"           # Регулярка для поиска \X2\....\X0\
    res = re.sub(pattern, unikod_to_rus, line)  # Замена найденного выражение через функцию
    return res


def unikod_to_rus(matchobj):
    word = matchobj.group(1)                    # Обращение к скобочной группе получаемой регуляркой
    letters = re.findall(r"\w{4}", word)        # "Сплит" по 4 символам
    res = ""                                    # Получение итоговой подстроки
    for letter in letters:
        res += chr(int(letter, 16))             # Замена кодировки unikod на буквы
    return res


# Перевод символов кирилицы в кодировку unikod
def line_change_to_unikod(line):
    pattern = r"[а-яА-Я]{1,}"                   # Регулярка для поиска слов из кирилицы
    res = re.sub(pattern, rus_to_unikod, line)  # Замена найденного слова через функцию
    return res


def rus_to_unikod(matchobj):
    word = matchobj.group(0)                    # Обращение к найденной группе
    res = ""
    for letter in word:
        digit = str(hex(ord(letter)))           # Перевод каждой буквы в число unikod в 16-чной форме
        res += re.sub("x", "", digit).upper()
    return "\X2\\" + res + "\X0\\"


def translation(dir, translation_mode = True):
# Поиск и перебор всех файлов IFC в каталоге
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.ifc'):
                with open(os.path.join(root, file), "r") as f:
                    print(file)
                    with open(os.path.join(root, file[:-4]+"_clean.ifc"), "w") as copy:
                        # Перевод символов кирилицы в кодировку unikod
                        if translation_mode:
                            for line in f:
                                copy.write(line_change_to_unikod(line))
                        # Перевод символов unikod в кирилицу
                        else:
                            for line in f:
                                copy.write(line_change_to_rus(line))
                os.remove(os.path.join(root, file))
                os.rename(os.path.join(root, file[:-4] + "_clean.ifc"), os.path.join(root, file))


if __name__ == "__main__":
    dir = r'I:\TEST'
    translation(dir, True)
