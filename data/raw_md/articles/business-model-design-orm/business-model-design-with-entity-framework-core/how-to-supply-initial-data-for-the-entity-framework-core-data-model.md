---
uid: "402992"
title: 'How to: Supply Initial Data for the Entity Framework Core Data Model'
owner: Yekaterina Kiseleva
seealso: []
---
# How to: Supply Initial Data for the Entity Framework Core Data Model

After you have introduced a data model, you may need to have the application populate the database with a predefined set of objects. In this topic, you will learn how to add data to the database in code when the application runs. For this purpose, the code that creates an Employee object with the associated Task is demonstrated here.

In this example, it is assumed that you have created an XAF solution with an Entity Framework Core data model in accordance with the following help topic: [Use the Entity Framework Core Data Model](xref:402972).

## Implement the Module Updater
Open the _MySolution.Module\\DatabaseUpdate\\Updater.cs_ and override the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method as shown below.

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModuleUpdater {
    public Updater(IObjectSpace objectSpace, Version currentDBVersion) : base(objectSpace, currentDBVersion) { }
    public override void UpdateDatabaseAfterUpdateSchema() {
        if (ObjectSpace.GetObjects<Employee>().Count == 0) {
            var employee = ObjectSpace.CreateObject<Employee>();
            employee.FirstName = "Mary";
            employee.LastName = "Tellitson";
            var task = ObjectSpace.CreateObject<Task>();
            task.Subject = "Check reports";
            task.AssignedTo = employee;
        }
        ObjectSpace.CommitChanges();
    }
}

public class Employee : BaseObject {
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
    publuc virtual IList<Task> Tasks { get; set; } = new ObservableCollection<Task>();
    // ...
}

public class Task : BaseObject {
    publuc virtual string Subject { get; set; }
    public virtual Employee AssignedTo { get; set; }
    // ...
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
***

In the code above, an **Employee** object with an associated **Task** is created if there are no **Employee** records in the database. As you can see, XAF uses an [Object Space](xref:113707) object to manipulate persistent objects (see [Create, Read, Update and Delete Data](xref:113711)).

> [!NOTE]
> To learn more about updating the application database, refer to the [How  database is updated in debug mode](xref:113239#how-database-is-updated-in-debug-mode) topic.

## Add the ModuleInfo Entity
The **ModuleInfo** entity mapped to the **ModuleInfo** table is used when the [XafApplication.CheckCompatibilityType](xref:DevExpress.ExpressApp.XafApplication.CheckCompatibilityType) property is set to **ModuleInfo**, to store the version information of the application modules. When a module assembly version is incremented, XAF compares the actual module versions with versions stored in the database. If versions differ, the database must be updated. To support the database update, an entity that implements the data model must have the **IModuleInfo** interface.

> [!NOTE]
> If you use the [Template Kit](xref:405447) to create an XAF solution, the **ModuleInfo** entity is added automatically by default.

XAF provides a built-in **IModuleInfo** implementor: the **ModuleInfo** entity. Register this entity within your **DbContext** descendant.

# [C#](#tab/tabid-csharp)

```csharp
public class MySolutionEFCoreDbContext : DbContext {
    // ...
    public DbSet<DevExpress.ExpressApp.EFCore.Updating.ModuleInfo> ModuleInfo { get; set; }
}
```

***

After applying the changes above, the **Employee** and **Task** records will be created in the application database.