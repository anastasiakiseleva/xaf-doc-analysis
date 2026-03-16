---
uid: DevExpress.ExpressApp.Editors.ListEditor.ProcessSelectedItem
name: ProcessSelectedItem
type: Event
summary: Occurs after an object is selected in the [List Editor](xref:113189)'s control and an end-user presses Enter or double-clicks the object.
syntax:
  content: public event EventHandler ProcessSelectedItem
seealso: []
---
Do not use this event to perform a custom Action when an object is double-clicked in the List Editor's control. This event is designed for internal needs. Instead, access the [](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController) and handle its [ListViewProcessCurrentObjectController.CustomProcessSelectedItem](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.CustomProcessSelectedItem) event. To access this Controller, use the **GetController\<ControllerType>** method. For details, refer to the [How to: Replace a List View's Default Action](xref:112820) topic.