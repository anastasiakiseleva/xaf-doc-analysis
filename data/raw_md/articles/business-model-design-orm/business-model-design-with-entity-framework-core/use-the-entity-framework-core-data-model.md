---
uid: "402972"
title: Use the Entity Framework Core Data Model
owner: Yekaterina Kiseleva
seealso:
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/ef/core/
    altText: Entity Framework Core Documentation
---
# Use the Entity Framework Core Data Model

This topic describes how to use the Entity Framework Core (EF Core) business model created within the @Microsoft.EntityFrameworkCore.DbContext entity container in XAF.

[!tutorial[Define the Data Model and Set the Initial Data with EF Core](xref:402129)]

## Specify the Entity Container (Context)

In Entity Framework Core, use `DbContext` to create and manage data.

**File**: _MySolution.Module\\BusinessObjects\\MySolutionDbContext.cs_

```csharp
// ...
using DevExpress.ExpressApp.Design;
using DevExpress.ExpressApp.EFCore.DesignTime;

namespace MySolution.Module.BusinessObjects;

public class MySolutionDesignTimeDbContextFactory : DesignTimeDbContextFactory<MySolutionDbContext> {
    protected override string ConnectionString
        => throw new InvalidOperationException("Connection string not specified. Specify connection string to your database here.");
    // Specify the connection string used by the application and defined in the config file, either MySolution.Blazor.Server/appsettings.json or MySolution.Win/App.config
}

[TypesInfoInitializer(typeof(DbContextTypesInfoInitializer<MySolutionDbContext>))]
public class MySolutionDbContext : DbContext {
	public MySolutionDbContext(DbContextOptions<MySolutionDbContext> options) : base(options) { }
	//public DbSet<ModuleInfo> ModulesInfo { get; set; }
	public DbSet<ModelDifference> ModelDifferences { get; set; }
	public DbSet<ModelDifferenceAspect> ModelDifferenceAspects { get; set; }
	// ...

    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        base.OnModelCreating(modelBuilder);
        // ...
    }
}
```

> [!IMPORTANT]
> [!include[composite-key-properties-template](~/templates/composite-key-properties-template.md)]

## Specify the Database Connection

> [!Important]
> [!include[multiple-active-result-sets-efcore](~/templates/multiple-active-result-sets-efcore.md)]

Specify the database connection in the `ConnectionString` section in the configuration file. For additional information, refer to the following topic: [Specify EF Core Database Provider in XAF Application](xref:404290)).

# [(Blazor) MySolution.Blazor.Server\\appsettings.json](#tab/tabid-blazor)
```JSON
{
  "ConnectionStrings": {
    "ConnectionString": "Integrated Security=SSPI;Pooling=false;MultipleActiveResultSets=True;Data Source=(localdb)\\mssqllocaldb;Initial Catalog=MySolution",
    // ...
  },
  // ...
}
```
# [(WinForms ) MySolution.Win\\App.config](#tab/tabid-win)

  ```XML
  <?xml version="1.0"?>
  <configuration>
    <!-- ... -->
    <connectionStrings>
        <add name="ConnectionString" connectionString="Integrated Security=SSPI;MultipleActiveResultSets=True;Data Source=(localdb)\mssqllocaldb;Initial Catalog=Solution111" providerName="System.Data.SqlClient" />
        <!-- ... -->
    </connectionStrings>
  </configuration>
  ```
***

## Add Entities to the UI

To display your entities in the [Navigation System](xref:113198), follow the steps below.

1. Add the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) to their implementations. To hide key properties from the UI, apply [Browsable(false)](xref:System.ComponentModel.BrowsableAttribute) attributes to them. You can apply other [built-in attributes](xref:112701) as well.

    ```csharp{7,9}
    using System;
    using System.ComponentModel;
    using System.ComponentModel.DataAnnotations;
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    // ...
    [DefaultClassOptions]
    public class Contact : BaseObject {
        public virtual String FullName { get; set; }
    }

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
    ```

2. Add the new entity to the solution's DbContext in the _MySolution.Module\\BusinessObjects\\MySolutionDbContext.cs_ file.

    ```csharp{9}
    // ...
    using Microsoft.EntityFrameworkCore;

    namespace MySolution.Module.BusinessObjects;
    // ...
    public class MySolutionDbContext : DbContext {
      public MySolutionDbContext(DbContextOptions<MySolutionDbContext> options) : base(options) { }
      // ...
        public DbSet<Contact> Contacts { get; set; }

        // ...
    }
    ```

## Related Demo 
You can review the **MainDemo.NET.EFCore** demo application that ships with XAF. You can find the demo in the following folder: _[!include[PathToAllXafDemos](~/templates/path-to-all-xaf-demos.md)]\\MainDemo.NET.EFCore_.
