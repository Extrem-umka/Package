# -*- coding: utf-8 -*-
def reoID():
   ids = {'user1': [213, 213, 213, 15, 213],
          'user2': [54, 54, 119, 119, 119],
          'user3': [213, 98, 98, 35]}
   val = set(sum(ids.values(), []))
   return val

if __name__ == '__main__':
    print(reoID())