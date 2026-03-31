---
uid: "404400"
seealso:
- linkId: "403104"
- linkId: "403111"
title: 'Extend the Functionality of an Application With EF Core Middle Tier Security'
---

# Extend the Functionality of an Application With EF Core Middle Tier Security

This article describes the considerations that you should take into account when you add certain functionality to your application with Middle Tier Security.

## Add a New DbContext

When you add a new EF Core DbContext to your application, you need to register the DbContext within the Middle Tier Service so that a client application can access business objects declared in this DbContext. To register a DbContext, add the following code to the Middle Tier Service application's `Startup.cs` file.

# [C#](#tab/tabid-csharp)

```csharp
public class Startup { 
    // ... 
    public void ConfigureServices(IServiceCollection services) {         
        //...
        services.AddXafMiddleTier(Configuration, builder => {
            //...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore()
                    // Add the code below.
                    .WithDbContext<NewDbContextType>((serviceProvider, options) => {
                        string connectionString = Configuration.GetConnectionString("ConnectionString");
                        options.UseConnectionString(connectionString);
                        // ... 
                    })
                    .AddNonPersistent();
        });
    }
} 
```
***

## Add the Audit Trail Module

When you add the [Audit Trail Module](xref:403104) to an application with Middle tier Security, you need to additionally configure your Middle Tier Service application to use the audited DbContext. To do this, edit the Middle Tier Service application's `Startup.cs` file as follows:

# [C#](#tab/tabid-csharp)

```csharp
public class Startup { 
    // ...
    public void ConfigureServices(IServiceCollection services) {
        //...
        services.AddXafMiddleTier(Configuration, builder => {
            //...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore()
                    // Remove the code below.
                    //.WithDbContext<MySolutionDbContext>((serviceProvider, options) => { 
                    //    string connectionString = Configuration.GetConnectionString("ConnectionString"); 
                    //    options.UseConnectionString(connectionString); 
                    //    ... 
                    //});
                    // Add the code below.
                    .WithAuditedDbContext(contexts => { 
                        contexts.Configure<MySolutionDbContext, AuditingDbContext>( 
                            (application, businessObjectDbContextOptions) => { 
                                string connectionString = Configuration.GetConnectionString("ConnectionString"); 
                                businessObjectDbContextOptions.UseConnectionString(connectionString); 
                                // ... 
                            }, 
                            (application, auditHistoryDbContextOptions) => { 
                                string connectionString = Configuration.GetConnectionString("ConnectionString"); 
                                auditHistoryDbContextOptions.UseConnectionString(connectionString); 
                            }); 
                    })
                    .AddNonPersistent();
        });
    }

} 
```
***