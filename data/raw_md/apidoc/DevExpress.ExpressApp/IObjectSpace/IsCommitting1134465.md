---
uid: DevExpress.ExpressApp.IObjectSpace.IsCommitting
name: IsCommitting
type: Property
summary: Indicates whether the Object Space is currently committing the changes made to its object(s).
syntax:
  content: bool IsCommitting { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the Object Space is currently committing changes; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.CommitChanges
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, you don't have to implement the **IsCommitting** property. It's implemented in the **BaseObjectSpace** class. In your descendant, you should set this property to **true** in your **DoCommit** method before the commit, and then to **false** after the commit.