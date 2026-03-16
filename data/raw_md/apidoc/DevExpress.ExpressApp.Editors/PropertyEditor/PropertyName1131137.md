---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.PropertyName
name: PropertyName
type: Property
summary: Specifies the name of the property that is represented by the current Property Editor.
syntax:
  content: public string PropertyName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value representing the name of the property bound to the current Property Editor.
seealso:
- linkId: "112580"
---
This property returns the [IModelMemberViewItem.PropertyName](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.PropertyName) property value of the [Application Model](xref:112580)'s node. This node can be accessed using the [PropertyEditor.Model](xref:DevExpress.ExpressApp.Editors.PropertyEditor.Model) property.