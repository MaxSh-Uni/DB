@echo off
set BASE_DIR=D:\DB\data
set MONGO_BIN="C:\Program Files\MongoDB\Server\8.2\bin\mongod.exe"
set MONGOS_BIN="C:\Program Files\MongoDB\Server\8.2\bin\mongos.exe"

start "Config Server" cmd /k %MONGO_BIN% --configsvr --replSet configRS --port 27019 --dbpath %BASE_DIR%\config --bind_ip 127.0.0.1

timeout /t 3

start "Shard1 Primary" cmd /k %MONGO_BIN% --shardsvr --replSet shard1RS --port 27020 --dbpath %BASE_DIR%\s1_rs1 --bind_ip 127.0.0.1

start "Shard1 Secondary" cmd /k %MONGO_BIN% --shardsvr --replSet shard1RS --port 27022 --dbpath %BASE_DIR%\s1_rs2 --bind_ip 127.0.0.1

timeout /t 3

start "Shard2 Primary" cmd /k %MONGO_BIN% --shardsvr --replSet shard2RS --port 27021 --dbpath %BASE_DIR%\s2_rs1 --bind_ip 127.0.0.1

start "Shard2 Secondary" cmd /k %MONGO_BIN% --shardsvr --replSet shard2RS --port 27023 --dbpath %BASE_DIR%\s2_rs2 --bind_ip 127.0.0.1

timeout /t 3

start "Mongos Router" cmd /k %MONGOS_BIN% --configdb configRS/localhost:27019 --port 27017 --bind_ip 127.0.0.1

echo.
echo All MongoDB servers started.
pause