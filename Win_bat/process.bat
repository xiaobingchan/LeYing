@echo off
wmic process where name="sqlservr.exe" delete
wmic process where name="sqlwriter.exe" delete
::wmic process call create sqlservr.exe
::wmic process call create sqlwriter.exe
wmic process where name="oracle.exe" delete
wmic process where name="java.exe" delete
wmic process where name="mongo.exe" delete
wmic process where name="mongod.exe" delete
wmic process where name="perl.exe" delete
wmic process where name="java.exe" delete
wmic process where name="memcached.exe" delete
wmic process where name="redis-server.exe" delete
wmic process where name="erl.exe" delete

::