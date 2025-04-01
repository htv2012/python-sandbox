import itertools


def get_views(client_json):
    views = []
    try:
        for number in itertools.count(0):
            view = client_json["View{}".format(number)].split()
            views.append(view)
    except KeyError:
        pass
    return views
