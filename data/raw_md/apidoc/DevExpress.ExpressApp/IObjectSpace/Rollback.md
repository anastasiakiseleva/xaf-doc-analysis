---
uid: DevExpress.ExpressApp.IObjectSpace.Rollback(System.Boolean)
name: Rollback(Boolean)
type: Method
summary: Cancels the changes made to the persistent objects belonging to the current Object Space.
syntax:
  content: bool Rollback(bool askConfirmation = true)
  parameters:
  - id: askConfirmation
    type: System.Boolean
    defaultValue: "True"
    description: '`true`, if the confirmation dialog is required, otherwise, `false`.'
  return:
    type: System.Boolean
    description: '`true`, if changes made to persistent objects were canceled; otherwise, `false`.'
seealso: []
---
Use this method to cancel the changes to the current Object Space's persistent objects. For example, the built-in **Cancel** Action uses this method.

When you implement the [IObjectSpace](xref:DevExpress.ExpressApp.IObjectSpace) interface in a descendant of the [BaseObjectSpace](xref:DevExpress.ExpressApp.BaseObjectSpace) class, you override the protected virtual `BaseObjectSpace.Reload` method. The [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) method calls `Reload`. 

This method checks if no objects in the current object space change after retrieval or after the last commit (see [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges)). When there are no changes, `BaseObjectSpace.Rollback` recreates the container for in-memory objects by calling `Reload`, retrieves the objects, and returns `true`. 

If at least one object changes, the [IObjectSpace.ConfirmationRequired](xref:DevExpress.ExpressApp.IObjectSpace.ConfirmationRequired) event occurs. Handle this event to show a confirmation window and ask whether to cancel changes. Use the [XafApplication.AskConfirmation](xref:DevExpress.ExpressApp.XafApplication.AskConfirmation(DevExpress.ExpressApp.ConfirmationType)) method to display the confirmation dialog. The method returns a [ConfirmationResult](xref:DevExpress.ExpressApp.ConfirmationResult) enumeration value based on the user's choice. Your next action depends on this result.

* **Yes**
    
    The `BaseObjectSpace.Reload` method recreates the Object Space's container for in-memory objects. In XPObjectSpace, it uses [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session). In EFCoreObjectSpace, it uses [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext). Then, the object retrieves persistent objects from the database. The `BaseObjectSpace.Rollback` method returns `true`.
* **No**
    
    The `BaseObjectSpace.Rollback` method does nothing and returns `false`.
* **Cancel**
    
    The `Rollback` method does nothing and returns `false`.

The `WinModificationsController` handles the [IObjectSpace.ConfirmationRequired](xref:DevExpress.ExpressApp.IObjectSpace.ConfirmationRequired) event. This controller activates only for Detail Views in Windows Forms applications. The controller shows a confirmation window as described above. The system does not show a confirmation window when you invoke the `Rollback` method in a List View. However, it sets the [ConfirmationResult.Yes](xref:DevExpress.ExpressApp.ConfirmationResult.Yes) value by default. This action rolls back all changes and retrieves objects using a new Session.

The following events related to the `Rollback` method are available:

* [IObjectSpace.RollingBack](xref:DevExpress.ExpressApp.IObjectSpace.RollingBack)
    
    Raised before the rollback to prevent it.
* [IObjectSpace.CustomRollBack](xref:DevExpress.ExpressApp.IObjectSpace.CustomRollBack)
    
    Raised before the rollback to perform a custom rollback instead of the default one.

To implement a rollback operation, override the `BaseObjectSpace.Reload` method. In this method, recreate the container for in-memory objects. In XPO, use the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session). In Entity Framework Core, use the [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext).

The `Rollback` method includes an optional parameter, `askConfirmation = true`. If you call the `Rollback` method without parameters, the method displays the following dialog:

![RefreshAskConfirmationq](~/images/RefreshAskConfirmation.png)

To roll back an [Object Space](xref:113707) without a confirmation dialog, explicitly set the `askConfirmation` parameter to `false`.