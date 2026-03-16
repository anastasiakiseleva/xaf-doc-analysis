---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObject(System.Object)
name: GetObject(Object)
type: Method
summary: Retrieves an object from another Object Space to the current Object Space.
syntax:
  content: public override object GetObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object that represents a template object from another Object Space.
  return:
    type: System.Object
    description: An object retrieved from the database via the current Object Space.
seealso: []
---
This method retrieves the object specified as the _ObjectFromDifferentObjectSpace_ parameter from the database via the current Object Space's [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session). If the passed object is not persistent, it's returned as is.