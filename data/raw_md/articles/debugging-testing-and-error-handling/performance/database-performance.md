---
uid: "402149"
title: Database Performance
owner: Alexey Kazakov
seealso:
  - linkId: "403402"
---
# Database Performance

This article explains how to analyze the application's database performance.

## Profile SQL Queries

You can collect diagnostic info in the following ways:

- **ORM-independent**
    
    Use the Microsoft SQL Server Profiler or similar tools for your database engine to analyze SQL queries.
- **ORM-dependent**

    - **XPO**

        - [eXpressAppFramework.log](xref:112575) (uncomment the XPO switch in the configuration file).
        - [XPO Profiler](xref:10646)
        - [A custom logger](xref:403928)

    - **Entity Framework Core**
        
        Add the following string to the _appsettings.json_ file:

        ```JSON
        // ...
        "Logging": {
            // ...
            "Microsoft.EntityFrameworkCore.Database.Command": "Information"
        },
        // ...
        ```

        Microsoft Visual Studio now shows SQL queries in the **Output** tab:

        ![|ef_sql](~/images/ef_debug_sql.png)

        Refer to the Microsoft documentation for more information: 
        * [Performance Diagnosis](https://learn.microsoft.com/en-us/ef/core/performance/performance-diagnosis)
        * [Overview of Logging and Interception](https://learn.microsoft.com/en-us/ef/core/logging-events-diagnostics/)

The collected diagnostics info typically includes the following information:

- The list of problematic SQL queries and their duration for problematic database tables.
- The list and code of ORM persistent classes mapped to problematic database tables.
- The list of CriteriaOperator, LINQ expressions and other .NET code methods that triggered problematic SQL queries.
- The list of user actions with slow UI components or a description of slow scenarios (text, screenshots, videos).
- The list of XAF security users for which performance issues are reproducible (it may be specific to permissions).

If everything is fine with your SQL query performance in both production and development environments, go to the [Application Performance](xref:402150) article.

If you determined that SQL queries are slow, follow this topic to exclude the most common reasons for why performance of database-connected or distributed apps may become degraded.

## Database Maintenance Recommendations

Databases require ongoing maintenance to prevent poor application performance, system downtime, and data loss.

Most database systems (for example, Microsoft SQL Server) have good built-in implementation of backup, performance analysis, replication, and other essential maintenance functionality.

Even though a database created by XPO/XAF with their default settings can still be used for some time without maintenance, it is very important to note that for optimal performance and reliability these databases should still be maintained as time goes on, application data grows and other factors are involved during the application's use in production. A good practice for application developers is to consider how database maintenance will be performed before the actual app goes to production, taking into account the specific knowledge of IT infrastructure used to deploy the system and other end client requirements.

You cannot find one-size-fits-all solution to database maintenance. Regular attention must be given to ensure the continued successful operation of any maintenance plan. In the list below, you can find recommendations for the database backup and other maintenance activities that are typically recommended on a regular basis to protect end application data and keep the system reliable, fast, and running smoothly:

- [SQL | Relational databases | Performance | Monitor and Tune for Performance](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance) (MSDN).
- [SQL Server: Top Tips for Effective Database Maintenance](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc671165(v=msdn.10)) (TechNet).
- [SQL Server: Optimizing SQL Server Query Performance](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc137757(v=msdn.10)) (TechNet).
- [SQL Server Maintenance Plan Best Practices](http://justgeeks.blogspot.com/2012/07/sql-server-maintenance-plan-best.html).
- [PostgreSQL | Routine Database Maintenance Tasks](https://www.postgresql.org/docs/current/maintenance.html).
- [Gibraltar VistaDB | Developer's Reference - Database Maintenance](https://doc.vistadb.com/DevelopersReference_Deployment_Maintenance.html).
- [General Mysql database maintenance advice](https://stackoverflow.com/questions/7478849/general-mysql-database-maintenance-advice).

For more details and specific instructions, refer to the documentation and related public community resources of your database vendor.


## Indices

Well-designed indices can reduce disk I/O operations and consume fewer system resources therefore improving SQL query performance. When the number of records in database tables grows, the SELECT and INSERT queries may become slow. You may often need to [add an index to columns](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described) involved in the WHERE, ORDER BY and GROUP BY operations. You can use XPO's [Indexed](xref:DevExpress.Xpo.IndexedAttribute) or [Indices](xref:DevExpress.Xpo.IndicesAttribute) attributes to add an index for a new table. 

If the indices are missing or corrupted, the following issues may occur:

- Slow server-side filtering, sorting, or grouping when using the grid controls or in code.
- [Audit Trail has missing Index](https://supportcenter.devexpress.com/ticket/details/t623550/audit-trail-has-missing-index) | [AuditTrailService is slow when there are many values in the AuditDataItemPersistent table](https://supportcenter.devexpress.com/ticket/details/t934155/audit-audittrailservice-is-slow-when-there-are-many-values-in-the).
- [25k Inserts Daily, 99% Fragmentation on Clustered GUID Index](https://stackoverflow.com/questions/8895818/25k-inserts-daily-99-fragmentation-on-clustered-guid-index) | [How I found out using Oids in clustered index in XAF is a very bad idea](https://supportcenter.devexpress.com/ticket/details/t569076/how-i-found-out-using-oids-in-clustered-index-in-xaf-is-a-very-bad-idea) | [GuidGenerationMode](xref:DevExpress.Xpo.GuidGenerationMode).



## Analyze Environment, Server Software and Hardware

Performance differences are often noticed when testing your app in production. You can analyze differences between the production and development environments, and experiment by making changes one by one. Common cases include the following:

- Network itself and geographic location of clients, web and database servers significantly affect your application performance, especially with remote databases and services. Latency can be high if your database or client is located far from your app server. Examples: a database hosted in a cloud-based infrastructure like Azure runs many SQL queries or a web browser makes many requests back and forth from Europe to a server in America. For more information, see the following: [Database Network Latency](https://stackoverflow.com/questions/605648/database-network-latency).
- Database and app performance depends on available software versions, operating systems, RAM, CPU or even paid plans.


## Next Steps

If everything is fine with your database and environment and your SQL queries still cause performance issues, go to [ORM Performance](xref:402151).
