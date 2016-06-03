# Web Crawling

### Definition

> `Wikipedia` A Web crawler is an Internet bot which systematically browses the World Wide Web, typically for the purpose of Web indexing.

**What is web indexing?**

> `Wikipedia` Web indexing (or Internet indexing) refers to various methods for indexing the contents of a website or of the Internet as a whole.

**How to systematically browse the web?**

To understand this, let's understand, "What is Web?".

> `Wikipedia` Web is a collection of related web pages, including multimedia content, typically identified with a common domain name, and published on at least one web server.

### robots.txt

### Implementation

For web crawling, we are going to use two Python libraries/packages.

> 1. `Requests` Requests allows you to send HTTP requests, without the need for manual labor. Visit [http://docs.python-requests.org/en/latest/](http://docs.python-requests.org/en/latest/) for reference.
2. `Beautiful Soup` Beautiful Soup is a Python library for pulling data out of HTML and XML files. Visit [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for reference.

##### Working with `Requests`

```python
# Import packages
import requests

# Seed URL to crawl
seed_url = 'http://www.flipkart.com/search?q=mobiles&as=off&as-show=on&otracker=start'

# Get source code of seed URL
source_code = requests.get(seed_url)

# Read the content of server's response
html_doc = source_code.text
```

##### Working with `BeautifulSoup`

```python
# Import packages
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
        <header id="header--primary">
          <h1 class="header__heading--blue">Heading of the Document</h1>
          <p>Description of the Document</p>
        </header>
        <section>
          <a href="https://google.com">Google</a>
          <a href="https://teslamotors.com">Tela Motors</a>
        </section>
        <footer>
          <p>This is the footer of the Document.</p>
        </footer>
      </main>
    </body>
  </html>
'''

# Create `BeautifulSoup` object
soup = BeautifulSoup(html_doc, 'html.parser')

# Pretty print
print soup.prettify()
```

`soup` is a BeautifulSoup object, which represents the document as a nested data structure.

Let's navigate that data structure.

```python
# `<title>HTML Document</title>`
print soup.title

# `title`
print soup.title.name

# `HTML Document`
print soup.title.string

# `head`
print soup.title.parent.name

# `main__container`
print soup.main['class']

# <header id="header__primary">
#   <h1>Heading of the Document</h1>
#   <p>Description of the Document</p>
# </header>
print soup.find(id='header__primary')

# [<p>Description of the Document</p>, <p>This is the footer of the Document.</p>]
print soup.find_all('p', limit=2)

# Extract all `a` tags
# https://google.com
# https://teslamotors.com
for link in soup.find_all('a'):
  print link.get('href')

# Extract all the text from the page
print soup.get_text()
```

**HTML Parser for BeautifulSoup**

Beautiful Soup supports the HTML parser included in Python’s standard library, but it also supports a number of third-party Python parsers.

Following are the details of available HTML parsers.

Parser | Usage | Advantages/Disadvantages
------ | ----- | ----------
Python’s html.parser | BeautifulSoup(html_doc, 'html.parser') | Decent Speed
lxml’s HTML parser | BeautifulSoup(html_doc, 'lxml') | Fast, Lenient
lxml’s XML parser | BeautifulSoup(html_doc, 'lxml-xml'), BeautifulSoup(html_doc, 'xml') | Fast, The only currently supported XML parser
html5lib | BeautifulSoup(html_doc, 'html5lib') | Extremely lenient, Parses pages the same way a web browser does, Creates valid HTML5, Slow

`Recommendation` Use lxml for speed

##### Making Soup

To parse a document, you can pass in a string or an open file handle into the `BeautifulSoup` constructor.

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('index.html'))
soup = BeautifulSoup('<html>Document Data</html>')
```

##### Beautiful Soup Objects

Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. But, we'll deal with four kinds of objects:

1. Tag
2. NavigableString
3. BeautifulSoup
4. Comment

**Tag**

> A Tag object corresponds to an XML or HTML tag in the original document. Tags have attributes and methods.

Tags contains `name` & attributes (`attrs`).

```python
tag = soup.h1

# <class 'bs4.element.Tag'>
print type(tag)

# Every tag has name
# h1
print tag.name

# Tag may have any number of attributes & can be retrieved as dictionary with `.attrs`
# {u'class': [u'header__heading--blue']}
print tag.attrs

# Add attribute to tag
tag['id'] = 'heading--primary'

# Remove tag's attribute
del tag['id']

# KeyError: 'id'
print tag['id']

# None
print tag.get('id')
```

**NavigableString**

> Beautiful Soup uses the `NavigableString` class to contain string which corresponds to a bit of text within a tag.

```python
# Heading of the Document
print tag.string

# <class 'bs4.element.NavigableString'>
print type(tag.string)
```

**BeautifulSoup**

> The BeautifulSoup object represents the document as a whole. Since, the BeautifulSoup object doesn’t correspond to an actual HTML or XML tag, it has no name and no attribute & it has been given a special `.name`, `[document]`.

```python
# [document]
print soup.name
```

**Comment**

> The `Comment` object is just a special type of `NavigableString`.

```python
html_doc = '<strong><!--Hola! I am a comment.--></strong>'
soup = BeautifulSoup(html_doc, 'html.parser')
comment = soup.strong.string

# Hola! I am a comment.
print comment

# <class 'bs4.element.Comment'>
print type(comment)

# Comment is displayed with special formatting when it appears as part of HTML document
# <strong>
#  <!--Hola! I am a comment.-->
# </strong>
print soup.strong.prettify()
```

### CSS Selectors
