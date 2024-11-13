import abc


class LanguageBase(abc.ABC):
    @abc.abstractmethod
    def greet(name):
        """Say hello to name"""
        pass


class French(LanguageBase):
    def greet(self, name):
        print("Bonjour {}".format(name))


class German(LanguageBase):
    pass


def main():
    """Entry"""
    french = French()
    french.greet("Francois")

    # Error: need to implement the "greet" method
    german = German()


if __name__ == "__main__":
    main()
