MongoDB: 
Scales horizontally pretty well, but write-heavy use cases may need careful setup.
Read-heavy, flexible 
Document-based	

Cassandra: 
Built for massive horizontal scaling, super write-optimized — often used in big data, IoT, time-series apps.
schema	Write-heavy, massive scale
Wide-column

Best Use Cases:
MongoDB: Content management, catalogs, user profiles, real-time analytics, applications needing flexibility.
Cassandra: Logging, time-series data, metrics, high-throughput IoT, apps needing write-heavy performance and uptime.


Cassandra:
docker pull cassandra:latest
docker run -d --name thename cassandra:latest
docker exec -it thename cqlsh
