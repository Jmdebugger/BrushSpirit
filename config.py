#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
URL_ACTION_SENDDATA = "http://app.50bang.org/?action=sendData"
URL_TONGJI_MODULE_SENDDATA = "http://app.50bang.org/tongji_module/?_c=log&action=sendData"
URL_TONGJI_MODULE_SESSION = "http://app.50bang.org/tongji_module/?_c=log&action=session"
URL_GET_LIST_FOR_ANDROID = "http://shouji.2345.com/api/getlist4android.php"


SOFTWARE_NAME = u"刷分精灵"

current_dir = os.getcwd()
db_dir = current_dir + u"\\db\\"
if not os.path.exists(db_dir):
    os.makedirs(db_dir)





if __name__ == "__main__":
    print db_dir