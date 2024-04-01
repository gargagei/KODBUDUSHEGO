print("Здравствуйте! Это генератор альбомов от Анны Маргарян")
print("Выберите подходящую для вас команду")
music_catalog=[{"title": "мои (твои) тёмные желания", "author": "ooes", "year": 2021, "genre": "меланхолия", "data": 22},
               {"title": "export", "author": "iowa", "year": 2014, "genre": "pop", "data": 49},
               {"title": "Точки расставлены", "author": "ёлка", "year": 2011, "genre": "pop", "data": 66}]
def add_album():
    album = {}
    album["title"] = input("Введите название альбома: ")
    album["author"] = input("Введите имя исполнителя: ")
    album["year"] = input("Год выпуска: ")
    album["genre"] = input("Жанр альбома: ")
    album["data"] = input("Продолжительность в минутах: ")
    music_catalog.append(album)
def view_albums():
    if len(music_catalog) == 0:
        print("Нет данных")
        return
    n=""
    for i in music_catalog:
        for j in i.values():
            n+= str(j) + " | "
        n+="\n"
    print(n)
def album_search():
    z=input("Введите имя исполнителя: ")
    c=0
    for i in music_catalog:
        if i["author"] == z:
            print(i["title"])
            c+=1
    if c == 0:
        print("Исполнитель не найден")
def delete_album():
    g=0
    z = input("Введите название альбома который вы хотите удалить: ")
    for i in music_catalog:
        if i["title"] == z:
            g+=0
            music_catalog.remove(i)
            print("Введенный альбом удален")
    if g == 0:
        print("Альбома не существует")


while True:

    print("\n1. Добавить альбом")
    print("2. Посмотреть все альбомы")
    print("3. Поиск музыки")
    print("4. Удалить альбом")
    print("5. Выход")
    choice = input("Выберите опцию: ")
    if choice == "1":
        print("\nВы выбрали пункт меню Добавить альбом\n")
        add_album()
    elif choice == "2":
        print("\nВы выбрали пункт меню Посмотреть все альбомы\n")
        view_albums()
    elif choice == "3":
        print("\nВы выбрали пункт меню Поиск\n")
        album_search()
    elif choice == "4":
        print("\nВы выбрали пункт меню Удалить альбом\n")
        delete_album()
    elif choice == "5":
        break
    else:
        print("Не получилось. Выбери пэж меню снова")
















