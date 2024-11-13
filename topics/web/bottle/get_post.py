from bottle import route, run, template, get, post, request


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == 'foo' and password == 'bar':
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

run(host='0.0.0.0', port=8080, debug=True)
