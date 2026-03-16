---
uid: DevExpress.ExpressApp.IObjectSpace.ConfirmationRequired
name: ConfirmationRequired
type: Event
summary: Occurs when performing **Refresh** or **Rollback** operations with the current Object Space's persistent objects.
syntax:
  content: event EventHandler<ConfirmationEventArgs> ConfirmationRequired
seealso: []
---
`BaseObjectSpace` raises the `ConfirmationRequired` event from the [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) and [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) methods when unsaved changes exist.

Windows Forms applications automatically handle this event to show confirmation messages in all Object Views (both Detail Views and List Views). The following topics describe how to change this behavior:
* @DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode
* [](xref:403181)

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in a descendant of the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class, you do not need to raise this event. The [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) and [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) methods raise it for you.

You only need to override the protected virtual `BaseObjectSpace.Reload` method. The system calls this virtual method from the `BaseObjectSpace.Refresh` and `BaseObjectSpace.Rollback` methods when it must reload the container for in-memory objects. For example, it reloads [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) in the XPObjectSpace case, or [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext) in the EFCoreObjectSpace case.