class BaseAPI:
    def __init_subclass__(cls, *, module, path, version=1, **kwargs):
        super.__init_subclass__(**kwargs)
        path = path.strip("/")
        cls.path = f"/api/{module}/v{version}/{path}"

    def __repr__(self):
        return f"{self.__class__.__name__}(path={self.path!r})"


def main():
    """Entry"""

    class EnvAPI(BaseAPI, module="adc", path="environments"):
        pass

    env_api = EnvAPI()
    print(f"env_api={env_api}")

    class RoleAPI(BaseAPI, module="platform", path="roles"):
        pass

    role_api = RoleAPI()
    print(f"role_api={role_api}")

    # What happens if we forgot to declare module and/or path
    try:

        class FooAPI(BaseAPI):
            pass
    except TypeError as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()
