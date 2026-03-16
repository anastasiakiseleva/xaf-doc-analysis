---
uid: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.SelectionType
name: SelectionType
type: Property
summary: Returns the selection type supported by the [](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor).
syntax:
  content: public override SelectionType SelectionType { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SelectionType
    description: A [](xref:DevExpress.ExpressApp.SelectionType) enumeration value that represents the selection type supported by the current List Editor.
seealso: []
---
The [](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor) supports selection of a single object as well as selection of multiple objects. So, the **SelectionType** property always returns [SelectionType.Full](xref:DevExpress.ExpressApp.SelectionType.Full).

This property is used by XAF to determine what [Actions](xref:112622) to enable for a List View. Each Action has the [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property that specifies whether an Action's availability depends on the current selection. XAF determines what actions to enable for a List View by comparing the value of the Action's **SelectionDependencyType** property with the [List Editor](xref:113189)'s **SelectionType** property value. For instance, if an Action requires a selected object and the current List Editor does not support selection, the Action will not be available.