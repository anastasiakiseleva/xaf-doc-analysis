---
uid: "403114"
title: Audit Trail Module (XPO)
seealso:
  - linkId: "113615"
  - linkId: "112783"
  - linkId: "112571"
  - linkType: HRef
    linkId: https://supportcenter.devexpress.com/Ticket/Details/E2274/how-to-reuse-xaf-audit-trail-module-functionality-in-a-non-xaf-winforms-application
    altText: How to reuse XAF Audit Trail module functionality in a non-XAF WinForms application
---
# Audit Trail Module (XPO)

The [Audit Trail](xref:112782) is implemented by the _DevExpress.ExpressApp.AuditTrail.Xpo[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_ assembly. Use approaches described in the following topic to add the module in your application: <xref:118047>.

Check that the _DevExpress.Persistent.Base[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_ assembly is referenced in your application, since it contains XAF-independent services used by the **Audit Trail** module.

## Audited Objects

The Audit Trail Module [logs changes](xref:112782#tracked-changes) in the following objects and properties:

* Persistent classes inherited from the [Base Persistent Classes](xref:113146).
* Public writable simple and reference properties defined in persistent classes.
* Public collection properties defined in persistent classes.

Read-only properties (those without a setter) and properties decorated with the @DevExpress.Xpo.NonPersistentAttribute are excluded from the audit trail.

You can change the default module behavior — add or delete objects and properties to log. For more information, see the following topic: <xref:402083>.

## Technical Notes and Details

* The module also saves the current user name provided by the [Security System](xref:113366).
* Real values of properties stored as blob data (for instance, images) are not saved. The "Blob data" string is saved instead. 
* Null values are saved as the "N/A" string.

When the object is modified in the [Detail View](xref:112611), the initial values are copied immediately when an object has been loaded. When the object is modified in [Editable List View](xref:113249), initial values are copied in the [BaseObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.BaseObjectSpace.ObjectChanged) event. The actual values are collected and saved in a separate @DevExpress.Xpo.UnitOfWork in the [BaseObjectSpace.Committed](xref:DevExpress.ExpressApp.BaseObjectSpace.Committed) event.

In code, changes are represented by the `AuditDataItem` class. This class' properties are logged. By default, they are saved to the database by an `AuditDataStore` object. This object creates an `AuditDataItemPersistent` persistent object and saves it to the database. To save changes represented by the `AuditDataItem` objects in another storage, inherit a custom class from the `AuditDataStore` class and override the `Save` method (see the [Customize the Audit Trail System](xref:112783) topic).

## Audit Trail Module Databases

Audit information is logged to the application database. The **Audit Trail** module adds the following tables to the database:

AuditDataItemPersistent
:   The table where `AuditDataItemPersistent` objects are stored. Each time one of the changes listed above is made, a new record is added to this table. The table's `AuditedObject` field contains references to the corresponding records in the `AuditObjectWeakReference` table. The `OldObject` and `NewObject` fields contain references to the corresponding records in the `XPWeekReference` table. String representations of these fields are stored in the `OldValue` and `NewValue` fields, respectively.
	
    > [!NOTE]
    > * The `AuditedObject` is null for deleting operation when the [deferred deletion](xref:2026#deferred-object-deletion) option is disabled for the audited type. Use the [](xref:DevExpress.Xpo.DeferredDeletionAttribute) to enable it.
    > * For collection modification entries (AddedToCollection, RemovedFromCollection, CollectionObjectChanged, AggregatedObjectChanged), a reference to the modified persistent object along with the object's string representation are always stored into the `OldObject` / `OldValue` fields.
    > * The [Security System](xref:113366) creates a default user that cannot access or change the audit data records. To allow a user to access these records, use the following permissions:
    >
    >   ```csharp
    >   // MySolution.Module/DatabaseUpdater/Updater
    >   defaultRole.AddTypePermission<AuditDataItemPersistent>(SecurityOperations.Read, SecurityPermissionState.Deny);
    >   defaultRole.AddObjectPermissionFromLambda<AuditDataItemPersistent>(SecurityOperations.Read, a => a.UserObject.Key == CurrentUserIdOperator.CurrentUserId().ToString(), SecurityPermissionState.Allow);
    >   defaultRole.AddTypePermission<AuditEFCoreWeakReference>(SecurityOperations.Read, SecurityPermissionState.Allow);
    >   ```

`XPWeakReference`
:   Contains data on the objects that have been changed. Object identifiers are stored as strings.
`AuditedObjectWeakReference`
:   Contains data on both objects that have been changed and objects that have taken part in a change. Object identifiers are stored in the `GuidId` or `IntId` field, depending on whether they are stored as Guid or integer values. Thus, the `AuditedObjectWeakReference` table represents a more convenient way to access object data in comparison to the `XPWeakReference` table.

## Work with a Session 

It is possible to lose some of the object changes if these changes are performed within a session that is not audited. This can occur if you manually create a @DevExpress.Xpo.Session or @DevExpress.Xpo.UnitOfWork. To avoid such a failure, use the @DevExpress.ExpressApp.XafApplication.CreateObjectSpace``1 method when you need to create your own @DevExpress.Xpo.Session or @DevExpress.Xpo.UnitOfWork:

# [C#](#tab/tabid-csharp)

```csharp
IObjectSpace objectSpace = Application.CreateObjectSpace<MyBusinessClass>();
// do not write a statement like the following
// Session session = new Session(...);
```

***

## Middle Tier Security Specifics

You need to add the Audit Trail Module only to the server application:

# [MySolution.MiddleTier/Startup.cs](#tab/tabid-csharp-net6)
```csharp{7}
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXafMiddleTier(Configuration, builder => {
            builder.Modules
                .AddAuditTrailXpo()
                // ...
        }
    }
}
```
***