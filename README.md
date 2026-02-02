# POSTGRES AND MONGDB

Hello! This project initiates an introduction and demonstrates a basic ETL pipeline using **Airflow**, **MongoDB**, and **PostgreSQL** running in Docker.  
## Runs and Execution

To start the App, run the following command after git clone

```bash
$ docker compose up --build 
```
##  ElasticSearch Activation

You can navigate to the Dockerfiles to start the cluster

```bash
$ docker-compose up --build
```

I have already added the mock data in the data-node but just in case you have new data(with arrays of objects),first run the file convert.py and name it mocks_es_format.json
After the docker-compose is up you should check the health status in the terminal and see the result in a browser extn

 ```bash
{
  [+] Running 24/24
 ✔ postgres Pulled                                                                                                                         133.3s
   ✔ 6e449ec89832 Pull complete                                                                                                              0.5s
   ✔ 8721b06a7eca Pull complete                                                                                                              0.7s
   ✔ 84f86f655a30 Pull complete                                                                                                              1.0s
   ✔ aa732be6e8c4 Pull complete                                                                                                             69.6s
   ✔ 119d43eec815 Pull complete                                                                                                             69.4s
   ✔ 0f7dd3f0f295 Pull complete                                                                                                              1.1s
   ✔ 1aec77daa624 Pull complete                                                                                                             70.1s
   ✔ 38605c048c10 Pull complete                                                                                                              1.3s
   ✔ 1bf67474c634 Pull complete                                                                                                             70.2s
   ✔ 8081da2e1e86 Pull complete                                                                                                              1.2s
   ✔ de996ff323f4 Pull complete                                                                                                              1.3s
   ✔ 2967a6781cea Pull complete                                                                                                             69.7s
   ✔ 0bfc5429d86c Pull complete                                                                                                              2.0s
   ✔ b47cf7661373 Pull complete                                                                                                            130.5s
 ✔ mongodb Pulled                                                                                                                          176.9s
   ✔ fc530503d63a Pull complete                                                                                                              0.5s
   ✔ 49725ac362ad Pull complete                                                                                                             42.9s
   ✔ 7407b56680a9 Pull complete                                                                                                              1.5s
   ✔ b189090aa38f Pull complete                                                                                                              0.8s
   ✔ c9863ceddd80 Pull complete                                                                                                             42.8s
   ✔ 053a896a950f Pull complete                                                                                                              3.1s
   ✔ 31ab68bcb301 Pull complete                                                                                                            174.3s
   ✔ 6f4ebca3e823 Pull complete                                                                                                             42.6s
[+] Building 173.5s (21/21) FINISHED

}
```
After you are certain the network is health you should start the flask app framework 

 ```bash
python app1.py
```
This app will automatically connect to the ES Single-cluster using the credentials aforementioned already inside 
You should be getting 
```bash
+] Running 9/9
 ✔ nigga-airflow               Built                                                                                                         0.0s
 ✔ nigga-app                   Built                                                                                                         0.0s
 ✔ Network nigga_default       Created                                                                                                       0.0s
 ✔ Volume nigga_mongo_data     Created                                                                                                       0.0s
 ✔ Volume nigga_postgres_data  Created                                                                                                       0.0s
 ✔ Container postgres          Created                                                                                                       0.3s
 ✔ Container mongo             Created                                                                                                       0.3s
 ✔ Container airflow           Created                                                                                                       0.2s
 ✔ Container nigga-app-1       Created                                                                                                       0.2s
Attaching to airflow, mongo, app-1, postgres
postgres  | The files belonging to this database system will be owned by user "postgres".
postgres  | This user must also own the server process.
postgres  |
postgres  | The database cluster will be initialized with locale "en_US.utf8".
postgres  | The default database encoding has accordingly been set to "UTF8".
postgres  | The default text search configuration will be set to "english".
postgres  |
postgres  | Data page checksums are disabled.
postgres  |
postgres  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
postgres  | creating subdirectories ... ok
postgres  | selecting dynamic shared memory implementation ... posix
postgres  | selecting default max_connections ... 100
postgres  | selecting default shared_buffers ... 128MB
postgres  | selecting default time zone ... Etc/UTC
postgres  | creating configuration files ... ok
postgres  | running bootstrap script ... ok
mongo     | {"t":{"$date":"2026-01-24T12:42:43.859+00:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS
 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
mongo     | {"t":{"$date":"2026-01-24T12:42:43.860+00:00"},"s":"I",  "c":"NETWORK",  "id":4915701, "ctx":"main","msg":"Initialized wire specificat
ion","attr":{"spec":{"incomingExternalClient":{"minWireVersion":0,"maxWireVersion":21},"incomingInternalClient":{"minWireVersion":0,"maxWireVersio
n":21},"outgoing":{"minWireVersion":6,"maxWireVersion":21},"isInternalClient":true}}}
mongo     | {"t":{"$date":"2026-01-24T12:42:43.865+00:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unava
ilable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
mongo     | {"t":{"$date":"2026-01-24T12:42:43.872+00:00"},"s":"I",  "c":"REPL",     "id":5123008, "ctx":"main","msg":"Successfully registered Pri
maryOnlyService","attr":{"service":"TenantMigrationDonorService","namespace":"config.tenantMigrationDonors"}}
mongo     | {"t":{"$date":"2026-01-24T12:42:43.872+00:00"},"s":"I",  "c":"REPL",     "id":5123008, "ctx":"main","msg":"Successfully registered Pri
maryOnlyService","attr":{"service":"TenantMigrationRecipientService","namespace":"config.tenantMigrationRecipients"}}
mongo     | {"t":{"$date":"2026-01-24T12:42:43.872+00:00"},"s":"I",  "c":"CONTROL",  "id":5945603, "ctx":"main","msg":"Multi threading initialized
"}
mongo     | {"t":{"$date":"2026-01-24T12:42:43.873+00:00"},"s":"I",  "c":"TENANT_M", "id":7091600, "ctx":"main","msg":"Starting TenantMigrationAcc
essBlockerRegistry"}

```

## MongoDb data
```bash
docker exec -it mongo mongosh
Current Mongosh Log ID: 6974cbed36f6ad0ec88ce5af
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.6.0
Using MongoDB:          7.0.28
Using Mongosh:          2.6.0

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2026-01-24T13:30:18.568+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2026-01-24T13:30:19.990+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2026-01-24T13:30:19.991+00:00: For customers running MongoDB 7.0, we suggest changing the contents of the following sysfsFile
   2026-01-24T13:30:19.993+00:00: vm.max_map_count is too low
------

test> use iot
switched to db iot

```

## Data gEN should 

```bash
 db.air_quality.find().pretty()
[
  {
    _id: ObjectId('6974c08de9af603beaabd481'),
    timestamp: ISODate('2026-01-24T12:52:29.684Z'),
    temperature: 27.56,
    humidity: 51.06,
    pm25: 56.31
  },
  {
    _id: ObjectId('6974c093e9af603beaabd482'),
    timestamp: ISODate('2026-01-24T12:52:35.266Z'),
    temperature: 27.22,
    humidity: 44.22,
    pm25: 64.67
  },
  {
    _id: ObjectId('6974c098e9af603beaabd483'),
    timestamp: ISODate('2026-01-24T12:52:40.268Z'),
    temperature: 22.72,
    humidity: 58.78,
    pm25: 47.61
  },
  {
    _id: ObjectId('6974c09de9af603beaabd484'),
    timestamp: ISODate('2026-01-24T12:52:45.269Z'),
    temperature: 22.16,
    humidity: 45.04,
    pm25: 37.56
  },
  {
    _id: ObjectId('6974c0a2e9af603beaabd485'),
    timestamp: ISODate('2026-01-24T12:52:50.271Z'),
    temperature: 21.78,
    humidity: 35.88,
    pm25: 77.33
  },
  {
    _id: ObjectId('6974c0a7e9af603beaabd486'),
    timestamp: ISODate('2026-01-24T12:52:55.271Z'),
    temperature: 17.93,
    humidity: 63.57,
    pm25: 24.78
  },
  {
    _id: ObjectId('6974c0ace9af603beaabd487'),
    timestamp: ISODate('2026-01-24T12:53:00.272Z'),
    temperature: 28.74,
    humidity: 53.19,
    pm25: 76.89
  },
  {
    _id: ObjectId('6974c0b1e9af603beaabd488'),
    timestamp: ISODate('2026-01-24T12:53:05.273Z'),
    temperature: 20.27,
    humidity: 73.42,
    pm25: 23.42
  },
  {
    _id: ObjectId('6974c0b6e9af603beaabd489'),
    timestamp: ISODate('2026-01-24T12:53:10.275Z'),
    temperature: 22.57,
    humidity: 47.33,
    pm25: 34.33
  },
  {
    _id: ObjectId('6974c0bbe9af603beaabd48a'),
    timestamp: ISODate('2026-01-24T12:53:15.276Z'),
    temperature: 17.11,
    humidity: 36.29,
    pm25: 59.16
  },

```
## Interaction:Airflow Dag
There are two ways to interact with this database ,through the index on address http://127.0.0.1:5000 with a landing page like this 

for db
![image](https://github.com/E-creator513/EL-process8/blob/master/OTW.png)

And to check if data is added its 
![image](https://github.com/E-creator513/EL-process8/blob/master/otw2.png)

 
## Terminal
Through the git-bash terminal with these commands 
### Searching 

for example the word Editor.js
```bash
curl -X GET "http://localhost:5000/search?querystring=Editor.js" -H "Content-Type: application/json"
```
you should be getting the result like 

```bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1856  100  1856    0     0   6642      0 --:--:-- --:--:-- --:--:--  6652{
  "documents": [
    {
      "fieldContent": "You can destroy an Editor.js instance by calling the `destroy` method.",
      "fieldName": "content",
      "id": "29"
    },
    {
      "fieldContent": "You can destroy an Editor.js instance by calling the `destroy` method.",
      "fieldName": "content",
      "id": "hmtni5IB-CXDxQLHAUBM"
    },
    {
      "fieldContent": "You can destroy an Editor.js instance by calling the `destroy` method.",
      "fieldName": "content",
      "id": "rmtxi5IB-CXDxQLHgEBl"
    },
    {
      "fieldContent": "You can destroy an Editor.js instance by calling the `destroy` method.",
      "fieldName": "content",
      "id": "1Wtzi5IB-CXDxQLH6EDn"
    },
    {
      "fieldContent": "In this guide, we will learn how to interact with the Editor.js API.",
      "fieldName": "content",
      "id": "37"
    },
    {
      "fieldContent": "In this guide, we will learn how to interact with the Editor.js API.",
      "fieldName": "content",
      "id": "jmtni5IB-CXDxQLHAkD1"
    },
    {
      "fieldContent": "In this guide, we will learn how to interact with the Editor.js API.",
      "fieldName": "content",
      "id": "tmtxi5IB-CXDxQLHgkCw"
    },
    {
      "fieldContent": "In this guide, we will learn how to interact with the Editor.js API.",
      "fieldName": "content",
      "id": "3Wtzi5IB-CXDxQLH6kBA"
    },
    {
      "fieldContent": "Since version 2.18, Editor.js provides an API for internationalization (i18n) that allows localizing all UI texts of the editor's core and plugins.",
      "fieldName": "content",
      "id": "30"
    },
    {
      "fieldContent": "Since version 2.18, Editor.js provides an API for internationalization (i18n) that allows localizing all UI texts of the editor's core and plugins.",
      "fieldName": "content",
      "id": "h2tni5IB-CXDxQLHAUB1"
    }
  ]
}
```
## Airflow dags data 
```bash
 docker exec -it airflow bash
airflow@8524d435c2cd:/opt/airflow$ ls /opt/airflow/dags
airflow@8524d435c2cd:/opt/airflow$ ls /opt/airflow/dags

```

The result should be 

```bash
        timestamp        | temperature | humidity | pm25
-------------------------+-------------+----------+-------
 2026-01-24 12:52:29.684 |       27.56 |    51.06 | 56.31
 2026-01-24 12:52:35.266 |       27.22 |    44.22 | 64.67
 2026-01-24 12:52:40.268 |       22.72 |    58.78 | 47.61
 2026-01-24 12:52:45.269 |       22.16 |    45.04 | 37.56
 2026-01-24 12:52:50.271 |       21.78 |    35.88 | 77.33
 2026-01-24 12:52:55.271 |       17.93 |    63.57 | 24.78
 2026-01-24 12:53:00.272 |       28.74 |    53.19 | 76.89
 2026-01-24 12:53:05.273 |       20.27 |    73.42 | 23.42
 2026-01-24 12:53:10.275 |       22.57 |    47.33 | 34.33
 2026-01-24 12:53:15.276 |       17.11 |    36.29 | 59.16
 2026-01-24 12:53:20.277 |       27.91 |    68.27 | 91.56
 2026-01-24 12:53:25.27  |       28.77 |    40.07 | 83.22
 2026-01-24 12:53:30.271 |       19.56 |    32.63 | 90.88
 2026-01-24 12:53:35.272 |       18.77 |    58.89 | 47.66
 2026-01-24 12:53:40.274 |       18.66 |    36.23 | 49.74
 2026-01-24 12:53:45.275 |        15.4 |    37.97 | 31.33
 2026-01-24 12:53:50.277 |       22.34 |    54.81 | 76.57
 2026-01-24 12:53:55.283 |       29.34 |    37.39 |  37.3
 2026-01-24 12:54:00.284 |       23.68 |    69.93 | 34.25
 2026-01-24 12:54:05.285 |       25.29 |    53.88 | 39.25
 2026-01-24 12:54:10.287 |        25.3 |       55 | 64.68
 2026-01-24 12:54:15.288 |        20.5 |    60.02 |  93.6
 2026-01-24 12:54:20.289 |       23.22 |    39.44 | 51.28
 2026-01-24 12:54:25.291 |       25.73 |    63.88 | 91.84
 2026-01-24 12:54:30.292 |        15.7 |    49.94 | 70.38
 2026-01-24 12:54:35.293 |       27.39 |    75.98 | 34.09
 2026-01-24 12:54:40.294 |       29.36 |     51.1 | 23.12
 2026-01-24 12:54:45.296 |       19.44 |    50.27 |  5.21
 2026-01-24 12:54:50.297 |       18.72 |    68.47 | 56.38
 2026-01-24 12:54:55.298 |       28.75 |    58.19 | 40.33
 2026-01-24 12:55:00.299 |       22.44 |    51.39 |  68.9
 2026-01-24 12:55:05.3   |       22.12 |     63.7 | 89.12
 2026-01-24 12:55:10.302 |       23.71 |    36.41 | 89.01
 2026-01-24 12:55:15.307 |       25.11 |    56.94 | 38.45

```


