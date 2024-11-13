import importlib


def from_module_import(module_name, names=None):
	# Import the module
	mod = importlib.import_module(module_name)

	# Determine a list of names to copy to the current name space
	if isinstance(names, str):
		names = [names]
	if names is None:
		names = getattr(mod, '__all__')
	if names is None:
		names = [n for n in dir(mod) if not n.startswith('_')]

	# Copy those names into the current name space
	g = globals()
	objects = []
	for name in names:
	    g[name] = getattr(mod, name)
	    objects.append(g[name])
	return objects

if __name__ == '__main__':
	names = from_module_import('collections', 'namedtuple')
	print(names)
	namedtuple  # Use it
