---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetKeyValue(System.Object)
name: GetKeyValue(Object)
type: Method
summary: Returns the key property's value of the specified persistent object.
syntax:
  content: public override object GetKeyValue(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object whose key property's value is requested.
  return:
    type: System.Object
    description: An object which is the value of the specified object's key property.
seealso: []
---
If there is a key property in the specified object, this method requests its value from the Object Space's [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session). If the specified persistent object is a **null** reference, a **System.ArgumentNullException** is thrown.