---
uid: "405384"
title: Optimistic Locking (Concurrency Control in EF Core)
---
# Optimistic Locking (Concurrency Control in EF Core)

XAF uses the [optimistic concurrency control](https://learn.microsoft.com/en-us/ef/core/saving/concurrency?tabs=data-annotations) (OCC) mechanism to handle data conflicts.

Objects with optimistic locking contain a concurrency token field that updates with each change in the database. XAF compares the local token value with the database value when changes are submitted. If they match, local changes overwrite database values and XAF updates the token. If they differ, XAF merges changes automatically or offers conflict resolution options based on configuration settings.

To support optimistic locking, a business class must implement the `IOptimisticLock` interface.

> [!TIP]
> This topic contains code samples based on the `MainDemo Blazor Server` demo application that ships with XAF. You can find this demo in the following folder: _[!include[PathToAllXafDemos](~/templates/path-to-all-xaf-demos.md)]\\MainDemo.NET.EFCore\CS\MainDemo.Blazor.Server_.

## Enable Optimistic Locking

Optimistic locking is available in new XAF applications out of the box for the `BaseObject` class and all its descendants.

In case of concurrent changes, XAF merges non-conflicting changes and displays a [pop-up window with resolution options](#resolve-collision-dialog) for conflicting changes.

To enable optimistic locking in an existing application, add the following code to the `DbContext.OnModelCreating()` method:

# [CS\MainDemo.Module\BusinessObjects\MainDemoDbContext.cs](#tab/tabid-module)
```csharp{10}
using DevExpress.Persistent.BaseImpl.EF;
using Microsoft.EntityFrameworkCore;

namespace MainDemo.Module.BusinessObjects;

public class MainDemoDbContext : DbContext {
    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        base.OnModelCreating(modelBuilder);
        //...
        modelBuilder.UseOptimisticLock()
    }
}
```
***

## Configure Concurrency Options

Optimistic locking functionality offers two options to fine-tune conflict detection and resolution in your system:

`OptimisticLockDetection`
:   Specifies whether XAF identifies conflicting changes using the object's concurrency token or by assessing all object properties.

`OptimisticLockHandling`
:   Defines how XAF handles conflicts: automatic merging or conflict resolution options.

You can specify both options for an object space in the application builder. These settings will affect your entire application.

# [(Blazor) CS\MainDemo.Blazor.Server\Startup.cs](#tab/tabid-blazor)
```csharp{14-15}
using Microsoft.EntityFrameworkCore;

namespace MainDemo.Blazor.Server;

public class Startup {
    //...
    public void ConfigureServices(IServiceCollection services) {
        //...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MainDemoBlazorApplication>();
            //...
            builder.ObjectSpaceProviders
                .AddSecuredEFCore(o => { o.PreFetchReferenceProperties();
                    o.OptimisticLockHandling = DevExpress.ExpressApp.DC.OptimisticLockHandling.Reload;
                    o.OptimisticLockDetection = DevExpress.ExpressApp.DC.OptimisticLockDetection.AllFields;
                })
        })
    }
}
```

# [(WinForms) CS\MainDemo.Win\ApplicationBuilder.cs](#tab/tabid-win)
```csharp{11-12}
using Microsoft.EntityFrameworkCore;

namespace MainDemo.Win;

public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication() {
        //...
        builder.ObjectSpaceProviders
           .AddEFCore(options => {
               options.PreFetchReferenceProperties();
               options.OptimisticLockDetection = DevExpress.ExpressApp.DC.OptimisticLockDetection.AllFields;
               options.OptimisticLockHandling = DevExpress.ExpressApp.DC.OptimisticLockHandling.Reload; 
           })
    }
}
```
***

To specify custom behavior for a specific class, use the `OptimisticLock` attribute:

[!include[](~/templates/optimisticlockattribute.md)]

## Resolve Collisions Behavior

XAF offers a variety of conflict resolution strategies that depend on the combination of @DevExpress.ExpressApp.DC.OptimisticLockHandling and @DevExpress.ExpressApp.DC.OptimisticLockDetection values.

If you specify `Default` for `OptimisticLockHandling` or `OptimisticLockDetection` option, XAF disables conflict resolution and displays a [warning message](#conflict-warning-message). When you refresh data, the database version overwrites local changes.

The following table covers other available combinations of the `OptimisticLockDetection` and `OptimisticLockHanding` options and describes XAF behavior when concurrency changes are detected:

| OptimisticLockHandling | OptimisticLockDetection = OptimisticLockField | OptimisticLockDetection = AllFields |
|-|-|-|
| `None` | XAF displays a [pop-up window with resolution options](#resolve-collision-dialog). | If changes do not conflict, XAF displays a [pop-up window with merge options](#merge-dialog). If changes are conflicting, XAF displays a [pop-up window with resolution options](#resolve-collision-dialog). |
| `Merge` | If XAF detects changes, it displays a [pop-up window with resolution options](#resolve-collision-dialog). | If changes do not conflict, XAF merges the changes in the background. If changes are conflicting, XAF displays a [pop-up window with resolution options](#resolve-collision-dialog). |
| `Ignore` | XAF overwrites the database object with the local version. | XAF merges non-conflicting changes and overwrites conflicting database changes with the local values. |
| `Reload` | XAF overwrites the local object with the database version. | XAF merges non-conflicting changes and overwrites conflicting local changes with the database values. |

If a user modifies an object that was deleted from the database, XAF shows a [warning message](#conflict-warning-message) and deletes the local version.

### Resolve Collision Dialog

![XAF ASP.NET Core Blazor Collision Handling Pop-Up Window, DevExpress|](~/images/xaf-optimisticlocking-conflict-resolution-popup-devexpress.png)

XAF displays this pop-up window when it detects concurrency conflicting changes in an object and the resulting conflicts cannot be resolved automatically.

Apply My Changes
:   XAF applies the local version of conflicting changes and the database version of non-conflicting changes.
Apply Their Changes
:   XAF takes the database version of conflicting changes and the local version of non-conflicting changes.
Discard All My Changes
:   XAF overwrites all local changes with the database version.
Cancel
:   XAF cancels the "Save" operation.

### Merge Dialog

![XAF ASP.NET Core Blazor Conflict Resolution Pop-Up Window, DevExpress|](~/images/xaf-optimisticlocking-popup-devexpress.png)

XAF displays this pop-up window when it detects concurrency non-conflicting changes in an object (for the combination of [OptimisticLockDetection.AllFields](xref:DevExpress.ExpressApp.DC.OptimisticLockDetection.AllFields) and [OptimisticLockHandling.None](xref:DevExpress.ExpressApp.DC.OptimisticLockHandling.None) options).

Merge
:   XAF merges changes.
Discard All My Changes
:   XAF overwrites all local changes with the database version.
Cancel
:   XAF cancels the "Save" operation.

### Conflict Warning Message

![|XAF ASP.NET Core Blazor Warning, DevExpress|](~/images/xaf-optimisticlocking-default-warning-devexpress.png)

XAF displays this warning when:

* Conflict resolution is disabled.
* When a user attempts to modify a deleted object.
* When a user attempts to delete a modified object.

[!include[](~/templates/collisionbehaviorcustomizedatruntime.md)]

## Disable Optimistic Locking For an Entire Application

To disable optimistic locking in an entire application, remove `modelBuilder.UseOptimisticLock();` from the `DbContext.OnModelCreating()` method:

# [CS\MainDemo.Module\BusinessObjects\MainDemoDbContext.cs](#tab/tabid-module)
```csharp{10}
using DevExpress.Persistent.BaseImpl.EF;
using Microsoft.EntityFrameworkCore;

namespace MainDemo.Module.BusinessObjects;

public class MainDemoDbContext : DbContext {
    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        base.OnModelCreating(modelBuilder);
        //...
        modelBuilder.UseOptimisticLock();

        //...
    }
}
```
***

## Disable Optimistic Locking For a Specific Class

To disable optimistic locking for a specific class, add the `OptimisticLockIgnore` attribute to the class declaration:

[!include[](~/templates/optimisticlockignoreclasslevel.md)]

## Disable Optimistic Locking For a Specific Property

To disable optimistic locking for a specific property, decorate the property with the `OptimisticLockIgnore` attribute:

[!include[](~/templates/optimisticlockignorepropertylevel.md)]