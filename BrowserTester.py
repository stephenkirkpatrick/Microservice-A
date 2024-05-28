import time

webpagestart = "https://www."
restaurant = ""
webpageend = ".com"

restaurant = "Mcdonalds"
restaurant = restaurant.replace(" ", "")
webpage = webpagestart + restaurant + webpageend
with open('webpage.txt', 'w', encoding="utf-8") as f:
    f.write(webpage)
time.sleep(10)

restaurant = "Burger King"
restaurant = restaurant.replace(" ", "")
webpage = webpagestart + restaurant + webpageend
with open('webpage.txt', 'w', encoding="utf-8") as f:
    f.write(webpage)
time.sleep(10)

restaurant = "Olive Garden"
restaurant = restaurant.replace(" ", "")
webpage = webpagestart + restaurant + webpageend
with open('webpage.txt', 'w', encoding="utf-8") as f:
    f.write(webpage)

