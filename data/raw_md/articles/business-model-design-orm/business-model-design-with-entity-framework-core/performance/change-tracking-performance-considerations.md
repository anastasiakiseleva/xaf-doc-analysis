---
uid: "404292"
title: 'Change Tracking in EF Core DbContext and Performance Considerations'
owner: Eugeniy Burmistrov
seealso:
  - linkId: "117395"
---

# Change Tracking in EF Core DbContext and Performance Considerations

In XAF, it is important that the application's UI is notified when a business object's property has been changed so that the displayed data is updated accordingly. For this reason, projects created by the [Template Kit](xref:405447) use the [ChangeTrackingStrategy.ChangingAndChangedNotificationsWithOriginalValues](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.changetrackingstrategy) change tracking strategy. This strategy requires entity classes to implement the [INotifyPropertyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanged) and [INotifyPropertyChanging](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanging) interfaces. 

XAF's built-in classes do not implement the `INotifyPropertyChanged` and `INotifyPropertyChanging` interfaces. Instead, the [change-tracking proxies extension](https://learn.microsoft.com/en-us/ef/core/change-tracking/change-detection#change-tracking-proxies) is used so that the `ChangeTrackingStrategy.ChangingAndChangedNotificationsWithOriginalValues` strategy works correctly. This extension requires that all persistent properties in your persistent classes are declared as **virtual**:

# [C#](#tab/tabid-csharp)

```csharp{2}
public class Department : BaseObject {
    public virtual string Name { get; set; }
    // ...
}
```
***

## How to Use Non-Virtual Properties

If you need to use classes with non-virtual persistent properties, the change tracking strategy requires you to manually implement the `INotifyPropertyChanged` and `INotifyPropertyChanging` interfaces for all classes that you use in your DBContext, including XAF internal classes. 

As an alternative, you can use the `ChangeTrackingStrategy.Snapshot` strategy so your entity classes do not need to implement `INotifyPropertyChanged` and `INotifyPropertyChanging`.
However, this can lead to performance issues and cause the application's UI to incorrectly refresh the displayed data.

## Use a DbContext Outside of an XAF Application

If you develop a non-XAF application that needs to reuse your XAF application's DbContext, make sure to add the change-tracking proxies extension in the DbContext creation code:

# [C#](#tab/tabid-csharp)

```csharp{4}
// ...
var optionsBuilder = new DbContextOptionsBuilder<MyEFCoreDbContext>()
    .UseConnectionString(connectionString)
var db = new MyEFCoreDbContext(optionsBuilder.Options);
// ...
```
***

The `UseConnectionString` method activates change tracking proxies. If you configure the database provider and connection string without using this method, you must explicitly call the `UseChangeTrackingProxies` method.