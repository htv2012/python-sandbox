import enum


class CaseInsensitiveName(enum.EnumType):
    def __getitem__(self, target):
        target = target.casefold()
        for key, member in self.__members__.items():
            if str(key).casefold() == target:
                return member

        raise KeyError(target)


class Environment(enum.Enum, metaclass=CaseInsensitiveName):
    TEST = enum.auto()
    PILOT = enum.auto()
    PROD = enum.auto()
