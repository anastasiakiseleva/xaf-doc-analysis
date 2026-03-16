---
uid: DevExpress.ExpressApp.Editors.ViewItem.ControlCreating
name: ControlCreating
type: Event
summary: Occurs before a control is created for the current View Item.
syntax:
  content: public event EventHandler<EventArgs> ControlCreating
seealso: []
---
A View Item represents a non-visual entity that contains a certain functionality related to an item in a Detail View. To be represented in a UI, a control is created for it. This event is raised as a result of calling the [ViewItem.CreateControl](xref:DevExpress.ExpressApp.Editors.ViewItem.CreateControl) method of the current View Item. Handle it, to perform custom actions before a control is created.

To customize the control after it has been created, handle the [ViewItem.ControlCreated](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreated) event.

By default, View Items' controls are initialized immediately, when a View is created. This behavior ensures that you can rely on the [View.ControlsCreated](xref:DevExpress.ExpressApp.View.ControlsCreated) and [ViewController.ViewControlsCreated](xref:DevExpress.ExpressApp.ViewController.ViewControlsCreated) events when accessing a View Item's control. The downside is that this behavior is slower. You can change this behavior, to speed up creation of complex Views, by setting the [XafApplication.DelayedViewItemsInitialization](xref:DevExpress.ExpressApp.XafApplication.DelayedViewItemsInitialization) property to **true**. This will ensure that View Items' controls are initialized only when they are visible to end-users. However, in this instance you can no longer rely on the **View.ControlsCreated** and **ViewController.ViewControlsCreated** events alone and should additionally ensure that your code is not accessing View Items' controls before they are created. For additional information, refer to the [XafApplication.DelayedViewItemsInitialization](xref:DevExpress.ExpressApp.XafApplication.DelayedViewItemsInitialization) property description.