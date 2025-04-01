from bs4 import BeautifulSoup

import requests

url = "http://www.hdwallpapers.in"
html = requests.get(url)
soup = BeautifulSoup(html.text)

# categories = (
#     "Nature",
#     "Animals & Birds",
#     "Beach",
#     "Bikes",
#     "Cars",
#     "Dreamy & Fantasy",
#     "Others",
#     "Travel & World")
# random_category = random.randint(0, len(categories)) - 1
# selected_category = categories[random_category]
# selected_category_url = soup.find('a', text=selected_category)

# category_page_url_join = urlparse.urljoin(url, selected_category_url['href'])
# print 'category_page_url_join:', category_page_url_join
# category_page_html = requests.get(category_page_url_join)
# print 'category_page_html:', category_page_html


# for cat in categories:
#     print '---'
#     a_node = soup.find('a', text=cat)
#     print 'Category:', cat
#     print a_node
#     newurl = urlparse.urljoin(url, a_node['href'])
#     print 'URL:', newurl

# List of categories:
category = dict(
    (a.text, a["href"]) for a in soup.find_all("a") if "wallpapers.html" in a["href"]
)

# pprint(cat)
longest = max(len(k) for k in category)
for i in sorted(category):
    print("{:<{w}}: {}".format(i, category[i], w=longest))
