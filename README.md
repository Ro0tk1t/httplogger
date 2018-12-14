A Simple package to parse apache‘s access.log
-----------------------------------------------------------

* How to install

` make install `



* How to use
```
In [1]: import accesslog

In [2]: f = open('access.log')

In [3]: a = accesslog.LOGS(f)

In [4]: a
Out[4]: <HTTPAccessLogsObj>   len: 513   at address 0x7f44f85bfb70

In [5]: a.logs[:5]
Out[5]: 
[<AccessLogObj> code: 200    at address 0x7f44f85bfe10,
 <AccessLogObj> code: 200    at address 0x7f44f85b2208,
 <AccessLogObj> code: 200    at address 0x7f44f85b2e48,
 <AccessLogObj> code: 404    at address 0x7f44f85b2f98,
 <AccessLogObj> code: 404    at address 0x7f44f85b2828]
 
In [6]: a.logs[0].remote_ip
Out[6]: '172.17.0.1'

In [7]: a.logs[0].req_addr
Out[7]: '/vulnerabilities/sqli_blind/?id=2&Submit=Submit'

In [8]: a.logs[0].req_addr_unquote
Out[8]: '/vulnerabilities/sqli_blind/?id=2&Submit=Submit'

In [9]: a.logs[0].get_code()
Out[9]: '200'

```
