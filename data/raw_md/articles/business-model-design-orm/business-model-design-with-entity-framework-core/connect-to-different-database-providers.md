---
uid: "404290"
title: Specify EF Core Database Provider in XAF Application
seealso: []
---
# Specify EF Core Database Provider in XAF Application

The DevExpress [Template Kit](xref:405447) allows you to specify a database provider for a new application. Select the required provider in the **Database** section:

![Template Kit - Database options](~/images/template-kit/template-kit-database-types.png)

The Template Kit specifies the connection string in the `connectionStrings` section, for example:

# [SolutionName.Blazor.Server\appsettings.json](#tab/tabid-blazor)
 
```JSON
"ConnectionStrings": {
    "ConnectionString": "Data Source=(localdb)\\mssqllocaldb;Integrated Security=SSPI;
        MultipleActiveResultSets=True;Initial Catalog=SolutionName",
    // ...
```
  
# [SolutionName.Win\App.config](#tab/tabid-win)
 
```HTML
<configuration>
  <connectionStrings>
    <add name="Data Source=(localdb)\mssqllocaldb;Integrated Security=SSPI;MultipleActiveResultSets=True;
        Initial Catalog=SolutionName" />
    <!-- ... -->
```

***

If your application includes a [Middle Tier Server](xref:404389), the Template Kit specifies the connection string in the _SolutionName.MiddleTier\appsettings.json_ file instead of the client application.

# [SolutionName.MiddleTier\appsettings.json](#tab/tabid-mt)
 
```JSON
"ConnectionStrings": {
 "ConnectionString": "Data Source=(localdb)\\mssqllocaldb;Integrated Security=SSPI;
    MultipleActiveResultSets=True;Initial Catalog=SolutionName",
```
***

> [!IMPORTANT]
> [!include[multiple-active-result-sets-efcore](~/templates/multiple-active-result-sets-efcore.md)]

## Change Database Provider in an Existing EF Core Application

XAF applications support the following EF Core providers:

| Database | Provider NuGet package | EFCoreProvider property value |
|------------|----------------------------------|-------------------------|
| Microsoft SQL Server | [Microsoft.EntityFrameworkCore.SqlServer](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.SqlServer/) | `SqlServer` |
| Microsoft SQL Azure | [Microsoft.EntityFrameworkCore.SqlServer](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.SqlServer/) | `SqlServer` |
| MySQL | [Pomelo.EntityFrameworkCore.MySql](https://www.nuget.org/packages/Pomelo.EntityFrameworkCore.MySql/) | `MySQL` |
| PostgreSQL | [Npgsql.EntityFrameworkCore.PostgreSQL](https://www.nuget.org/packages/Npgsql.EntityFrameworkCore.PostgreSQL/) | `PostgreSQL` |
| Oracle | [Oracle.EntityFrameworkCore](https://www.nuget.org/packages/Oracle.EntityFrameworkCore) | `Oracle` |
| Firebird | [FirebirdSql.EntityFrameworkCore.Firebird](https://www.nuget.org/packages/FirebirdSql.EntityFrameworkCore.Firebird) | `Firebird` |
| [SQLite](#sqlite-and-other-file-based-databases) | [Microsoft.EntityFrameworkCore.Sqlite](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.Sqlite) | `SQLite`|

> [!IMPORTANT]
> [Pomelo.EntityFrameworkCore.MySql](https://www.nuget.org/packages/Pomelo.EntityFrameworkCore.MySql/) does not support .NET 10 and Entity Framework Core 10.

To switch to a different supported database provider, follow these steps:

1. Install the provider NuGet package. The referenced **Microsoft.EntityFrameworkCore** package version must match the Entity Framework version used in your solution.

2. Use the `EFCoreProvider` parameter in the connection string to specify the database provider type used in your application.

    # [SolutionName.Blazor.Server\appsettings.json](#tab/tabid-blazor)
    ```JSON
    "ConnectionStrings": {
        "ConnectionString": "EFCoreProvider=Postgres;Host=localhost;Username=user;
            Password=qwerty;Persist Security Info=True;Database=my_db",
        // ...
    ```    

    # [SolutionName.Win\App.config](#tab/tabid-win)
    ```HTML
    <add name="ConnectionString" connectionString="EFCoreProvider=Postgres;Host=localhost;Username=user;
        Password=qwerty;Persist Security Info=True;Database=my_db" />
    ```
    ***

3. If you use [migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/), change the `SolutionNameDesignTimeDbContextFactory.ConnectionString` property as follows:

    # [SolutionName.Module\BusinessObjects\SolutionNameDbContext.cs)](#tab/module)
    ```csharp
    public class SolutionNameDesignTimeDbContextFactory : DesignTimeDbContextFactory<SolutionNameEFCoreDbContext> {
        protected override string ConnectionString  => 
            "EFCoreProvider=Postgres;Host=localhost;Database=my_db;Username=user;Password=qwerty";
    }
    ```
    ***

## In-Memory Database

You can use an in-memory database that works best during the development/debugging stage. To enable this option, open the _SolutionName.Blazor.Server\Startup.cs_ file, comment the `UseConnectionString` option, and uncomment the `UseInMemoryDatabase` option as shown in the following code snippet. Do the same in the _SolutionName.Win\Startup.cs_ file.

Note that this database is recreated each time the server starts. Do not use this code in a production environment to avoid data loss. Refer to the following help topic before you use an in-memory database: [Testing EF Core Applications](https://docs.microsoft.com/en-us/ef/core/testing/in-memory).


# [SolutionName.Blazor.Server\Startup.cs](#tab/tabid-blazor)

```csharp{15,17}
//..
namespace SolutionName.Blazor.Server;

public class Startup {
    public void ConfigureServices(IServiceCollection services) {
        services.AddXaf(Configuration, builder => {
            builder.ObjectSpaceProviders
                .AddEFCore(options => {
                    options.PreFetchReferenceProperties();
                })
                .WithDbContext<WithMigrations.Module.BusinessObjects.WithMigrationsEFCoreDbContext>((serviceProvider, options) => {
                    // Uncomment this code to use an in-memory database. This database is recreated each time the server starts. With the in-memory database, you don't need to apply a migration when the data model is changed.
                    // Do not use this code in a production environment to avoid data loss.
                    // We recommend that you refer to the following help topic before you use an in-memory database: https://docs.microsoft.com/en-us/ef/core/testing/in-memory
                    options.UseInMemoryDatabase();
                    // ...
                    //options.UseConnectionString(connectionString);
                    // ...
```
# [SolutionName.Win\Startup.cs](#tab/tabid-win)

```csharp{12-13}
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        // ...
        builder.ObjectSpaceProviders
            .AddEFCore(options => {
                options.PreFetchReferenceProperties();
            })
                .WithDbContext<constr.Module.BusinessObjects.constrEFCoreDbContext>((application, options) => {
                    // Uncomment this code to use an in-memory database. This database is recreated each time the server starts. With the in-memory database, you don't need to apply a migration when the data model is changed.
                    // Do not use this code in a production environment to avoid data loss.
                    // We recommend that you refer to the following help topic before you use an in-memory database: https://docs.microsoft.com/en-us/ef/core/testing/in-memory
                    options.UseInMemoryDatabase();
                    //options.UseConnectionString(connectionString);
                    // ...
``` 
***


## Configure an Application with Other Providers

This section describes how to use an XAF Application with a database provider that is not listed in the [table of supported providers](#change-database-provider-in-an-existing-ef-core-application) above.

1. Install the relevant EFCore provider for your database. Refer to the following topic for a list of available EF Core providers: [Database Providers](https://learn.microsoft.com/en-us/ef/core/providers/).
1. Change your application's connection string. Do not specify the `EFCoreProvider` parameter.
    # [SolutionName.Blazor.Server\appsettings.json](#tab/tabid-blazor)
    ```JSON
    "ConnectionStrings": {
        "ConnectionString": "<write your connection string here>",

    ```    

    # [SolutionName.Win\App.config](#tab/tabid-win)
    ```HTML
    <add name="ConnectionString" connectionString="<write your connection string here>" />
    ```
    ***
1. If you use [migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/), change the `SolutionNameDesignTimeDbContextFactory.CreateDbContext` method to use your database provider and the updated connection string. Call the appropriate extension method to set up the provider and connection string: `options.UseYourConnectionProvider(connectionString)`. This method and its parameters can be found in the official documentation for the EFCore provider being used.
    
    # [SolutionName.Module\BusinessObjects\SolutionNameDbContext.cs](#tab/module)
    ```csharp{4}
    public class SolutionNameDesignTimeDbContextFactory : DesignTimeDbContextFactory<SolutionNameDbContext> {
        public SolutionNameDbContext CreateDbContext(string[] args) {
            var optionsBuilder = new DbContextOptionsBuilder<SolutionNameDbContext>();
            optionsBuilder.UseYourConnectionProvider(connectionString);
            optionsBuilder.UseChangeTrackingProxies();
            optionsBuilder.UseObjectSpaceLinkProxies();
            return new SolutionNameDbContext(optionsBuilder.Options);
        }
    ```
    ***

1. Change the following files to use your database provider:

    # [Blazor (SolutionName.Blazor.Server\Startup.cs)](#tab/tabid-blazor)
    ```csharp{6}
    public class Startup {
        public void ConfigureServices(IServiceCollection services) {
            //...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore().WithDbContext<SolutionName.Module.BusinessObjects.SolutionNameDbContext>((serviceProvider, options) => {
                    options.UseYourConnectionProvider(connectionString);
                    options.UseChangeTrackingProxies();
                    options.UseObjectSpaceLinkProxies();
                })
    ```

    # [WinForms (SolutionName.Win\Startup.cs)](#tab/tabid-win)
    ```csharp{6}
    public class ApplicationBuilder : IDesignTimeApplicationFactory {
        public static WinApplication BuildApplication(string yourConnectionString) {
            //...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore().WithDbContext<SolutionName.Module.BusinessObjects.SolutionNameDbContext>((application, options) => {
                    options.UseYourConnectionProvider(connectionString);
                    options.UseChangeTrackingProxies();
                    options.UseObjectSpaceLinkProxies();
                })
    ``` 

    ***

## Database Connection Lifetime

Frequent use of a Blazor app or many simultaneous users can create numerous long-lived database connections. To reduce database server load, optimize connection parameters as follows:
* Reduce the wait time before closing idle connections in the pool. For example, add the following parameters to your connection string: `Connection Idle Lifetime=10; Connection Lifetime=1;`.
* Limit the number of connections. For example, add the following parameter to your connection string: `Maximum Pool Size=10`.

 Refer to your ADO.NET provider’s documentation for information about supported connection parameters:
* [PostgreSQL - Connection string parameters](https://www.npgsql.org/doc/connection-string-parameters.html#pooling)
* [SQL Server - ConnectionString property](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectionstring)

## SQLite and Other File-Based Databases

[!include[server-based-data-access-modes-part-1-template](~/templates/server-based-data-access-modes-part-1-template.md)]

We can only recommend that our customers use SQLite for demo/testing purposes or simple applications that do not have many records. NOTE: As a developer or tester, you can also use the databases that can be installed with Visual Studio: Microsoft SQL Server Express or LocalDB databases (a free edition of SQL Server, ideal for development and production for desktop, web, and small server applications).

For XPO-based applications, refer to the following topic to learn how to connect these applications to different database providers: [](xref:2114).