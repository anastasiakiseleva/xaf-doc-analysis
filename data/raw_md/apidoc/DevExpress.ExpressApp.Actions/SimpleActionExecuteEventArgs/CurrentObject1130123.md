---
uid: DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.CurrentObject
name: CurrentObject
type: Property
summary: Provides access to the current object represented by the currently displayed [View](xref:112611).
syntax:
  content: public object CurrentObject { get; }
  parameters: []
  return:
    type: System.Object
    description: An Object which is currently selected in a View.
seealso: []
---
Simple Actions, like other Actions, accompany [Views](xref:112611). When handling the Simple Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event, you can access the current object of the View that is accompanied by this Action. For this purpose, use the **CurrentObject** property.

For additional information, refer to the [How to: Access Objects Selected in the Current View](xref:113324) help topic.