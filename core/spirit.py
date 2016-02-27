#!/usr/bin/python
# -*- coding:utf-8 -*-
import config
import os
import threading
from util import sync
try:
    import cPickle as pickle
except ImportError:
    import pickle



class Tech:
    def __init__(self ,tid):
        self.tid = tid
        self.phones = {}
    def onfire(self):
        pass
    def onhire(self):
        pass
    def onwork(self):
        pass
    def onfree(self):
        pass



class Boss(object):
    def __init__(self , name):
        self.name = name
        self.techs = {}

    def hire(self ,tech):
        """
        :param tech: the tech who will be hired
        :return:if the tech is not exist then return tech,else return None
        """
        if self.techs.has_key(tech.tid):
            return None
        self.techs[tech.tid] = tech
        tech.onhire()
        tech.onwork()
        return tech

    def fire(self ,tid):
        """
        :param tid: tid of tech
        :return: if tech who`s tid is tid is exist then return tech
        """
        if self.techs.has_key(tid):
            tech = self.techs.pop(tid)
            tech.onfire()
            tech.onfree()
            return tech
        return None

    def onwork(self):
        for tech in self.techs.values():
            tech.onwork()

    def onfree(self):
        for tech in self.techs.values():
            tech.onfree()


__boss = None
__boss_name = u"boss"
__boss_file = config.db_dir + __boss_name + u".db"
__boss_lock = threading.Lock()

@sync(__boss_lock)
def loadBoss():
    global  __boss
    if __boss is None:
        if os.path.exists(__boss_file):
            with open(__boss_file , "rb") as f:
                __boss  = pickle.load(f)
        else:
            __boss = Boss(__boss_name)
        __boss.onwork()
    return __boss

@sync(__boss_lock)
def saveBoss():
    global __boss
    if __boss is None:
        return False
    __boss.onfree()
    with open(__boss_file , "wb") as f:
        pickle.dump(__boss , f)
    __boss = None
    return True











if __name__ == "__main__":
    loadBoss()
    saveBoss()
    loadBoss()


