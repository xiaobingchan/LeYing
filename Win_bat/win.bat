@echo off

sc start null

net stop "DB2DAS00"
net stop "DB2REMOTECMD_DB2COPY1"
net stop "DB2MGMTSVC_DB2COPY1"
net stop "DB2-0"

net stop "postgresql-x64-10"

net stop "MSSQL$SQLEXPRESSLYJ"
net stop "SQLBrowser"
net stop "SQLWriter"

net stop "Oracle ORCL VSS Writer Service"
net stop "OracleOraDb11g_home1ClrAgent"
net stop "OracleServiceORCL"
net stop "OracleOraDb11g_home1TNSListener"

net stop "RabbitMQ"

net stop "Zabbix Agent"

mysqld.exe --install MySql --defaults-file="e:/phpStudy/PHPTutorial/MySQL/my.ini"
net stop mysql

for /f "skip=2 tokens=2 delims=," %%i in ('wmic os get FreePhysicalMemory /format:CSV') do (
set richparm2=%%i&goto e1)
:e1
set /a unit=1024
set /a result=%richparm2%/%unit%
echo {'FreePhysicalMemory':{'value':%result%,'unit':'MB','status':0}}


for /f "skip=2 tokens=2 delims=," %%i in ('wmic os get TotalVisibleMemorySize /format:CSV') do (
set richparm3=%%i&goto e2)
:e2
set /a unit=1024
set /a result2=%richparm3%/%unit%
echo {'TotalVisibleMemorySize':{'value':%result2%,'unit':'MB','status':0}}

if %result2% geq 1000 (echo TotalVisibleMemorySize greater or equal 1000)