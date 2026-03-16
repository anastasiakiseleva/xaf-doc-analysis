---
uid: DevExpress.ExpressApp.IObjectSpace.IsModified
name: IsModified
type: Property
summary: Specifies whether objects belonging to the current Object Space are modified.
syntax:
  content: bool IsModified { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if at least one persistent object is modified; otherwise, **false**.'
seealso: []
---
An Object Space manages the state of the persistent objects which it created or retrieved. You can learn about this state via the **IsModified** property.

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to implement the **IsModified** property. It's implemented in the **BaseObjectSpace** class. The property's value is changed using the protected **BaseObjectSpace.SetIsModified** method. This method raises the [IObjectSpace.ModifiedChanged](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedChanged) event if the **IsModified** property has been changed. The property returns **false** if none of the objects have been modified since they were retrieved or committed (see [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges)). After an object has been created, modified or deleted, the **IsModified** property returns **true**.

When implementing the **BaseObjectSpace** class descendant, call the **BaseObjectSpace.SetIsModified** method to change the **IsModified** state where it is required.

To get the list of modified objects, use the [IObjectSpace.ModifiedObjects](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedObjects) property.