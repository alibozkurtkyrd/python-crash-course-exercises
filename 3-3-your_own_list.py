my_own_list =['fiat','hyundai','skoda','woswogen']
message = "I think that my first car will be " + my_own_list[1].title() + " because it's so affordable"
print(message)

message = " I will buy " + my_own_list[2] + "model car 10 years later because the number of family number might increase."
print(message.lstrip())
#not lstrip() i kullanma nedenim 2.message  değişkenimde sol tarafta boşluk var o yüzden bilerek yazdım

message ="if I had enough money, I would like to buy" + " " + my_own_list[3] + " model car"
print(message)
#not ister boşluk bırakmak için iki tırnak arası boşluk koy ya da string bitimine tırnak öncesi bir boşluk bırak
