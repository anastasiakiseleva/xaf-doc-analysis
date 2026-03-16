---
uid: "403104"
title: Audit Trail Module (EF Core)
owner: Eugeniy Burmistrov
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-show-audit-entries-for-a-current-object-and-its-aggregated-objects-in-one-list
  altText: XAF - How to show audit entries for a current object and its aggregated objects in one list
---
# Audit Trail Module (EF Core)

This topic describes how to add the Audit Trail Module to your ASP.NET Core Blazor or WinForms application and explains the Module's features specific to the Entity Framework Core ORM.

## Audited Objects

The Audit Trail Module logs changes in the following objects and properties:

* Persistent classes registered as @Microsoft.EntityFrameworkCore.DbSet`1 properties in @Microsoft.EntityFrameworkCore.DbContext.
* Public writable simple and reference properties defined in persistent classes.
* Public collection properties defined in persistent classes.

> [!NOTE]
> * To exclude a persistent property from audit, set @DevExpress.Persistent.Base.UseInAuditTrailAttribute to `false`.

## Add the Audit Trail Module to Your Application

Follow the steps below to add the Audit Trail Module to your application. If you added this Module when you created an XAF application, the [Template Kit](xref:405447) generates the described code automatically:

1. Add the **DevExpress.ExpressApp.AuditTrail.EFCore** NuGet package to the application's main module (_MySolution.Module_).

2. Add a new @Microsoft.EntityFrameworkCore.DbContext used to store audit trail records to the application's main module and register the `AuditDataItemPersistent` and `AuditEFCoreWeakReference` types both in this DbContext and in the application's main DbContext.

	> [!NOTE]
	>
	> You only need to declare the properties used by the Audit Trail Module in both DbContexts if they share the same database connection, which is the default configuration that DevExpress [Template Kit](xref:405447) generates. If you store audit trail records in a separate database, you should only declare these properties in the additional DbContext. Refer to the following help topic for more information on this technique: [Store Audit Data in a Separate Database](xref:403111#store-audit-data-in-a-separate-database).

    **File**: _MySolution.Module/BusinessObjects/MySolutionDbContext.cs_

	# [C#](#tab/tabid-csharp)
	
	```csharp
	public class MySolutionEFCoreDbContext : DbContext {
		// ...
		// Do not add these properties to the main DbConext if you store 
		// audit trail records in a separate database
		public DbSet<AuditDataItemPersistent> AuditData { get; set; }
		public DbSet<AuditEFCoreWeakReference> AuditEFCoreWeakReference { get; set; }

		protected override void OnModelCreating(ModelBuilder modelBuilder) {
			base.OnModelCreating(modelBuilder);
			// ...
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
			// ...
		}
	}
	public class MySolutionAuditingDbContext : DbContext {
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
	```
	***

	For more information on `AuditDataItemPersistent` and `AuditEFCoreWeakReference` classes, refer to the following help topic: [Access the Audit Log In the Database](xref:403111#database-tables-and-corresponding-classes).

3. Register the Audit Trail Module in the ASP.NET Core Blazor and WinForms application projects:

    **File**: _MySolution.Blazor.Server/Startup.cs._, _MySolution.Win/Startup.cs_

	# [C# (Blazor)](#tab/tabid-csharp-blazor)

	```csharp
	public void ConfigureServices(IServiceCollection services) {-+
		// ...
		services.AddXaf(Configuration, builder => {
			// ...
			builder.Modules
				.AddAuditTrailEFCore()
		}
		// ...
	}
	```	

	# [C# (WinForms)](#tab/tabid-csharp-winforms)

	```csharp
	public static WinApplication BuildApplication(string connectionString) {
		var builder = WinApplication.CreateBuilder();
		// ...
		builder.Modules
			.AddAuditTrailEFCore()
	}
	// ...
	```
	***

	> [!Tip]
	> See the following topic for information on alternative ways to register a module: [Ways to Register a Module](xref:118047).

4. In both files, locate the code that configures the object space provider and replace the call to `WithDbContext` with `WithAuditedDbContext` as follows:

    **File**: _MySolution.Blazor.Server/Startup.cs._, _MySolution.Win/Startup.cs_

	# [C# (Blazor)](#tab/tabid-csharp-blazor)
	
	```csharp{6-33}
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
                            businessObjectDbContextOptions.UseObjectSpaceLinkProxies();
                        },
                        (serviceProvider, auditHistoryDbContextOptions) => {
                            string connectionString = null;
                            if (Configuration.GetConnectionString("ConnectionString") != null) {
                                connectionString = Configuration.GetConnectionString("ConnectionString");
                            }

                            ArgumentNullException.ThrowIfNull(connectionString);
                            auditHistoryDbContextOptions.UseConnectionString(connectionString);
                            auditHistoryDbContextOptions.UseObjectSpaceLinkProxies();
                        });
				    // ...
                })
			// ...	
		}
		// ...
	}
	```	

	# [C# (WinForms)](#tab/tabid-csharp-winforms)
	
	```csharp{4-17}
	public static WinApplication BuildApplication(string connectionString) {
		// ...
		builder.ObjectSpaceProviders
			.AddSecuredEFCore().WithAuditedDbContext(contexts => {
				contexts.Configure<MySolutionEFCoreDbContext, MySolutionAuditingDbContext>(
					(application, businessObjectDbContextOptions) => {
						businessObjectDbContextOptions.UseConnectionString(connectionString);
						businessObjectDbContextOptions.UseObjectSpaceLinkProxies();
					},
					(application, auditHistoryDbContextOptions) => {
						auditHistoryDbContextOptions.UseConnectionString(connectionString);
						auditHistoryDbContextOptions.UseObjectSpaceLinkProxies();
					}
				);
			})
			// ...
	}
	```
	***

7. Run the application and click the **Reports** | **Audit Event** navigation item. The invoked list view contains change history for audited objects.

**ASP.NET Core Blazor**

![Audit Event View in an ASP.NET Core Blazor application](~/images/AuditEvents_Blazor.png)

**WinForms**

![Audit Event View in a WinForms application](~/images/AuditEvents_WinForms.png)

> [!Note]
> The `AuditInformationReadonlyViewController` does not allow users to create, edit, or delete `IAuditDataItemPersistent` objects from the UI.

## Display Change History in the Object Detail View

Follow the steps below to show the history of an object in its detail view:

1. Add the `AuditDataItemPersistent` collection property to your business class.
	
	# [C#](#tab/tabid-csharp)

	```csharp
	using System;
	using System.Collections.Generic;
	using System.ComponentModel;
	using System.ComponentModel.DataAnnotations;
	using System.ComponentModel.DataAnnotations.Schema;
	using DevExpress.ExpressApp;
	using DevExpress.Persistent.Base;
	using DevExpress.Persistent.BaseImpl.EF;
	using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
	// ...
	[DefaultClassOptions]
	public class MyBusinessObject : BaseObject {
		public virtual string StringProperty { get; set; }

		[CollectionOperationSet(AllowAdd = false, AllowRemove = false)]
		[NotMapped]
		public virtual IList<AuditDataItemPersistent> ChangeHistory {
		    get { return AuditDataItemPersistent.GetAuditTrail(ObjectSpace, this); }
		}
	}

	// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
	```
	***

2. In applications with the [Security System](xref:113366), configure permissions for non-administrative user roles so users can read information on their changes only.
	
	**File**: _MySolution.Module/DatabaseUpdater/Updater.cs_
    # [C#](#tab/tabid-csharp)
	
	```csharp{12-14}
	using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
	// ...
    public class Updater : ModuleUpdater {
		// ...
    	public override void UpdateDatabaseAfterUpdateSchema() {
            base.UpdateDatabaseAfterUpdateSchema();
			// ...
			PermissionPolicyRole userRole = ObjectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Users");
            if(userRole == null) {
				defaultRole = ObjectSpace.CreateObject<PermissionPolicyRole>();
				// ...
				defaultRole.AddTypePermission<AuditDataItemPersistent>(SecurityOperations.Read, SecurityPermissionState.Deny);
				defaultRole.AddObjectPermissionFromLambda<AuditDataItemPersistent>(SecurityOperations.Read, a => a.UserObject.Key == CurrentUserIdOperator.CurrentUserId().ToString(), SecurityPermissionState.Allow);
				defaultRole.AddTypePermission<AuditEFCoreWeakReference>(SecurityOperations.Read, SecurityPermissionState.Allow);
			}
		}
	}
	```
	***


The images below demonstrate the result:

**ASP.NET Core Blazor**

![Change History in a business object Detail View](~/images/AuditDataItemPersistent_collection.png)

**WinForms**

![Change History in a business object Detail View](~/images/AuditDataItemPersistent_collection_WinForms.png)

> [!Tip]
> You can also [access the audit log in the database](xref:403111) directly if you do not want to display history in the UI.
