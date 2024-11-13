"""
Database layer
"""
import collections
import sqlite3
import random
import string


Shortener = collections.namedtuple('Shortener', ['token', 'url'])
_valid_chars = list(string.ascii_letters + string.digits)
random.shuffle(_valid_chars)


# Connect and create the table if needed
_conn = sqlite3.connect('short.db')
_conn.execute('create table if not exists short (token text, url text)')
_conn.commit()


def row_factory(cursor, row):
	return Shortener._make(row)


# Set the row factory to create a named tuple
_conn.row_factory = row_factory


# ======================================================================
# Tokens
# ======================================================================

def _query_all_tokens():
	query = 'select token from short'
	rows = _conn.execute(query)
	tokens = set(row[0] for row in rows)
	return tokens


def _create_token():
	token = random.choices(_valid_chars, k=4)
	token = ''.join(token)
	return token


# ======================================================================
# Shortener
# ======================================================================

def find(token):
	query = 'select * from short where token=?'
	rows = _conn.execute(query, (token,))
	found = next(rows, None)
	return found


def url_exists(url):
	query = 'select * from short where url=?'
	rows = _conn.execute(query, (url,))
	found = next(rows, None)
	return found is not None


def insert(url, token=None):
	if url_exists(url):
		raise ValueError(f'URL exists: {url!r}')

	if token is not None and find(token) is not None:
		raise ValueError(f'Token exists: {token!r}')

	if token is None:
		while True:
			token = _create_token()
			if find(token) is None:
				break

	_conn.execute('insert into short values (?, ?)', (token, url))
	_conn.commit()

	return token


# for i in range(10):
# 	print(_create_token())

# f = find('abc')
# print(f'Find(abc) ==> {f}')
# f = find('foo')
# print(f'Find(foo) ==> {f}')
# f = find('def')

# t = _query_all_tokens()
# print(t)

# text = 'text for def'
# tok = 'def'
# insert(text, tok)
