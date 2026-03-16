---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjectByKey(System.Type,System.Object)
name: GetObjectByKey(Type, Object)
type: Method
summary: Returns the persistent object that has the specified value for its key property.
syntax:
  content: public virtual object GetObjectByKey(Type objectType, object key)
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
This method does nothing and returns `null`. Override it in the `BaseObjectSpace` class' descendants.