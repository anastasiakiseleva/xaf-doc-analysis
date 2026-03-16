---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetKeyPropertyType(System.Type)
name: GetKeyPropertyType(Type)
type: Method
summary: Gets the key property type of the specified business type.
syntax:
  content: public virtual Type GetKeyPropertyType(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of the objects whose key property type is requested.
  return:
    type: System.Type
    description: A [](xref:System.Type) object which is the type of the specified type's key property.
seealso: []
---
Returns `null` if there is no key property in the specified type.