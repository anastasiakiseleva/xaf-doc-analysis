---
uid: DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase.SelectionType
name: SelectionType
type: Property
summary: Returns the selection type supported by the [](xref:DevExpress.ExpressApp.Scheduler.SchedulerListEditorBase).
syntax:
  content: public override SelectionType SelectionType { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SelectionType
    description: A [](xref:DevExpress.ExpressApp.SelectionType) enumeration value that represents the selection type supported by the current List Editor.
seealso: []
---
Scheduler List Editors support selection of single and multiple objects. The `SelectionType` property always returns [SelectionType.Full](xref:DevExpress.ExpressApp.SelectionType.Full).

XAF uses this property to determine what [Actions](xref:112622) should be enabled for a List View. Each Action has the [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property that specifies whether the Action's availability depends on the current selection. XAF compares the Action's `SelectionDependencyType` property value with the [List Editor](xref:113189)'s `SelectionType` property value. If an Action requires a selected object and the current List Editor does not support selection, the Action is not available.