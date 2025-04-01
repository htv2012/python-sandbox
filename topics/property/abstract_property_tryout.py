# Goal: define a base class, which force derrived classes to implement
# a certain property

import abc  # abstract base class


class BaseRecipe(object, metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def time_to_cook(self):
        pass


class SoupRecipe(BaseRecipe):
    @property
    def time_to_cook(self):
        return self._time_to_cook

    @time_to_cook.setter
    def time_to_cook(self, value):
        self._time_to_cook = value


recipe = SoupRecipe()
recipe.time_to_cook = 5
print(recipe.time_to_cook)
