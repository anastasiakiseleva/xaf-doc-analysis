---
uid: "404862"
title: 'How to: Choose the Optimal Query Splitting Behavior in Entity Framework Core'
seealso:
  - linkId: "404429"
  - linkType: HRef
    linkId: https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/24.1.6%2B/Benchmarks
    altText: .NET App Security API Benchmark for EF Core and XPO
---

# How to: Choose the Optimal Query Splitting Behavior in Entity Framework Core

XAF does not explicitly configure query splitting behavior for EF Core DB Contexts. If you do not configure this setting in your application, it defaults to _single query mode_, in which EF Core uses joins to load collection property data from multiple database tables in a single query. In some cases, this mode may lead to excessive data rows loaded with some requests and result in noticeable drops in performance. In such cases, you can use _split query_ mode. In this mode, multiple separate queries are used to load data. Refer to the following topic for more information: [Single vs. Split Queries](https://learn.microsoft.com/en-us/ef/core/querying/single-split-queries).

To enable split query mode in your application, modify the `WithDbContext` method call in the code that configures the EF Core DB Context as follows:

**File**: _MySolution.Blazor.Server/Startup.cs._, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp-blazor)

```csharp{6}
// ...
builder.ObjectSpaceProviders
    .AddSecuredEFCore(options => options.PreFetchReferenceProperties())
        .WithDbContext<DXApplication61.Module.BusinessObjects.DXApplication61EFCoreDbContext>((serviceProvider, options) => {
            // ...
            // This code is specific to MS SQL Server. 
            // Other databases may require different configurations for query splitting behavior.
            options.UseConnectionString(connectionString);
            options.UseSqlServer(o => o.UseQuerySplittingBehavior(QuerySplittingBehavior.SplitQuery));
            // ...
        })
        // ...
```	

***

## Performance Considerations

The [XAF Security System](xref:113366) loads all security data (users, roles, and permissions) [_eagerly_](xref:115638). For this reason, loading security data can become a performance bottleneck in applications with complex security policies. Because of this, the information below focuses on loading of security data as a popular example. However, bear in mind that it is applicable to eager loading of any business object's collection properties.

Consider the following case: your application has a `Users` role assigned to _3_ users. This role is assigned _6_ Type Permissions, _6_ Navigation Permissions, and _4_ Denied Actions. Each Type Permission defines _2_ Member Permissions and _2_ Object Permissions. See [](xref:404633) for more information on permissions in the XAF Security System. When the `Users` role is eagerly loaded, you can calculate the total number of loaded rows as follows.

* In _single query_ mode: _1_ query with over _1720_ data rows is loaded. In this mode, data is always loaded in a single query, but this mode is suboptimal in terms of the amount of data transferred over the network.
* In _split query_ mode: _6_ queries with _43_ total data rows are loaded. This mode saves network traffic and system memory, but it is suboptimal in terms of the total number of requests to the server.

As you can see, there is no single correct answer on which mode to use, because this decision must be based on your application's business model architecture and network infrastructure. The following section demonstrates the strategy that you can follow, to chose the mode that is optimal for your application.

## A Strategy to Choose the Optimal Query Splitting Mode

Look through the list of possible cases below and see which one best describes your application and network infrastructure.

The system has many users (in multiples of _10_). User roles have many permissions (in multiples of _10_) of various types.
:   Use the _split query_ mode.

There are not many users in the system, and/or user roles do not have many permissions.
:   Consider your network's performance to decide which mode to use. See the possible options below.

Your network is fast and network latency is low.
:   Use _split query_ mode.

Your server is hosted in a cloud service; the network is _slow_ and has considerable latency (tens of milliseconds).
:   You need to experiment with various modes.
