@echo off
set PRIMARY_DB=D:\DB\data\rs1
set SECONDARY_DB=D:\DB\data\rs2
set MONGO_BIN="C:\Program Files\MongoDB\Server\8.2\bin\mongod.exe"

start "MongoDB Primary" cmd /k %MONGO_BIN% --port 27017 --dbpath %PRIMARY_DB% --replSet rs0 --bind_ip 127.0.0.1
timeout /t 3
start "MongoDB Secondary" cmd /k %MONGO_BIN% --port 27018 --dbpath %SECONDARY_DB% --replSet rs0 --bind_ip 127.0.0.1

pause