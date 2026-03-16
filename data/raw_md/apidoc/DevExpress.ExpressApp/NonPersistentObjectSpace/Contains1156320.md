---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.Contains(System.Object)
name: Contains(Object)
type: Method
summary: Indicates whether a specified object belongs to the current Object Space.
syntax:
  content: public override bool Contains(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object to be tested.
  return:
    type: System.Boolean
    description: '**true** if the specified object belongs to the current Object Space; otherwise, **false**.'
seealso: []
---
Objects that you process can belong to different Object Spaces. For instance, one object can be from a Detail View's Object Space, another from the invoked pop-up Window's Object Space. The **Contains** method is intended to indicate whether a certain object belongs to the current Object Space.