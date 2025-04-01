import os

from jinja2 import Environment, FileSystemLoader

here = os.path.dirname(__file__)
templates_dir = os.path.join(here, "hello", "templates")
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template("index.html")
print(template)
print(template.render(name="World"))
