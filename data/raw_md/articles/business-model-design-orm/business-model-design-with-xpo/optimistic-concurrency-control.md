---
uid: "113596"
seealso: []
title: Optimistic Concurrency Control
owner: Ekaterina Kiseleva
---
# Optimistic Concurrency Control

The [optimistic concurrency control](https://en.wikipedia.org/wiki/Optimistic_concurrency_control) (OCC) mechanism is used in XAF applications if you inherit from any of the [base persistent classes ](xref:113146) (except for the `XPLiteObject`). This topic describes how data conflicts are handled in an XAF application.

## Object-Level Locking
Example: Two users open the same object on different workstations and make changes. The first user saves their changes to the database. When the second user tries to save their changes afterward, a message appears indicating a conflict:

![ConcurrencyWin](~/images/concurrencywin116222.png)

After refreshing the object (if required), the second user will be able to make modifications against the renewed object and persist them. If the first user deleted the object, the second user will not be able to make any modifications, and will instead receive the following message.

![ConcurrencyDeleted](~/images/concurrencydeleted116219.png)

## Field-Level Locking
In multi-user applications, two users might edit the same record simultaneously. If they change different fields (for instance, one edits the description, the other adds a file), XAF can merge their changes. To support this, set the static [XpoDefault.TrackPropertiesModifications](xref:DevExpress.Xpo.XpoDefault.TrackPropertiesModifications) property to `true`.

In the _Program.cs_ file of a WinForms application project:

    # [C#](#tab/tabid-csharp)

    ```csharp
    static void Main() {
        DevExpress.Xpo.XpoDefault.TrackPropertiesModifications = true;
        // ...
    }
    ```
    ***

When this property is set to `true` and a user modifies an object that was already changed by another user, a dialog window that suggests merging changes is displayed.

![ConcurrencyMerge](~/images/concurrencymerge117396.png)

Merging is possible when users modify the values of different fields. If both users change the same field value, merging is not possible, and the user can either refresh data or cancel saving.

![ConcurrencyRefresh](~/images/concurrencyrefresh117397.png)

The dialogs illustrated above are provided by the `ProcessDataLockingInfoController` Controller from the `SystemModule` module.

> [!NOTE]
> To see field-level locking in action, refer to the **Concurrent Modifications** section of **Feature Center** demo installed with XAF. By default, the **Feature Center** demo is installed in _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_.

## View-Level Locking

Besides concurrency control at the data level, the `LockController` from the `SystemWindowsForms` module tracks changes at the View level (in WinForms applications). It displays the following message when an object is being modified in two or more different **Views**.

![ConcurrencyLock](~/images/concurrencylock116220.png)

[!include[](~/templates/collisionbehaviorcustomizedatruntime.md)]