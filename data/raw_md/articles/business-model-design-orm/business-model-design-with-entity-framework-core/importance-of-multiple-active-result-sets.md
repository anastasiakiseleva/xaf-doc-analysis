---
uid: "404348"
title: 'The Importance of Multiple Active Result Sets in Entity Framework Core Data Models'
---

# The Importance of Multiple Active Result Sets in Entity Framework Core Data Models

XAF requires [Multiple Active Result Sets (MARS)](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/enabling-multiple-active-result-sets) in applications connected to a Microsoft SQL Server database. Make sure that your connection strings include the following setting: `MultipleActiveResultSets=True;`.

For database management systems other than Microsoft SQL Server, the following mechanism is used so that applications can work correctly without the Multiple Active Result Sets feature: we register an [interceptor](https://learn.microsoft.com/en-us/ef/core/logging-events-diagnostics/interceptors) that creates additional separate database connections when an application needs to execute multiple queries in parallel. The queries are then executed within these separate connections.

## Technical Details

XAF applications use the [Lazy Loading](https://learn.microsoft.com/en-us/ef/core/querying/related-data/lazy) feature of Entity Framework Core to load related objects and collections only when the application needs them. 

When XAF loads a collection of objects from a database, sometimes it needs to read the properties of an object that has just been loaded. For example, this is required when the application uses the Security System, or when it load objects into a collection that is already displayed in the user interface. In such cases, if it is required to read a lazy loaded property before XAF has finished loading all requested objects, multiple database queries are executed within the same database connection. To execute such a query, Multiple Active Result Sets support is required at the ADO.NET database provider level.
