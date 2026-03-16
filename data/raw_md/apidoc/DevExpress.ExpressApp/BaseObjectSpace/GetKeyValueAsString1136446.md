---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetKeyValueAsString(System.Object)
name: GetKeyValueAsString(Object)
type: Method
summary: Returns the key property's value of the specified object, converted to a string representation.
syntax:
  content: public virtual string GetKeyValueAsString(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object whose key property's value is returned.
  return:
    type: System.String
    description: A string which is the value of the specified object's key property.
seealso: []
---
This method does nothing and returns `null`. Override it in the `BaseObjectSpace` class' descendants.