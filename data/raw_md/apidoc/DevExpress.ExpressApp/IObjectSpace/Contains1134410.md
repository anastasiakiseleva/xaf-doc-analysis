---
uid: DevExpress.ExpressApp.IObjectSpace.Contains(System.Object)
name: Contains(Object)
type: Method
summary: Indicates whether a specified object belongs to the current Object Space.
syntax:
  content: bool Contains(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A persistent object to be tested.
  return:
    type: System.Boolean
    description: '**true** if the specified persistent object belongs to the current Object Space; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.Contains(System.Object)
  altText: EFCoreObjectSpace.Contains(Object)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.Contains(System.Object)
  altText: XPObjectSpace.Contains(Object)
---
Persistent objects that you process can belong to different Object Spaces. For instance, one object can be from a Detail View's Object Space, another from the invoked pop-up Window's Object Space. The **Contains** method is intended to indicate whether a certain object belongs to the current Object Space.