---
uid: "404395"
seealso:
- linkId: "404292"
title: EF Core Middle Tier Security - Performance Considerations
owner: Eugeniy Burmistrov
---

# EF Core Middle Tier Security - Performance Considerations

Follow the recommendations below to maximize performance of your XAF application with Middle Tier Security.

The client-server communication between the WinForms application and the Middle Tier Security server is built on top of the HTTP/HTTPS protocol, which imposes an overhead on the request latency and the data transfer speed. Because of this, data queries in an application with Middle Tier Security are slower than in an application that communicates with a database directly. 

The client-server communication speed is affected by the total number of requests more than by the overall volume of the data transferred. 

With the above points in mind, you can use the following best practices to minimize the impact of the Middle Tier Security on the client-server communication speed:

- For List Views that display objects that contain displayable navigation properties, consider using the `DataAcessMode = DataView` setting rather than  `DataAcessMode = Client`. See the following article for more information: [](xref:113683).

- When you use LINQ to load one or multiple objects that contain navigation properties, we recommend that you configure the query to include the navigation property values in the query result (use the [include](https://learn.microsoft.com/en-us/ef/core/querying/related-data/eager) method).

- In the client WinForms application's code that registers the EF Core object space provider, enable the `PreFetchReferenceProperties` setting to ensure that navigation property values are automatically included in queries used to load all persistent objects:

    # [C#](#tab/tabid-csharp1)

    ```csharp
    builder.ObjectSpaceProviders.AddEFCore(
        options => options.PreFetchReferenceProperties()
        // ...
    ),
    ```
    ***

- Use connection pooling to shorten the time required for the Middle Tier Security server to connect to the database. To enable connection pooling, ensure that your ADO.NET provider supports this feature and, if it does, add the following option to the connection string: `Pooling=true`.

    For more information on connection pooling in Microsoft SQL Server, refer to the following article: [SQL Server connection pooling (ADO.NET)](https://learn.microsoft.com/en-us/sql/connect/ado-net/sql-server-connection-pooling).

- It is recommended that your Middle Tier Security server and the database server are hosted on the same physical machine if your production environment allows this.

- Be aware that when you run the Middle Tier Security server and WinForms client from Visual Studio in _Debug_ mode, the application's performance can significantly degrade when compared to the same application without a debugger attached. This is because the Visual Studio debugger greatly increases the `HttpClient`'s data transfer latency both for requests and responses.