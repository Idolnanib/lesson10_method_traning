# Написать метод, который ведет список фильмов для просмотра на потом.
# Метод ПРИНИМАЕТ название фильма и ВОЗВРАЩАЕТ true, если фильм был добавлен в список, иначе false.
# Фильм может быть не добавлен в список, если он уже там есть
# Если фильм был успешно добавлен, то программа выводит список фильмов

def add_film(spisok, film):
    if film not in spisok:
        spisok.append(film)
        return True
    return False


films = []
while True:
    if add_film(films, input("Enter film: ")):
        print("Вот ваш список:")
        print(films)
    else:
        print("Такой фильм уже есть")