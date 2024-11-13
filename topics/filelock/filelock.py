import multiprocessing

_locks = {}
dict_lock = multiprocessing.Lock()

def exclusive_access(filename):
    while True:
        with dict_lock:
            locked = _locks.get(filename)

        if locked is None:
            with dict_lock:
                locked = multiprocessing.Lock()
                _locks[filename] = locked
            break

        time.sleep(1)

    yield locked

    with dict_lock:
        _locks[filename].release()
