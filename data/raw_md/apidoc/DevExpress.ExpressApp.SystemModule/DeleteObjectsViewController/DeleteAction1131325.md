---
uid: DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.DeleteAction
name: DeleteAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController)'s **Delete** Action.
syntax:
  content: public SimpleAction DeleteAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the **Delete** Action.
seealso: []
---
The **Delete** Action deletes object(s) selected in the current View.

This Action's `Execute` event is handled by the `DeleteObjectsViewController`'s `Delete` protected method (see the class description). If you need to modify the way this Action is executed, inherit from this Controller and override the `Delete` method.

Alternatively, handle the [DeleteObjectsViewController.Deleting](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.Deleting) event. It provides access to the collection of objects to be deleted. You can change this collection. To do this, use the event handler's `DeletingEventArgs.Objects` parameter.

By default, the object(s) from a root View (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)) is deleted immediately. The objects deleted from a nested View (not root View) are only marked as objects to be deleted. They will be removed during the next call of the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method. To change this behavior, use the [DeleteObjectsViewController.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.AutoCommit) property.

By default, the **Delete** Action is active (visible) under the following conditions:

* The current View is not read-only.
* The current View is a root Detail View (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)) or any List View.
* The applied [Security System](xref:113366) allows deletion from the current object collection.
* The [IModelView.AllowDelete](xref:DevExpress.ExpressApp.Model.IModelView.AllowDelete) property is set to `true`.
* The object to be deleted from a Detail View is not new.

For more information of how to hide the Actions, refer to the [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) topic.

To ascertain why the **Delete** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

Information on the **Delete** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).