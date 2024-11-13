import foo


class JapaneseRestaurant:
    pass


class Bar(foo.Foo):
    pass


class CocktailBar(Bar):
    pass


class SeafoodBar(Bar):
    pass


class SushiBar(Bar, JapaneseRestaurant):
    pass


class Boo(foo.Foo):
    pass
