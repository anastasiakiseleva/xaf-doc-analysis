---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjectKey(System.Type,System.String)
name: GetObjectKey(Type, String)
type: Method
summary: Converts the key property value string representation into its actual type.
syntax:
  content: public virtual object GetObjectKey(Type objectType, string objectKeyString)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of the object whose key property value is to be converted.
  - id: objectKeyString
    type: System.String
    description: A string that is the key property value to be converted.
  return:
    type: System.Object
    description: An object that is the value of the specified type object's key property.
seealso: []
---
The **GetObjectKey** method supports **Int16**, **Int32**, **Int64**, **Decimal**, **Guid**and **String** key types and returns _null_ for other types.