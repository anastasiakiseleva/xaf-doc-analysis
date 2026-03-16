---
uid: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.GetSelectedObjects
name: GetSelectedObjects()
type: Method
summary: Returns a collection of objects that are currently selected in the [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase)'s control.
syntax:
  content: public override IList GetSelectedObjects()
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) object that represents a list of the selected objects.
seealso: []
---
Use this method to access the selected objects. To perform the required actions when the selection is changed, handle the [ListEditor.SelectionChanged](xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionChanged) event.