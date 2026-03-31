---
uid: "403111"
title: Access the Audit Log In the Database
seealso: []
---
# Access the Audit Log In the Database

You can use a database management system (DBMS) that supports SQL query execution to access the audit log in the application database. If you use Microsoft SQL Server, we recommend that you use **Microsoft SQL Server Management Studio** or [sqlcmd utility](https://learn.microsoft.com/en-us/sql/tools/sqlcmd-utility) to execute SQL queries. This topic describes the database tables that the Audit Trail Module uses and how to query their records.

## Database Tables and Corresponding Classes

The Audit Trail Module can store the change history in the application database or separate database. This Module uses the following classes to access the information from this database:

DevExpress.Persistent.BaseImpl.EFCore.AuditTrail.AuditEFCoreWeakReference
:	Information on modified objects. Objects and their identifiers are stored as strings.

DevExpress.Persistent.BaseImpl.EFCore.AuditTrail.AuditDataItemPersistent
:	Information on changes. 

To use these classes, ensure that they are registered in your application's auditing @Microsoft.EntityFrameworkCore.DbContext:

**File:** _MySolution.Module\\BusinessObjects\\MySolutionDbContext.cs_

```csharp
public class MySolutionAuditingDbContext : DbContext {
    // ...
    public DbSet<AuditDataItemPersistent> AuditData { get; set; }
    public DbSet<AuditEFCoreWeakReference> AuditEFCoreWeakReference { get; set; }
    // ...
}

```	

When a user changes an audited object, the Module adds new records to the **AuditData** and **AuditEFCoreWeakReference** database tables. The following diagram demonstrates the relationship between these tables:

![Database diagram](~/images/AuditTrail_DatabaseDiagram.png)

> [!NOTE]
> The names of these database tables depend on the names of the corresponding `DbSet` properties in the auditing DbContext and may differ from the default names described above.

### Implement Custom Persistent Object to Store Audit Data

If you want to store additional audit information, do the following:

1. Implement custom classes that either extend the `AuditDataItemPersistent` and `AuditEFCoreWeakReference` classes, or implement the `IAuditDataItemPersistent` and `IEFCoreWeakReference` interfaces. 

   Note that the class that implements `IAuditDataItemPersistent` must contain four foreign keys that refer to the primary key of the class that implements `IEFCoreWeakReference`: 
   
   * `AuditedObject`
   * `OldObject`
   * `NewObject`
   * `UserObject`

2. In ASP.NET Core Blazor and WinForms applications, modify the `WithAuditedDbContext` method call to assign your custom types to `AuditTrailOptions.AuditPersistentItemType` and `AuditTrailOptions.AuditWeakReferenceType` properties.

    **File**: _MySolution.Blazor.Server/Startup.cs._, _MySolution.Win/Startup.cs_

	# [C# (Blazor)](#tab/tabid-csharp-blazor)
	
	```csharp{6,10-13}
    public void ConfigureServices(IServiceCollection services) {-+
        // ...
        services.AddXaf(Configuration, builder => {
			// ...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore().WithAuditedDbContext(contexts => {
                    contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                        (serviceProvider, businessObjectDbContextOptions) => { /* ... */},
                        (serviceProvider, auditHistoryDbContextOptions) => { /* ... */ },
                        (options) => {
                            options.AuditPersistentItemType = typeof(CustomAuditDataItemPersistent);
                            options.AuditWeakReferenceType = typeof(CustomAuditEFCoreWeakReference);
                        }
                    );    
				    // ...
                })
			// ...	
		}
		// ...
	}
	```	

	# [C# (WinForms)](#tab/tabid-csharp-winforms)
	
	```csharp{9-10}
	public static WinApplication BuildApplication(string connectionString) {
	    // ...
		builder.ObjectSpaceProviders
			.AddSecuredEFCore().WithAuditedDbContext(contexts => {
				contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
					(application, businessObjectDbContextOptions) => { /* ... */ },
					(application, auditHistoryDbContextOptions) => { /* ... */ },
                    (options) => {
                        options.AuditPersistentItemType = typeof(CustomAuditDataItemPersistent);
                        options.AuditWeakReferenceType = typeof(CustomAuditEFCoreWeakReference);
                    }
				);
			})
			// ...
	}
	```
	***

## Store Audit Data in a Separate Database

The Audit Trail Module allows you to configure the application's auditing @Microsoft.EntityFrameworkCore.DbContext to use a separate database connection. Use this technique when you need to store audit records in a separate database. 

1. Add an additional connection string for a separate database to the application configuration files.

    **File**: _MySolution.Blazor.Server\appsettings.json_, _MySolution.Win\App.config_

    # [ASP.NET Core Blazor](#tab/tabid-json)
    
    ```JSON
    {
      "ConnectionStrings": {
        "AuditConnectionString": "Integrated Security=SSPI;Pooling=false;MultipleActiveResultSets=true;Data Source=(localdb)\\mssqllocaldb;Initial Catalog=DXApplicationAudit",
        // ...
      },
      // ...
    }
    ```
    # [WinForms](#tab/tabid-xml)
    
    ```XML
    <?xml version="1.0"?>
      <configuration>
        <!-- ... -->
        <connectionStrings>
          <add name="AuditConnectionString" connectionString="Integrated Security=SSPI;MultipleActiveResultSets=True;Data Source=(localdb)\mssqllocaldb;Initial Catalog=DXApplicationAudit" providerName="System.Data.SqlClient" />
          <!-- ... -->
      </connectionStrings>
    </configuration>

    ```
    
    ***

2. Ensure that your application's main module has an additional auditing DbContext that contains code that registers the default `AuditDataItemPersistent` and `AuditEFCoreWeakReference` types. If you use [custom persistent objects to store audit data](#implement-custom-persistent-object-to-store-audit-data), register your custom types instead.

    If the application's main DbContext contains code that registers the same types (the default setting), remove or comment out this code.

    **File**: _MySolution.Module\BusinessObjects\AdditionalDbContext.cs`_

    # [C#](#tab/tabid-csharp)
    ```csharp
    using Microsoft.EntityFrameworkCore;
    using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
    // Additional auditing DbContext
    public class MySolutionAuditingDbContext : DbContext {
        public MySolutionAuditingDbContext(DbContextOptions<MySolutionAuditingDbContext> options)
            : base(options) {
        }
        public DbSet<AuditDataItemPersistent> AuditData { get; set; }
        public DbSet<AuditEFCoreWeakReference> AuditEFCoreWeakReference { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder) {
            base.OnModelCreating(modelBuilder);
            modelBuilder.HasChangeTrackingStrategy(ChangeTrackingStrategy.ChangingAndChangedNotificationsWithOriginalValues);
            modelBuilder.Entity<AuditEFCoreWeakReference>()
                .HasMany(p => p.AuditItems)
                .WithOne(p => p.AuditedObject);
            modelBuilder.Entity<AuditEFCoreWeakReference>()
                .HasMany(p => p.OldItems)
                .WithOne(p => p.OldObject);
            modelBuilder.Entity<AuditEFCoreWeakReference>()
                .HasMany(p => p.NewItems)
                .WithOne(p => p.NewObject);
            modelBuilder.Entity<AuditEFCoreWeakReference>()
                .HasMany(p => p.UserItems)
                .WithOne(p => p.UserObject);
        }
    }
    public class MySolutionEFCoreDbContext : DbContext {
        // ...
        // public DbSet<AuditDataItemPersistent> AuditData { get; set; }
        // public DbSet<AuditEFCoreWeakReference> AuditEFCoreWeakReference { get; set; }
        
        protected override void OnModelCreating(ModelBuilder modelBuilder) {
            // ...

            //modelBuilder.Entity<AuditEFCoreWeakReference>()
            //    .HasMany(p => p.AuditItems)
            //    .WithOne(p => p.AuditedObject);
            //modelBuilder.Entity<AuditEFCoreWeakReference>()
            //    .HasMany(p => p.OldItems)
            //    .WithOne(p => p.OldObject);
            //modelBuilder.Entity<AuditEFCoreWeakReference>()
            //    .HasMany(p => p.NewItems)
            //    .WithOne(p => p.NewObject);
            //modelBuilder.Entity<AuditEFCoreWeakReference>()
            //    .HasMany(p => p.UserItems)
            //    .WithOne(p => p.UserObject);

            // ...
    }
    ```
    ***

3. In ASP.NET Core Blazor and WinForms applications, modify the `WithAuditedDbContext` method call to use separate connection strings for the application's main and auditing DbContexts:

    **File**: _MySolution.Blazor.Server/Startup.cs._, _MySolution.Win/Startup.cs_

	# [C# (Blazor)](#tab/tabid-csharp-blazor)
	
	```csharp{9-14,18-23}
    public void ConfigureServices(IServiceCollection services) {-+
        // ...
        services.AddXaf(Configuration, builder => {
			// ...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore().WithAuditedDbContext(contexts => {
                    contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                        (serviceProvider, businessObjectDbContextOptions) => {
                            string connectionString = null;
                            if (Configuration.GetConnectionString("ConnectionString") != null) {
                                connectionString = Configuration.GetConnectionString("ConnectionString");
                            }
                            ArgumentNullException.ThrowIfNull(connectionString);
                            businessObjectDbContextOptions.UseConnectionString(connectionString);
                            // ...
                        },
                        (serviceProvider, auditHistoryDbContextOptions) => {
                            string connectionString = null;
                            if (Configuration.GetConnectionString("AuditConnectionString") != null) {
                                connectionString = Configuration.GetConnectionString("AuditConnectionString");
                            }
                            ArgumentNullException.ThrowIfNull(connectionString);
                            auditHistoryDbContextOptions.UseConnectionString(connectionString);
                            // ...
                        }
                    );                           
				    // ...
                })
			// ...	
		})
		// ...
	}
	```	

	# [C# (WinForms)](#tab/tabid-csharp-winforms)
	
	```csharp{7,11-17}
	public static WinApplication BuildApplication(string connectionString) {
	    // ...
		builder.ObjectSpaceProviders
			.AddSecuredEFCore().WithAuditedDbContext(contexts => {
				contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
					(application, businessObjectDbContextOptions) => {
                        businessObjectDbContextOptions.UseConnectionString(connectionString);
                        // ...
                    },
					(application, auditHistoryDbContextOptions) => { 
                        string connectionString = null;
                        if (ConfigurationManager.ConnectionStrings["AuditConnectionString"].ConnectionString != null) {
                            connectionString = ConfigurationManager.ConnectionStrings["AuditConnectionString"].ConnectionString;
                        }
                        ArgumentNullException.ThrowIfNull(connectionString);
                        auditHistoryDbContextOptions.UseConnectionString(connectionString);
                        // ...
                    }
				);
			})
			// ...
	}
	```
	***

4. If you want to display audit records from a separate database in the UI, register an additional object space provider for the auditing DbContext:

    **File**: _MySolution.Blazor.Server/Startup.cs._, _MySolution.Win/Startup.cs_

	# [C# (Blazor)](#tab/tabid-csharp-blazor)
	
	```csharp{10-22}
    public void ConfigureServices(IServiceCollection services) {-+
        // ...
        services.AddXaf(Configuration, builder => {
			// ...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore().WithAuditedDbContext(contexts => {
                    contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                        (serviceProvider, businessObjectDbContextOptions) => { /* ... */  },
                        (serviceProvider, auditHistoryDbContextOptions) => { /* ... */ });            
                .AddSecuredEFCore()
                    .WithDbContext<MySolutionAuditingDbContext>((serviceProvider, options) => {
                        string connectionString = null;
                        if (Configuration.GetConnectionString("AuditConnectionString") != null) {
                            connectionString = Configuration.GetConnectionString("AuditConnectionString");
                        }

                        ArgumentNullException.ThrowIfNull(connectionString);
                        options.UseConnectionString(connectionString);
                        options.UseObjectSpaceLinkProxies();
                })
			// ...	
		})
		// ...
	}}
	```	

	# [C# (WinForms)](#tab/tabid-csharp-winforms)
	
	```csharp{8-18}
	public static WinApplication BuildApplication(string connectionString) {
	    // ...
		builder.ObjectSpaceProviders
            .AddSecuredEFCore().WithAuditedDbContext(contexts => {
                contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
                    (serviceProvider, businessObjectDbContextOptions) => { /* ... */  },
                    (serviceProvider, auditHistoryDbContextOptions) => { /* ... */ });
            .AddSecuredEFCore()
                .WithDbContext<DXApplication32.Module.BusinessObjects.DXApplication32AppAuditingDbContext>((serviceProvider, options) => {
                    string connectionString = null;
                    if (ConfigurationManager.ConnectionStrings["AuditConnectionString"].ConnectionString != null) {
                        connectionString = ConfigurationManager.ConnectionStrings["AuditConnectionString"].ConnectionString;
                    }
                    ArgumentNullException.ThrowIfNull(connectionString);
                    options.UseConnectionString(connectionString);
                    options.UseObjectSpaceLinkProxies();
                })
			// ...
	    }
    }
	```
	***

5. In the `Updater` class, check whether the current object space can create an `ApplicationUser` object (or any other persistent object used by the application):

    ```csharp
    // ...
    namespace YourApplicationName.Module.DatabaseUpdate;
    public class Updater : ModuleUpdater {
        public override void UpdateDatabaseAfterUpdateSchema() { 
            base.UpdateDatabaseAfterUpdateSchema(); 
            if (!ObjectSpace.CanInstantiate(typeof(ApplicationUser))) { 
                return; 
            }
            // ...
        }
    }
    ```

## Access the Audit Log

You can write SQL queries to access data from the audit log stored in the database. The following code demonstrates a sample query:

# [SQL](#tab/tabid-sql)
```SQL
SELECT OperationType, ModifiedOn, uwr.DefaultString as UserName, PropertyName, OldValue, NewValue, owr.DefaultString as OldObject, nwr.DefaultString as NewObject
FROM AuditData ad
LEFT JOIN AuditEFCoreWeakReference awr ON ad.AuditedObjectID = awr.ID
LEFT JOIN AuditEFCoreWeakReference owr ON ad.OldObjectID = owr.ID
LEFT JOIN AuditEFCoreWeakReference nwr ON ad.NewObjectID = nwr.ID
LEFT JOIN AuditEFCoreWeakReference uwr ON ad.UserObjectID = uwr.ID
```
***

For example, to filter changes of a particular object, use the following SQL statement (for Microsoft SQL):

# [SQL](#tab/tabid-sql)
```SQL
SELECT OperationType, ModifiedOn, uwr.DefaultString as UserName, PropertyName, OldValue, NewValue, owr.DefaultString as OldObject, nwr.DefaultString as NewObject
FROM AuditData ad
LEFT JOIN AuditEFCoreWeakReference awr ON ad.AuditedObjectID = awr.ID
LEFT JOIN AuditEFCoreWeakReference owr ON ad.OldObjectID = owr.ID
LEFT JOIN AuditEFCoreWeakReference nwr ON ad.NewObjectID = nwr.ID
LEFT JOIN AuditEFCoreWeakReference uwr ON ad.UserObjectID = uwr.ID
WHERE awr.DefaultString = 'Office'
ORDER BY  ModifiedOn
```
***

## Remove the Audit Log Part
The following SQL statements illustrate how to delete all audit log entries made before March 12, 2021:

# [SQL](#tab/tabid-sql)
```SQL
DELETE FROM AuditData WHERE ModifiedOn < '2021-03-12';
DELETE FROM AuditEFCoreWeakReference WHERE LastModifiedDate < '2021-03-12'
```
***

You can also implement an [Action](xref:112622) that executes SQL statements (use standard ADO.NET techniques).
