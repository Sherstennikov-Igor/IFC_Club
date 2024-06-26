import os
import ifcopenshell.util
import ifcopenshell.util.element

# Структура данных {Класс: {Набор параметров: [Список параметров]}}
Pset_dict = {"IfcWall": {"Местоположение": ["Номер корпуса", "Номер секции", "Этаж", "Тест местоположение"],
                         "Маркировка": ["Позиция", "Обозначение", "Наименование"],
                         "Геометрические параметры": ["Толщина", "Длина", "Объем", "Высота"],
                         "Пожарные параметры": ["Предел огнестойкости", "Тип противопожарной преграды", "Класс пожарной опасности"],
                         "Строительные параметры": ["Материал", "Наружная", "Тестовый параметр для стен"],
                         "Тестовый набор для стен": ["Тест"]},
             "IfcDoor": {"Местоположение": ["Номер корпуса", "Номер секции", "Этаж"],
                         "Маркировка": ["Позиция", "Обозначение", "Наименование"],
                         "Геометрические параметры": ["Высота", "Высота в свету", "Высота порога", "Процент остекления", "Ширина", "Ширина в свету", "Тестовый параметр для дверей"],
                         "Пожарные параметры": ["Аварийный выход", "Предел огнестойкости", "Тип противопожарной преграды", "Эвакуационный выход"],
                         "Строительные параметры": ["Материал"],
                         "Тестовый набор для дверей": ["Тест"]}}

path = '..'
files = sorted(os.listdir(path))

B_elements = [] # Переменная для хранения элементов

for file in files:
    if file.endswith(".ifc"):
        print("\nОбработка файла", file, "\n")
        ifc_file = ifcopenshell.open(file)
        B_elements = ifc_file.by_type("IfcBuildingElement")     # Элементы каркаса здания IfcBuildingElement можно указывать нужные классы

    for i in B_elements:
        print(f"Элемент {i.is_a()} c GUID {i.get_info()['GlobalId']} ")
        ifc_class = i.is_a()                            # Получение класса IFC элемента
        Psets = Pset_dict.get(ifc_class)                # Получение требуемого набора параметров и свойств для класса IFC из словаря
        Data = ifcopenshell.util.element.get_psets(i)   # Выводит словарь свойств для элемента "Pset" : {"Prop" : "var"}

        try:
            for Pset, Props in Psets.items():
                if Pset not in Data.keys():
                    print(f"\t Элемент не содержит требуемого набора параметров '{Pset}'")
                else:
                  for Prop in Props:
                        if Prop not in Data.get(Pset):
                            print(f"\t Набор атрибутов '{Pset}': \n\t\t не содержит требуемого свойства '{Prop}'")
        except:
            print(f"\tДля элемента нет условия проверок")
