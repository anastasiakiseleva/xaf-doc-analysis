---
uid: DevExpress.ExpressApp.Editors.ListEditor.SelectionType
name: SelectionType
type: Property
summary: Returns the selection type supported by the current [List Editor](xref:113189).
syntax:
  content: public abstract SelectionType SelectionType { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SelectionType
    description: A [](xref:DevExpress.ExpressApp.SelectionType) enumeration value that represents the selection type supported by the current List Editor.
seealso: []
---
This property is used by XAF to determine what [Actions](xref:112622) to enable for a List View. 
Each Action has the [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property that specifies whether an Action's availability depends on the current selection. 
XAF determines what actions to enable for a List View by comparing the value of the Action's **SelectionDependencyType** property with the List Editor's **SelectionType** property value.

For example, if an Action requires a selected object and the current List Editor does not support selection, the Action will not be available.

When deriving from the **ListEditor** class, implement this property, so that it returns the correct **SelectionType** enumeration value.