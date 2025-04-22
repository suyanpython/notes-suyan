# MongoDB: 

> Scales horizontally pretty well, but write-heavy use cases may need careful setup.

>Read-heavy, flexible 

>Document-based	


# Cassandra: 

>Built for massive horizontal scaling, super write-optimized — often used in big data, IoT, time-series apps.

>schema	Write-heavy, massive scale

>Wide-column


# Best Use Cases:

- MongoDB: Content management, catalogs, user profiles, real-time analytics, applications needing flexibility.

- Cassandra: Logging, time-series data, metrics, high-throughput IoT, apps needing write-heavy performance and uptime.



# Cassandra:

```sh
docker pull cassandra:latest

docker run -d --name thename cassandra:latest

docker exec -it thename cqlsh


CREATE KEYSPACE perfmonitor
WITH replication = {‘class’ : ‘SimpleStrategy’, ‘replication_factor’: 1};


USE perfmonitor;


CREATE TABLE app_instance (
    id uuid,
    app_name text,
    proc_id text,
    host_id text,
    cpu_time int,
    num_io_ops int,
    PRIMARY KEY (id)
);

DESCRIBE app_instance;


```
# You expected to see
***
```sh
cqlsh:perfmonitor> DESCRIBE app_instance;

CREATE TABLE perfmonitor.app_instance (
    id uuid PRIMARY KEY,
    app_name text,
    cpu_time int,
    host_id text,
    num_io_ops int,
    proc_id text
) WITH additional_write_policy = '99p'
    AND allow_auto_snapshot = true
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND cdc = false
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '16', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND memtable = 'default'
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND extensions = {}
    AND gc_grace_seconds = 864000
    AND incremental_backups = true
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99p';
```


