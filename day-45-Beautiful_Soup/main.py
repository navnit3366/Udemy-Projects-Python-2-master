from bs4 import BeautifulSoup

with open("website.html") as web_file:
    contents = web_file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.string)

# Getting the first tag of the specified element
print(soup.a)

# Getting all tags of the specified elements (as a list)
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# Getting text inside tags
for tag in all_anchor_tags:
    print(tag.getText())

# Getting the value of an attribute of an element
for tag in all_anchor_tags:
    print(tag.get('href'))

# Finding an element by id
print(soup.find(name="h1", id="name"))
# Same thing but by class
print(soup.find(name="h3", class_="heading"))

# Getting parts of the html code with CSS selectors
# Here we are getting an 'a' inside a 'p' tag
print(soup.select_one(selector="p a"))

