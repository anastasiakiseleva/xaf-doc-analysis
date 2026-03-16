---
uid: DevExpress.ExpressApp.View.ControlsCreated
name: ControlsCreated
type: Event
summary: Occurs after controls for a [](xref:DevExpress.ExpressApp.View) are created.
syntax:
  content: public event EventHandler ControlsCreated
seealso:
- linkId: "402154"
- linkId: DevExpress.ExpressApp.ViewController.ViewControlsCreated
---

Handle the **View.ControlsCreated** event if you've manually set the [](xref:DevExpress.ExpressApp.XafApplication.DelayedViewItemsInitialization) property to **false**.

> [!NOTE] 
> In most scenarios, handle the [](xref:DevExpress.ExpressApp.Editors.ViewItem.ControlCreated) event instead. The **View.ControlsCreated** event may fire before the necessary controls are created for your [View](xref:112611) and the [](xref:DevExpress.ExpressApp.Editors.ViewItem.Control) property may return null in the event handler. For more details, see [](xref:DevExpress.ExpressApp.XafApplication.DelayedViewItemsInitialization).
