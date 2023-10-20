
a = "Samiur Rabbi Alex"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("x")) #remove the selected character
print(a.replace("Samiur", "Saimur"))
print(a.split(" "))
# print(a.split(" ")[1])
print(a.split(" ")[1][0])
print(a.split(" ")[1][0:2])
print(a.split(" ")[1][0:3])
print(a.split(" ")[1][0:4])
print(a.split(" ")[1][0:5])

#capitalization of sentence
b = "bangladesh army"
print(b.capitalize())

#add null characters
c = "I am Samiur Rabbi Alex"
print(len(c))
print(c.center(50))
print(len(c.center(50)))


#counting a word or characer numbers in a given string

c = 'Alex Samiur Rabbi Alex '
print(c.count("Alex"))



str1 = "Samiur Rabbi ?"
print(str1.endswith("?"))
print(str1.startswith("Samiur"))
print(str1.find("Rabbi"))

s1 = "Welcome34"
print(s1.isalnum())  #its scan alphanumeric numbe or not . Alpha numeric - A-Z, a-z, 0-9
print(s1.isalpha())  #scan only alpha A-Z,a-Z

a = "Alex"
print(a.islower())  # if all lower then it will print true
print(a.isupper())# if all capital then it will print true

b = "alex"
print(b.islower())

c = "Alex"
print(c.isupper())


d = "Samiur Rabbi Alex"
print(d.swapcase()) #upper to lower , lower to upper

s1 = "Alex0204"
print(s1.isdigit()) #scan only digits 0-9
print(s1.isspace()) #scan only space
print(s1.istitle()) #scan only title case
print(s1.isidentifier()) #scan only identifier
print(s1.isprintable()) #scan only printable character  

title = "Alex"
print(title.istitle())
print(title.title())
