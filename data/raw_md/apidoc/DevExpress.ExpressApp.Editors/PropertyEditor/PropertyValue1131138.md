---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.PropertyValue
name: PropertyValue
type: Property
summary: Specifies the value of the property represented by the current Property Editor.
syntax:
  content: public object PropertyValue { get; set; }
  parameters: []
  return:
    type: System.Object
    description: An object representing the current value of the Property Editor's bound property.
seealso: []
---
This property returns null if the [ViewItem.CurrentObject](xref:DevExpress.ExpressApp.Editors.ViewItem.CurrentObject) property is set to null (Nothing).

You cannot set a value for this property if the Property Editor is read-only, or its [ViewItem.CurrentObject](xref:DevExpress.ExpressApp.Editors.ViewItem.CurrentObject) is set to null (Nothing).

If you set this property manually, [PropertyEditor.ControlValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValue) will not be changed.