---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetKeyValueAsString(System.Object)
name: GetKeyValueAsString(Object)
type: Method
summary: Returns the key property's value of the specified object, converted to a string representation.
syntax:
  content: public override string GetKeyValueAsString(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object whose key property value is requested.
  return:
    type: System.String
    description: A string which is the value of the specified object's key property.
seealso: []
---
This method requests the key property value of the specified object from the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session). If the value is not `null`, its string representation is returned.