---
uid: DevExpress.Persistent.BaseImpl.BaseObject.ToString
name: ToString()
type: Method
summary: Returns a human-readable string that represents the current business object.
syntax:
  content: public override string ToString()
  return:
    type: System.String
    description: A string representing the current business object.
seealso: []
---
This method returns the value of the business object's default property, converted to a string representation. If a business object does not have a default property, the **ToString** method returns the business class type name postfixed by the object's unique identifier.