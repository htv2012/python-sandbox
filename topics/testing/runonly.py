# ======================================================================
# TODO: Delete before reviewing
def run_only(*patterns):
    def remove_all_but_this_test(cls):
        for name in dir(cls):
            if name.startswith('test_') and not any(p in name for p in patterns):
                delattr(cls, name)
        return cls
    return remove_all_but_this_test
@run_only('$END$')
# ======================================================================
