
languages = ['Turkish','English','France','German','Korean','Arabic','Persiann']
print(languages)
print(languages[2])
print(languages[3].title())
print(languages[-1].lower())
message ="After, I learned " + languages[1] + "," + " I am planning to learn " + languages[3] + "."
print(message)


languages[4] = 'Endonesian'
print(languages)
languages.insert(1,'Dutch')

print(languages)
languages.append('Swiss')
print(languages)

del languages[2]
print(languages)
popped_languages = languages.pop()
print(languages)
print(popped_languages)
print("The  last languages I learned was a " + popped_languages.upper() + ".")

languages.remove('Dutch')
print(languages)

mother_language = 'Turkish'
languages.remove(mother_language)
print(languages)
print("\nA " + mother_language.upper()+ " is my mother language.")
print("\nHere is the sorted list:")
print(sorted(languages))
print("\nHere is the original list:")
print(languages)
print("\nHere is the reverse alphabetical order with sorted function")
print(sorted(languages, reverse=True))
languages.reverse()
print(languages)
languages.reverse()
print(languages)
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
