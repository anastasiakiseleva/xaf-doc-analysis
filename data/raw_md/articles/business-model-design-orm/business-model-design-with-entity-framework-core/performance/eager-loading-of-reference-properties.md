---
uid: "404429"
title: 'Eager Loading of Reference (Foreign Key, Complex Type) Properties'
seealso:
  - linkId: "402958"
  - linkId: "404292"
  - linkId: "404862"
---

# Eager Loading of Reference (Foreign Key, Complex Type) Properties

When an object that has reference properties is retrieved from a database, the objects linked to the reference properties are not immediately loaded. To load a referenced object, a separate database query is executed the first time the reference property is accessed. This results in an increase in the number of individual database queries, which can negatively impact the application performance.

Use the [PreFetchReferenceProperties](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1.PreFetchReferenceProperties) setting to specify that when business objects are fetched from the database, all objects linked to their reference properties should also be eagerly fetched within the same database query, which reduces the number of database requests required to display views for objects with reference properties. 

> [!NOTE]
> The `PreFetchReferenceProperties` setting does not affect _collection_ properties.

The `PreFetchReferenceProperties` setting is specified on application startup in code that registers the EF Core Object Space Provider (the [Template Kit](xref:405447) generates this code automatically):

**File**: _MySolution.Blazor.Server/Startup.cs._, _MySolution.Win/Startup.cs_

# [C# (Blazor)](#tab/tabid-csharp-blazor)

```csharp{6}
public void ConfigureServices(IServiceCollection services) {-+
    // ...
    services.AddXaf(Configuration, builder => {
        // ...
        builder.ObjectSpaceProviders
            .AddSecuredEFCore(options => options.PreFetchReferenceProperties())
            .WithDbContext<MySolutionEFCoreDbContext>((application, options) => { /* ... */ }
        // ...
    }
    // ...
}
```	

# [C# (WinForms)](#tab/tabid-csharp-winforms)

```csharp{4}
public static WinApplication BuildApplication(string connectionString) {
    // ...
    builder.ObjectSpaceProviders
        .AddSecuredEFCore(options => options.PreFetchReferenceProperties())
        .WithDbContext<MySolutionEFCoreDbContext>((application, options) => { /* ... */ }
    // ...
}
```
***

## Usage Details

Consider the following EF Core business class:

# [C#](#tab/tabid-csharp)

```csharp
public class BusinessObject : BaseObject {
   public virtual string Name { get; set; }
   public virtual RefObjectA RefA { get; set; }
   public virtual RefObjectB RefB { get; set; }
   public virtual ICollection<RefObjectC> RefCollection { get; set; }
}
```
***

If the `PreFetchReferenceProperties` setting is disabled, when the business object is loaded from a database, only the object itself is loaded. The business objects linked to the `RefA` and `RefB` properties are loaded lazily, when the application first accesses these properties. If you use the `PreFetchReferenceProperties(true)` setting, a single database query is used to load the persistent parent object together with the referenced objects.

Because collection properties are not affected by the `PreFetchReferenceProperties` setting, objects linked to the `RefCollection` property are still loaded lazily.