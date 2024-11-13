import os
import logging

import tiny


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug('__file__=%r', __file__)
dbfile = __file__.replace('.py', '.sqlite')
mytiny = tiny.Tiny(dbfile)

# ======================================================================
# Tests
# ======================================================================

def test_dbfile_must_exists():
    assert os.path.exists(dbfile), \
            "Missing {!r} needed for the tests".format(dbfile)

# ======================================================================

def test_find_existing_token():
    token = '2pBm3K'
    result = mytiny.find_by_token(token)

    assert result['status'] == 'OK'
    assert result['token'] ==  token
    assert result['url'] ==  'https://pinboard.in/u:htv2017/t:book'

def test_find_non_existing_token():
    token = 'yabadabadoo'
    result = mytiny.find_by_token(token)
    assert result['status'] == 'not found'
    assert result['token'] ==  token
    assert result['url'] ==  ''

# ======================================================================

def test_find_existing_url():
    url = 'https://pinboard.in/u:htv2017/t:book'
    result = mytiny.find_by_url(url)
    assert result['status'] == 'OK'
    assert result['url'] == url
    assert result['token'] == '2pBm3K'

def test_find_non_existing_url():
    url = 'foobar'
    result = mytiny.find_by_url(url)
    assert result['status'] == 'not found'
    assert result['url'] == url
    assert result['token'] == ''

# ======================================================================
def test_list():
    result = mytiny.list_all()

    assert result['status'] == 'OK'
    assert len(result['entries']) == 4

    entry0 = dict(url='http://southeastwind.net/karaoke', token='kara')
    assert result['entries'][0] == entry0

    entry1 = dict(url='http://45.33.63.153:8888/tree', token='notebooks')
    assert result['entries'][1] == entry1

    entry2 = dict(url='https://pinboard.in/u:htv2017/t:book', token='2pBm3K')
    assert result['entries'][2] == entry2

    entry3 = dict(url='https://pinboard.in/u:htv2017', token='pirqAm')
    assert result['entries'][3] == entry3
