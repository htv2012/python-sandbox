# try out: class method


class Demo(object):
    @classmethod
    def get_random_string(cls):
        return "yabadabadoo"

    def greeting(self):
        return self.get_random_string()


d = Demo()
print(d.greeting())
