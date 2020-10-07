class Contact:
    def __init__(self, name, phone, birthday, address):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        print(f"Создаём новый контакт {name}")


mike = Contact("Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6")
vlad = Contact("Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12")


def print_contact():
    print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")


# здесь измените адрес для объекта mike
# здесь измените телефон для объекта mike
mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
mike.phone = 'К-058-67'
vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
vlad.phone = '2-35-71'
# здесь измените адрес для объекта vlad
# здесь измените телефон для объекта vlad

print_contact()  # выводим данные на экран