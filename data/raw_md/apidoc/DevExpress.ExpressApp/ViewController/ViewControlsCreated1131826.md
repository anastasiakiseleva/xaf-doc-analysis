---
uid: DevExpress.ExpressApp.ViewController.ViewControlsCreated
name: ViewControlsCreated
type: Event
summary: Occurs after the controls have been created for the current Controller's [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) if the Controller has already been activated.
syntax:
  content: public event EventHandler ViewControlsCreated
seealso: []
---
Use the **ViewController.ViewControlsCreated** event if you are working in a [Controller](xref:112621)'s designer, or in other scenarios when you need to access controls after a [View Controller](xref:DevExpress.ExpressApp.ViewController) was activated.

> [!NOTE]
> When not working in the scenarios described above, consider handling the **ViewItem.ControlCreated** event instead. The **ViewController.ViewControlsCreated** event may fire before all [View Items](xref:112612) create their controls, for example, if the View Items are on inactive tabs. For more details, see [](xref:DevExpress.ExpressApp.XafApplication.DelayedViewItemsInitialization).