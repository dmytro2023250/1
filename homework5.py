#AI. Порграма має відповісти на питання чи є введений стрінг
#1 - номером телефону
#2 - email-ом
#3 - Іменем з ініціалами
#4 - Даними невідомого формату

#+380631112233 -> Phone
#bcdef@abc.efg -> email   3+ letters @ 3 letters. 3 letters
#Bill J.I. -> name   2 words
#something else -> unknown
raw_str = input("Введіть символи")
if len(raw_str) == 13 and raw_str[0] == "+":
    print("Phone number")
elif len((splited := raw_str.split('.'))) == 2:
    _name = splited[0]
    _initials = splited[1]
    if _name.isalpha() and _name.capitalize() == _name:
        if _initials[-1] == "." and _initials[-3] == "." and _initials[0].isalpha() and _initials[0].upper() == _initials[2].isalpha() and _initials[2].upper() == _initials[2]:
            print("name")
email = raw_str
if email.count("@") == 1 and email[0] != "@" and email.count(".") > 0 and email.rfind(".") and email.find("@"):
    print("Email")
else:
    print("Невідомо")




