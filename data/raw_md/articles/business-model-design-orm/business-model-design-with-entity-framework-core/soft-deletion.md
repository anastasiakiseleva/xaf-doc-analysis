---
uid: "405259"
title: Soft Deletion (Deferred Object Deletion)
---
# Soft Deletion (Deferred Object Deletion)

XAF UI and Web API Service-powered apps support EF Core soft deletion (deferred). If you use this deletion mode, the ORM does not immediately remove the corresponding record from the database. Instead, it marks the record as deleted. This technique avoids database exceptions when you delete objects referenced by other entities.

## How It Works

EF Core business classes can implement the `IDeferredDeletion` interface that declares an integer @DevExpress.Persistent.BaseImpl.EF.BaseObject.GCRecord property. As a result, database tables for such classes contain @DevExpress.Persistent.BaseImpl.EF.BaseObject.GCRecord columns. When an object is marked as deleted, XAF assigns the `1` value to @DevExpress.Persistent.BaseImpl.EF.BaseObject.GCRecord. XAF checks @DevExpress.Persistent.BaseImpl.EF.BaseObject.GCRecord values when it loads data for List and Detail Views, reports, and so on.
[DevExpress.Persistent.BaseImpl.EF.BaseObject](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject) and all other built-in XAF business classes (for example, `PermissionPolicyUser` and `FileData`) already implement `IDeferredDeletion` and support this functionality out of the box.

## Enable Soft Deletion

### Configure Your Project's `DBContext`

Newly created projects

:   If you used our [Template Kit](xref:405447), your application already supports deferred deletion functionality on the `DBContext` level (the `UseDeferredDeletion` method). In this case, proceed to the next step: [Enable Deferred Deletion in Custom Entity Classes](#enable-deferred-deletion-in-custom-entity-classes).

Existing projects created with XAF versions before v24.2

:   In the `OnModelCreating` method of your DBContext, call the `UseDeferredDeletion` method:

    **File:** _YourSolutionName.Module\BusinessObjects\YourSolutionNameDbContext.cs_

    ```csharp{13}
    using DevExpress.ExpressApp.Design;
    using DevExpress.ExpressApp.EFCore.DesignTime;
    using DevExpress.Persistent.BaseImpl.EF;
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
    using Microsoft.EntityFrameworkCore;
    using Microsoft.EntityFrameworkCore.Design;

    namespace YourSolutionName.Module.BusinessObjects;

    public class YourSolutionNameDbContext : DbContext {
        protected override void OnModelCreating(ModelBuilder modelBuilder) {
            base.OnModelCreating(modelBuilder);
            modelBuilder.UseDeferredDeletion(this);
            // ...
        }
    }
    ```
### Enable Deferred Deletion in Custom Entity Classes

Recommended technique

:   Derive your custom entity class from [DevExpress.Persistent.BaseImpl.EF.BaseObject](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject) and inherit the @DevExpress.Persistent.BaseImpl.EF.BaseObject.GCRecord property.

Advanced technique

:   Implement the `IDeferredDeletion` interface in your entity class and add a @DevExpress.Persistent.BaseImpl.EF.BaseObject.GCRecord property:

    ```csharp{4,7}
    using DevExpress.Persistent.BaseImpl.EF;
    namespace YourSolutionName.Module.BusinessObjects;

    public class YourCustomEntity : IDeferredDeletion {
        // ...
        public virtual string Name { get; set; }
        public virtual int GCRecord { get; set; }
    }
    ```

### Add the GCRecord Column To Existing Database Tables

If you already mapped your business classes to an existing database, use the automatic converter. For more information, refer to the following Breaking Change ticket in our Support Center: [Core - Database and data model code changes for XAF EF Core apps to support Soft/Deferred Deletion](https://supportcenter.devexpress.com/ticket/details/t1247762/core-database-and-data-model-code-changes-for-xaf-ef-core-apps-to-support-soft-deferred)

## Disable Soft Deletion

To disable soft deletion for the entire application, remove the `UseDeferredDeletion` method from the `OnModelCreating` method in your `DBContext`.

**File:** _YourSolutionName.Module\BusinessObjects\YourSolutionNameDbContext.cs_

```csharp{14}
using DevExpress.ExpressApp.Design;
using DevExpress.ExpressApp.EFCore.DesignTime;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;

namespace YourSolutionName.Module.BusinessObjects;

public class YourSolutionNameDbContext : DbContext {
    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        base.OnModelCreating(modelBuilder);
        // Remove this line from your code.
        modelBuilder.UseDeferredDeletion(this);
        // ...
    }
}
```

To disable soft deletion for a specific class, decorate it with the [DisableDeferredDeletion](xref:DevExpress.ExpressApp.EFCore.DisableDeferredDeletionAttribute) attribute:

```csharp{5}
using DevExpress.Persistent.BaseImpl.EF;

namespace YourSolutionName.Module.BusinessObjects;

[DisableDeferredDeletion]
public class YourCustomEntity : BaseObject {
    public virtual string Name { get; set; }
}
```

Alternatively, you can disable soft deletion for a specific class at runtime in code. This approach can be useful, for instance, when you cannot modify business objects directly.

```csharp{7}
public class YourSolutionNameDbContext : DbContext {
    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        base.OnModelCreating(modelBuilder);
        modelBuilder.UseDeferredDeletion(this);

        // disable deferred deletion for YourCustomEntity
        modelBuilder.DisableDeferredDeletion<YourCustomEntity>();
    }
}
```


## Purge Deleted Objects from SQL Server Database

To purge deleted objects from a table, use the following script:

```
DELETE FROM table_name
WHERE GCRecord = '1'
```

To purge deleted objects from all tables, use the following script:

```
DECLARE @sql NVARCHAR(MAX) = '';
 
SELECT @sql = @sql + 'DELETE FROM ' + table_name + ' WHERE GCRecord = 1'
FROM information_schema.columns
WHERE column_name = 'GCRecord';
 
EXEC sp_executesql @sql;
```
