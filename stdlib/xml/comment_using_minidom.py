#!/usr/bin/env python

from xml.dom import minidom

d = minidom.parseString('<Books/>')
root = d.documentElement

#
# Create the first book
#

comment = d.createComment('The Divergent Series, book 1')
root.appendChild(comment)

book = d.createElement('Book')
book.setAttribute('isbn', '9780062024039')
root.appendChild(book)

title = d.createElement('Title')
text = d.createTextNode('Divergent')
title.appendChild(text)
book.appendChild(title)

author = d.createElement('Author')
text = d.createTextNode('Veronica Roth')
author.appendChild(text)
book.appendChild(author)


#
# Create the second book
#

comment = d.createComment('The Divergent Series, book 2')
root.appendChild(comment)

book = d.createElement('Book')
book.setAttribute('isbn', '9780062024046')
root.appendChild(book)

title = d.createElement('Title')
text = d.createTextNode('Insurgent')
title.appendChild(text)
book.appendChild(title)

author = d.createElement('Author')
text = d.createTextNode('Veronica Roth')
author.appendChild(text)
book.appendChild(author)

#
# Create the third book
#

comment = d.createComment('The Divergent Series, book 3')
root.appendChild(comment)

book = d.createElement('Book')
book.setAttribute('isbn', '9780062024060')
root.appendChild(book)

title = d.createElement('Title')
text = d.createTextNode('Allegiant')
title.appendChild(text)
book.appendChild(title)

author = d.createElement('Author')
text = d.createTextNode('Veronica Roth')
author.appendChild(text)
book.appendChild(author)

print(d.toprettyxml())
