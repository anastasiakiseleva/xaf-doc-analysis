---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObjectByKey(System.Type,System.Object)
name: GetObjectByKey(Type, Object)
type: Method
summary: Returns the persistent object that has the specified value for its key property.
syntax:
  content: public override object GetObjectByKey(Type objectType, object key)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of the object to search for.
  - id: key
    type: System.Object
    description: An object that is the persistent object's key property value.
  return:
    type: System.Object
    description: A persistent object with the specified value for its key property.
seealso: []
---
The `GetObjectByKey` method searches the memory for the object that has the specified value for its key property. If such an object is found, it is not reloaded from the database. Otherwise, the object is retrieved from the database. The `GetObjectByKey` method cannot find objects if they are not saved to a data storage.

To get the key property value, use the [XPObjectSpace.GetKeyValue](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.GetKeyValue(System.Object)) method.
