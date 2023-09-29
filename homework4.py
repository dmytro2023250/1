#Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.

#text = input("Введіть текст:")
#vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
#words = text.split(" ")
#count = text.count(" ") + 0
#for word in words:
 #   consecutive_vowels = 0
  #  for letter in word:
   #     if letter in vowels:
    #        consecutive_vowels += 1
     #       if consecutive_vowels == 2:
      #          count += 1
       #         break
        #    else:
         #      consecutive_vowels = 2
          #  print("Кількість слів з двома голосними підряд:",count)


#Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
# "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран
# назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:

#prices = { "cito": 47.999, "BB_studio":42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
 #"the_partner": 38.988, "store": 37.720, "rozetka": 38.003}
#lower_limit = 35.9
#upper_limit = 37.339
#result = [shop for shop,price in prices.items()if lower_limit <= price <= upper_limit]
#for shop in result:
 #   print("match:",shop)