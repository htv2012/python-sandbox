class Car(object):
    def __del__(self):
        print("Goodbye")


print("Hello")
c = Car()
print("Exiting")
