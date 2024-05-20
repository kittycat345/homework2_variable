#Задача «Работаем с выводом данных».
product_name=input("Название товара")
price_of_product=float(input("Цена товара"))
weight_of_product=float(input("Вес товара"))
money_user=float(input("Количество денег у пользователя"))
end_price=(price_of_product*weight_of_product)
change=str(money_user-end_price)
print("Чек "+product_name+"-"+str(weight_of_product)+"кг"+" -"+str(price_of_product)+" руб/кг")
print("Итого: "+str(end_price)+" руб Внесено: "+str(money_user)+" руб Сдача: "+change+" руб")

