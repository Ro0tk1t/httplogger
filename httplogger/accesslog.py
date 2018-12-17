#!/usr/bin/env python
# coding=utf-8

import re
from io import TextIOWrapper
import six

PY3 = six.PY3
if PY3:
    from urllib import parse
else:
    import urlparse as parse


time_reg = re.compile('\[(.*?)\]')
reg = re.compile('"(.*?)"')

class LOGS():
    def __init__(self, fileobj):
        if PY3:
            assert isinstance(fileobj, TextIOWrapper)
        else:
            assert isinstance(fileobj, file)
        #assert fileobj.readable()
        assert 'r' in fileobj.mode
        self.logs = [ACCESS(text.strip()) for text in fileobj if text.strip()]

    def __repr__(self):
        return '<HTTPAccessLogsObj>   len: %s   at address %s'%(len(self.logs), hex(id(self)))


class ACCESS():
    def __init__(self, text):
        '''
        input such as:
        172.17.0.1 - - [03/Nov/2018:02:50:02 +0000] "GET /vulnerabilities/sqli_blind/?id=2&Submit=Submit HTTP/1.1" 200 1765 "http://127.0.0.1:8001/vulnerabilities/sqli_blind/?id=1&Submit=Submit" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

        self.remote_ip -> 172.17.0.1
        self.visit_time -> 03/Nov/2018:02:50:02 +0000
        self.method -> GET
        self.http_type -> HTTP/1.1
        self.req_addr -> /vulnerabilities/sqli_blind/?id=2&Submit=Submit
        self.code -> 200
        self.res_len -> 1765
        self.referer -> http://127.0.0.1:8001/vulnerabilities/sqli_blind/?id=1&Submit=Submit
        '''
        ip, _ = text.split(' - - ')
        self.remote_ip = ip
        v_time = re.search(time_reg, _).group()
        self.visit_time = v_time.strip('[]')
        _ = _.split(v_time)[1].strip()
        req, referer, ua = re.findall(reg, _)
        req_sp = req.split(' ')
        self.method = req_sp[0]
        self.http_type = req_sp[-1]
        self.req_addr = req.lstrip(self.method).rstrip(self.http_type).strip()
        self.req_addr_unquote = parse.unquote(self.req_addr)
        self.referer = referer
        self.ua = ua
        _ = _[len(req)+3:]
        __ = _.split(' ')
        code, length = __[0], __[1]
        self.code = code
        self.res_len = length

    def __repr__(self):
        return '<AccessLogObj> code: %s    at address %s'%(self.code, hex(id(self)))

    @property
    def RemoteIP(self):
        return self.remote_ip

    @property
    def VisitTime(self):
        return self.visit_time

    @property
    def Method(self):
        return self.method

    @property
    def ReqAddr(self):
        return self.req_addr

    @property
    def Code(self):
        return self.code

    @property
    def ResLen(self):
        return self.res_len

    @property
    def Referer(self):
        return self.referer

    @property
    def UA(self):
        return self.ua
