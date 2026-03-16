---
uid: DevExpress.ExpressApp.IObjectSpace.IsDeleting
name: IsDeleting
type: Property
summary: Indicates whether the current Object Space is about to delete an object(s).
syntax:
  content: bool IsDeleting { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the current Object Space is deleting an object(s); otherwise, **false**.'
seealso: []
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, you don't have to implement the **IsDeleting** property. It's implemented in the **BaseObjectSpace** class. It is set to **true** before the delete operation is performed by the [BaseObjectSpace.Delete](xref:DevExpress.ExpressApp.BaseObjectSpace.Delete*) method and then it is set to **false** after the delete has been performed.