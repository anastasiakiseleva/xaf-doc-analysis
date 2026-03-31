---
uid: "404262"
title: "Audit Trail: Log Data Changes Made via Web API Endpoints"
---
# Audit Trail: Log Data Changes Made via Web API Endpoints

You can use the following methods to enable the **Audit Trail** module in your applications.

>[!note]
 This option of our Web API Service ships as part of the [DevExpress Universal Subscription](https://www.devexpress.com/subscriptions/universal.xml).


## Enable the Module in the Template Kit

If you use the [Template Kit](xref:405447) to create your **Backend Web API** project, you can enable the **Audit Trail** module the the **Additional Modules** section. For additional information, refer to the following topic: [Create a Standalone Web API Application](xref:403401).


## Enable the EF Core Audit Module in an Existing App

The general information about the EF Core Audit Module, refer to the following article:

- [Audit Trail Module (EF Core)](xref:403104)

### Standalone Web API Application

Install the **DevExpress.ExpressApp.AuditTrail.EFCore** NuGet package.

Register the audited `DBContext` in *Startup.cs*. 

# [C#](#tab/tabid-csharp2)
 
```csharp
services.AddXafWebApi(builder => {
    builder.Modules
        .AddAuditTrailEFCore();

    builder.ConfigureOptions(options => {
        //...
    });

    builder.ObjectSpaceProviders
        .AddSecuredEFCore()
        .WithAuditedDbContext(contexts => contexts.Configure<AppDbContext, AuditingDbContext>(
            (serviceProvider, options) => {
                string connectionString = Configuration.GetConnectionString("ConnectionString");
                options.UseConnectionString(connectionString);
                options.UseObjectSpaceLinkProxies();
            },
            (serviceProvider, options) => {
                string connectionString = Configuration.GetConnectionString("ConnectionString");
                options.UseConnectionString(connectionString);
                options.UseObjectSpaceLinkProxies();
            }
            ))
        .AddNonPersistent();
}, Configuration);
```
***

### XAF Blazor Application

Install the **DevExpress.ExpressApp.AuditTrail.EFCore** NuGet package.

Register the **Audit Trail** module and required services in *Startup.cs*. Use the XAF Application builder:

# [C#](#tab/tabid-csharp2)
 
```csharp
services.AddXaf(Configuration, builder => {
    //..
    builder.Modules
        .AddAuditTrailEFCore()
    //...
}
```
***

## Enable the XPO Audit Module in an Existing App

For general information about XPO Audit Module, refer to the following article: 

- [Audit Trail Module (XPO)](xref:403114)

### Standalone Web API Application

Install the **DevExpress.ExpressApp.AuditTrail.Xpo** NuGet package.

Register the Audit Trail module and required services via the Web API builder in _Startup.cs_:

# [C#](#tab/tabid-csharp2)
 
```csharp
services.AddXafWebApi(builder => {
    builder.AddXpoServices();

    builder.Modules
        .AddAuditTrailXpo(options => {
            //...
        });
}, Configuration);
```
***

### XAF Blazor Application

Install the **DevExpress.ExpressApp.AuditTrail.Xpo** NuGet package.

Register the **Audit Trail** module and required services via the XAF Application builder in _Startup.cs_:

# [C#](#tab/tabid-csharp2)
 
```csharp
services.AddXaf(Configuration, builder => {
    //..
    builder.Modules
        .AddAuditTrailXpo(options => {
            //...
        })
    //...
})
```
***

## Query and Analyze Audit Log Stored in a Data Store

After you run CRUD operations with the help of Web API endpoints, audit log will be stored in the underlying database (**AuditDataItemPersistent** table). The **Audit Module** tracks built-in change operations (such as object creation, deletion, property modification), as well as any custom operations.

You can access the audit log with the help of any database management system (DBMS) that supports SQL query execution. Another option is to write code - use the API of your ORM tool:

- **EF Core**: [Access the Audit Log In the Database](xref:403111) 
- **XPO**: [Analyze the Audit Log using SQL Queries](xref:113615#analyze-the-audit-log-using-sql-queries)

Web API Service users who own the Universal Subscription can optionally create an administrative XAF WinForms or ASP.NET Core Blazor clients to view and analyze the Audit Log:

- **EF Core**: [Display Change History in the Object Detail View](xref:403104#display-change-history-in-the-object-detail-view)
- **XPO**: [Analyze the Audit Log in a UI](xref:113615#analyze-the-audit-log-in-a-ui)
