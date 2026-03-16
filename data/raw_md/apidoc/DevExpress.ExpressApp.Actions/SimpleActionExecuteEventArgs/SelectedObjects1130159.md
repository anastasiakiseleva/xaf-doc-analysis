---
uid: DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.SelectedObjects
name: SelectedObjects
type: Property
summary: Provides access to the objects selected in the currently invoked [View](xref:112611).
syntax:
  content: public IList SelectedObjects { get; }
  parameters: []
  return:
    type: System.Collections.IList
    description: A list of objects that are selected in the current View.
seealso: []
---
Simple Actions, like other Actions, accompany [Views](xref:112611). When handling the Simple Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event, you can access the selected objects of the View which is accompanied by this Action. To do this, use the **SelectedObjects** property.

> [!NOTE]
> If a Simple Action accompanies a Detail VIew, the **SelectedObjects** property returns the View's current object.

For additional information, refer to the [How to: Access Objects Selected in the Current View](xref:113324) help topic.