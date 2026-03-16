---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.CreateNestedObjectSpace
name: CreateNestedObjectSpace()
type: Method
summary: Creates a nested Object Space.
syntax:
  content: public override IObjectSpace CreateNestedObjectSpace()
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object that is a created nested Object Space.
seealso: []
---
Use this method to create a nested Object Space for the current Object Space. When committing the changes made within a nested Object Space, they are merged back into the parent Object Space. This allows treating several related operations as a single unified operation.