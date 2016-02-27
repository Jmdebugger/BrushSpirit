#!/usr/bin/python
# -*- coding:utf-8 -*-
def sync(lock):
    def syncWithLock(fn):
        def newFn(*args,**kwargs):
            lock.acquire()
            try:
                return fn(*args,**kwargs)
            finally:
                lock.release()
        newFn.func_name = fn.func_name
        newFn.__doc__ = fn.__doc__
        return newFn
    return syncWithLock