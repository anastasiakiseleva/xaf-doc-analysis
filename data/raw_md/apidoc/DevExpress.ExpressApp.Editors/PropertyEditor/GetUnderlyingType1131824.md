---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.GetUnderlyingType
name: GetUnderlyingType()
type: Method
summary: Specifies the underlying type of the property represented by the current Property Editor.
syntax:
  content: public Type GetUnderlyingType()
  return:
    type: System.Type
    description: A [](xref:System.Type) object representing the underlying type of the property represented by the current Property Editor.
seealso: []
---
If the Property Editor is bound to a nullable type property, the **GetUnderlyingType** property returns the underlying type argument of the nullable type. Otherwise, the property's type is returned.