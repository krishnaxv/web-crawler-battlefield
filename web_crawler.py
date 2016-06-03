from bs4 import BeautifulSoup

html_doc = '''
  <!DOCTYPE html>
  <html lang="en">
        <head>
      <meta charset="utf-8" />
      <title>HTML Document</title>
    </head>
    <body>
      <main class="main__container">
        <header id="header__primary">
          <h1 class="header__heading--blue">Heading of the Document</h1>
          <p>Description of the Document</p>
        </header>
        <section>
          <a href="https://google.com" class="company">Google</a>
          <a href="https://teslamotors.com" class="company">Tesla Motors</a>
        </section>
        <section>
          <img src="image_1.jpg" title="Image 1" />
          <img src="image_2.jpg" title="Image 2" />
        </section>
        <footer>
          <p>This is the footer of the Document.</p>
        </footer>
      </main>
    </body>
  </html>
'''

# Create `BeautifulSoup` object
soup = BeautifulSoup(html_doc, 'lxml')

# Pretty print
print soup.prettify()

print soup.title
print soup.title.name
print soup.title.string
print soup.title.parent.name
print soup.find_all('p')
print soup.find_all('a')
print soup.find_all('img')

# Get all links
for link in soup.find_all('a'):
    print link.get('href')

# Get all images
for image in soup.find_all('img'):
    print image.get('src')

# Get tag by Id
header = soup.find(id='header__primary')
print header
print header.p.string

# Search for a string
print soup.find(string='Google')

# Find all parents
print header.find_parents()

# Display all parents of `header`
for parent in header.find_parents():
    print parent.name

# Find immediate parent
print header.find_parent('body')

# find_next_siblings()
print header.find_next_siblings()

# find_next_sibling()
print header.find_next_sibling()

# find_previous_siblings()
print header.find_previous_siblings()

# find_previous_sibling()
print header.find_previous_sibling()

# Find all elements with `company` class
print soup.find_all('a', { "class": "company" })
print soup.find_all('a', class_='company')

# CSS Selectors
print soup.select_one('title')

# soup.select('head > title')
# soup.select('p > a')
# soup.select('p > a:nth-of-type(2)')
# soup.select('.class-name')
# soup.select('[class~="class-name"]')
# soup.select('#link1')
# soup.select('a[href]')

# Extract all the text
# print soup.get_text()
