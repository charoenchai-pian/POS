import pandas

dic_menu1 = {
    "menu" : ["Som tum", "Tom yum", "Pad thai"],
    "price" : [50, 60, 70]
}
df1 = pandas.DataFrame(dic_menu1)
df1.to_csv("Menu1_thai_food.csv")

dic_menu2 = {
    "menu" : ["Sushi", "Ramen", "Tempura"],
    "price" : [100, 120, 150]
}
df2 = pandas.DataFrame(dic_menu2)
df2.to_csv("Menu2_japanese_food.csv")

dic_menu3 = {
    "menu" : ["Lasagna", "Pizza", "Pasta"],
    "price" : [200, 300, 400]
}
df3 = pandas.DataFrame(dic_menu3)
df3.to_csv("Menu3_italian_food.csv")
