import logging
import os
import json


from bottle import route, run, template, get, post, request


logging.basicConfig(
    level=os.getenv('LOGLEVEL', logging.DEBUG))
logger = logging.getLogger(__name__)


html = """
<form action="/" method="POST">

  <button type="submit">Submit Form</button>

</form>
"""


@get('/')
def index():
    return open('setup-server.html').read()

@post('/')
def run_app():
    logger.debug('Posting, forms=%r', request.forms)
    args = ['{}={}'.format(k, v) for k, v in request.forms.items() if v]
    for k, v in request.forms.items():
        logger.debug('%s=%r', k, v)
    logger.debug('Args=%r', args)
    # logger.debug('Forms:\n%s', json.dumps(request.forms, sort_keys=True, indent=4))
    return 'Goodbye'

run(host='0.0.0.0', port=8080, debug=True)
