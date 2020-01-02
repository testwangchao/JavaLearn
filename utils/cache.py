import memcache

cache = memcache.Client(['127.0.0.1:11211'], debug=True)

def set(key, value, timeout=60):
    return cache.set(key, value, timeout)


def get(key):
    return cache.get(key)


def delete(key):
    return cache.delete(key)


if __name__ == '__main__':
    set("15201403874", "123456", timeout=1800)
    print(get('15201403874'))