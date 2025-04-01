from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("hello", "templates"))
template = env.get_template("index.html")
print(template)
print(template.render(name="World"))
