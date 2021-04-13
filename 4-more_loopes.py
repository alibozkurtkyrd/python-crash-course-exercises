
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my food:")
for i in my_foods:
    print("\t",i)
print("\nFriend foods:")
for i in friend_foods:
    print("\t",i)
