Specifics:
Load Balancer Configuration:

Distribution Algorithm: Round Robin - Simple, evenly distributes traffic among servers.
Active-Active Setup: All servers are active and serving traffic.
Database Primary-Replica Cluster:

Purpose: Provides fault tolerance and scalability.
Primary Node: Handles both read and write operations.
Replica Node: Mirrors data from the primary, handles read-only operations.
Difference Between Primary and Replica:

Primary Node: Accepts write operations, updates the database.
Replica Node: Provides read scalability, mirrors data from the primary.
Issues with the Infrastructure:
Single Point of Failure (SPOF):

The Load Balancer (HAproxy) is a potential SPOF. If it fails, incoming traffic won't be distributed, causing downtime.
Mitigation: Implement a High Availability setup for the Load Balancer (e.g., clustering, failover).
Security Issues:

No Firewall: Lack of a firewall exposes servers to unauthorized access.
No HTTPS: Communication between users and servers is not encrypted, risking data interception.
Mitigation: Implement firewalls, and configure HTTPS using SSL/TLS certificates.
No Monitoring:

Lack of monitoring makes it difficult to identify performance issues, security breaches, or infrastructure failures.
Mitigation: Implement monitoring tools (e.g., Prometheus, Grafana) for real-time visibility into server and application health.
