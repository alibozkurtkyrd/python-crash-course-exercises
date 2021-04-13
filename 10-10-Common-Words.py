

filename = 'Thrilling stories.txt'

try:
    with open(filename, encoding = "ISO-8859-1") as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    msg = "Sorry, the file '" + filename + "' does not exist."
    print(msg)

else:
    a = contents.lower().count('the')
    print(a)

#sonuç internet sitesinde ctrl + f aracığıyla kontrol edildi sonuç doğrulandı sitede 4531 adet the buldunduğunu belirtti
    
    
