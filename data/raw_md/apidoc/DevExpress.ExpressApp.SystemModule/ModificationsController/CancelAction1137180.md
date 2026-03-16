---
uid: DevExpress.ExpressApp.SystemModule.ModificationsController.CancelAction
name: CancelAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController)'s **Cancel** Action.
syntax:
  content: public SimpleAction CancelAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the **Cancel** Action.
seealso: []
---
The **Cancel** Action rolls back the changes made to the object selected in the current View (see [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean))).

When you execute this Action in a Windows Forms application, you can invoke a confirmation dialog, if the [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode) property is set to [ModificationsHandlingMode.Confirmation](xref:DevExpress.ExpressApp.SystemModule.ModificationsHandlingMode.Confirmation). In this dialog, you can prevent canceling changes or confirm them. If you do not want to invoke this dialog, set the `ModificationsHandlingMode` property to [ModificationsHandlingMode.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.ModificationsHandlingMode.AutoCommit) or [ModificationsHandlingMode.AutoRollback](xref:DevExpress.ExpressApp.SystemModule.ModificationsHandlingMode.AutoRollback).

The **Cancel** Action is active when the current View is root (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)). In Windows Forms applications, its active state depends on the [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode) property value.

Information on the **Cancel** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).