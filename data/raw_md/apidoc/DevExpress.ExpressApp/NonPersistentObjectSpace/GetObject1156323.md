---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.GetObject(System.Object)
name: GetObject(Object)
type: Method
summary: Retrieves an object from another Object Space to the current Object Space.
syntax:
  content: public override object GetObject(object objectFromDifferentObjectSpace)
  parameters:
  - id: objectFromDifferentObjectSpace
    type: System.Object
    description: An object that represents a template object from another Object Space.
  return:
    type: System.Object
    description: An object retrieved from the database via the current Object Space.
seealso: []
---
This method retrieves the object specified as the _ObjectFromDifferentObjectSpace_ parameter from the database via the current Object Space.