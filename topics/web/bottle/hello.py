from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello</b> {{name}}', name=name)

run(host='0.0.0.0', port=8080, debug=True)
