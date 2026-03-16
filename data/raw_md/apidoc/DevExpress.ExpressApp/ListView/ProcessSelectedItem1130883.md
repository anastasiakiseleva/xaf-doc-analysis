---
uid: DevExpress.ExpressApp.ListView.ProcessSelectedItem
name: ProcessSelectedItem
type: Event
summary: Occurs when double-clicking an object in the current List View.
syntax:
  content: public event EventHandler ProcessSelectedItem
seealso: []
---
Do not use this event to perform a custom Action when an object is double-clicked in the List View. This event is designed for internal needs. Instead, access the [](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController) and handle its [ListViewProcessCurrentObjectController.CustomProcessSelectedItem](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.CustomProcessSelectedItem) event. To access this Controller, use the **GetController\<ControllerType>** method. For details, refer to the [How to: Replace a List View's Default Action](xref:112820) topic.