---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.ControlValue
name: ControlValue
type: Property
summary: Returns the value that is set to the current Property Editor's control.
syntax:
  content: public virtual object ControlValue { get; }
  parameters: []
  return:
    type: System.Object
    description: An object representing the value that is set in the current Property Editor's control.
seealso: []
---
This method calls the **GetControlValueCore** method. This method should be overridden in the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) class descendants.