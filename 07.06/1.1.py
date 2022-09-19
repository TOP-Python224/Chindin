import datetime as dt

now_year = dt.datetime.now().year

print("Введите имя: ")
name = input()
print("Введите фамилию: ")
surname = input()
print("Введите год рождения: ")
birthday = input()

print(name, surname, ',', now_year-int(birthday))
