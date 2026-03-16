---
uid: "405376"
title: 'Use EF Core Migrations to Update the Database Schema in Multi-Tenant Applications'
---
# Use EF Core Migrations to Update the Database Schema in Multi-Tenant Applications

When you use [EF Core migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/) in a multi-tenant application, the following points are still relevant, just as they are in a non-multi-tenant application:

* EF Core migrations do not update the database data. This means that the logic implemented in `ModuleUpdater` is not executed during a migration.
* The first migration must be applied before the initial application launch to create the database structure.

> [!note]
> Disable the XAF database update mechanism, because it can disrupt [EF Core migrations](xref:405418#ef-core-migrations). Refer to the following topic for more information: [Disable Automatic Database Schema Updates](xref:405418#disable-automatic-updates)

## Apply Migrations to Tenant Databases

When using EF Core migrations for tenant databases, the approach is similar to regular databases, but requires specific considerations for multi-tenant applications:

* You need to explicitly specify the connection string for each tenant's database when applying a migration.
* Any changes to the business model require you to apply a migration to every tenant database.
* For a new tenant, its database must be created using migrations strictly before the first login.

The following steps outline the recommended sequence for using migrations for tenant databases in a multi-tenant application:

1. Once you have created the application project and before you run it, create a new migration that will create empty databases for tenants:

    ```Console
    Add-Migration -Project DXApplication1.Module -StartupProject DXApplication1.Module -Context DXApplication1EFCoreDbContext TenantDatabaseInitialCreate
    ```

1. Before the first run of the application, apply the new migration to create a database for every tenant. The [Template Kit](xref:405447) initially creates two tenants in the application: **company1.com** and **company2.com**. In this case, the migration must be applied twice, with different connection strings for the corresponding tenants:

    ```Console
    Update-Database -Project DXApplication1.Module -StartupProject DXApplication1.Module -Context DXApplication1EFCoreDbContext -Connection "Integrated Security=SSPI;Pooling=true;MultipleActiveResultSets=true;Data Source=(localdb)\mssqllocaldb;Initial Catalog=DXApplication1_company1" TenantDatabaseInitialCreate
    Update-Database -Project DXApplication1.Module -StartupProject DXApplication1.Module -Context DXApplication1EFCoreDbContext -Connection "Integrated Security=SSPI;Pooling=true;MultipleActiveResultSets=true;Data Source=(localdb)\mssqllocaldb;Initial Catalog=DXApplication1_company2" TenantDatabaseInitialCreate
    ```

1. Run the application and log into the host interface to create tenant records in the host database.
1. _Optional._ Log into tenant databases to populate them with initial data.
1. Modify the structure of business objects.
1. Create a new migration:

    ```Console
    Add-Migration -Project DXApplication1.Module -StartupProject DXApplication1.Module -Context DXApplication1EFCoreDbContext NewMigrationName
    ```

1. Apply the new migration to every tenant database:

    ```Console
    Update-Database -Project DXApplication1.Module -StartupProject DXApplication1.Module -Context DXApplication1EFCoreDbContext -Connection "Integrated Security=SSPI;Pooling=true;MultipleActiveResultSets=true;Data Source=(localdb)\mssqllocaldb;Initial Catalog=DXApplication1_company1" NewMigrationName
    Update-Database -Project DXApplication1.Module -StartupProject DXApplication1.Module -Context DXApplication1EFCoreDbContext -Connection "Integrated Security=SSPI;Pooling=true;MultipleActiveResultSets=true;Data Source=(localdb)\mssqllocaldb;Initial Catalog=DXApplication1_company2" NewMigrationName
    ```

1. Repeat steps 4-7 as functionality is added to the application.

## Apply Migrations to the Host Database

The host database is intended to store service information about tenants and the administrator user account. Usually, its data structure does not change, and applying EF Core migrations to the host database is not required.

However, it is technically possible to apply migrations to the host database. The following steps demonstrate how to apply migrations to the host database in a multi-tenant application:

1. Since an XAF application does not contain `DbContext` for the host database, you need to create a separate `DbContext` specifically for it:

    ```csharp
    public class DXApplication1HostDbContext : DbContext {
        public DbSet<Tenant> Tenants { get; set; }
        public DbSet<ModelDifference> ModelDifferences { get; set; }
        public DbSet<ModelDifferenceAspect> ModelDifferenceAspects { get; set; }
        public DbSet<ModuleInfo> ModuleInfo { get; set; }
        public DbSet<PermissionPolicyRole> Roles { get; set; }
        public DbSet<ApplicationUser> Users { get; set; }
        public DbSet<ApplicationUserLoginInfo> UserLoginInfos { get; set; }
        public DXApplication1HostDbContext(DbContextOptions<DXApplication1HostDbContext> options) : base(options) { }
        protected override void OnModelCreating(ModelBuilder modelBuilder) {
            base.OnModelCreating(modelBuilder);
            modelBuilder.HasChangeTrackingStrategy(ChangeTrackingStrategy.ChangingAndChangedNotificationsWithOriginalValues);
            modelBuilder.UsePropertyAccessMode(PropertyAccessMode.PreferFieldDuringConstruction);
            modelBuilder.Entity<ApplicationUserLoginInfo>(b => {
                b.HasIndex(nameof(DevExpress.ExpressApp.Security.ISecurityUserLoginInfo.LoginProviderName), nameof(DevExpress.ExpressApp.Security.ISecurityUserLoginInfo.ProviderUserKey)).IsUnique();
            });
            modelBuilder.Entity<ModelDifference>()
                .HasMany(t => t.Aspects)
                .WithOne(t => t.Owner)
                .OnDelete(DeleteBehavior.Cascade);
        }
    }
    //This factory creates DbContext for design-time services. For example, it is required for database migration.
    public class DXApplication1HostDesignTimeDbContextFactory : DesignTimeDbContextFactory<DXApplication1HostDbContext> {
        protected override string ConnectionString  => ";";
    }
    ```

1. In the multi-tenancy configuration code, call the [WithHostDbContext\<TDbContext>](xref:DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder.WithHostDbContext(System.Action{System.IServiceProvider,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},System.Boolean,System.Boolean,System.Boolean)) method to assign the new `DbContext` to the host database:

    # [Sartup.cs](#tab/tabid-csharp)
    ```csharp
    builder.AddMultiTenancy()
        .WithHostDbContext<DXApplication1HostDbContext>((serviceProvider, options) => {
            options.UseConnectionString(connectionString);
        })
    // ...
    ```
    ***

    Once complete, you can use migrations to create and update the host database in the usual way.

1. Once you have created the application project and before you run it, create a new migration that will create the empty host database:

    ```Console
    Add-Migration -Project DXApplication1.Module -StartupProject DXApplication1.Module -Context DXApplication1HostDbContext HostDatabaseInitialCreate
    ```

1. Before the first run of the application, apply the new migration to create the host database.

    ```Console
    Update-Database -Project DXApplication1.Module -StartupProject DXApplication1.Module -Context DXApplication1HostDbContext -Connection "Integrated Security=SSPI;Pooling=true;MultipleActiveResultSets=true;Data Source=(localdb)\mssqllocaldb;Initial Catalog=DXApplication1_Service" HostDatabaseInitialCreate
    ```
1. Modify the structure of business objects in the host database.
1. Create a new migration.
1. Apply the new migration to the host database.
1. Repeat steps 5-7 as functionality is added to the application.