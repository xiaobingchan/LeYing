#!/bin/sh
#date:2018-04-09 15:35:11
#author:chengengcong
#company:NanWangZongBu
#version:1.0.1
#file: os_linux_check_001.sh
#Description: the linuc check...
/usr/local/nginx/sbin/nginx # 启动Nginx进程
/usr/local/php/sbin/php-fpm #  php版本信息：http://192.168.56.1/test.php
systemctl start zabbix-server # zabbix后台：http://192.168.56.1/zabbix ；账号：Admin , 密码：zabbix

