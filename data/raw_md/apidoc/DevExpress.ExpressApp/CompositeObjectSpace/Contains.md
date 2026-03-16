---
uid: DevExpress.ExpressApp.CompositeObjectSpace.Contains(System.Object)
name: Contains(Object)
type: Method
summary: Indicates whether a specified object belongs to the current Object Space.
syntax:
  content: public override bool Contains(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object this method checks.
  return:
    type: System.Boolean
    description: '**true** if the specified object belongs to the current Object Space; otherwise, **false**.'
seealso: []
---
Objects that you process can belong to different Object Spaces. For instance, one object can be from a Detail View's Object Space, another from the invoked pop-up Window's Object Space. Use the **Contains** method before changing a certain object in a certain Object Space. The use of a wrong Object Space causes an exception.

This method returns **true** for all [non-persistent types](xref:116516).