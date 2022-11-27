# -*- coding: utf-8 -*-
def commercial():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    max(stats.values())
    for k, v in stats.items():
      if v == max(stats.values()):
        return k

if __name__ == '__main__':
    print(commercial())
