---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsModified
name: IsModified
type: Property
summary: Specifies whether objects belonging to the current Object Space are modified.
syntax:
  content: public override bool IsModified { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if at least one persistent object is modified; otherwise, **false**.'
seealso: []
---
An Object Space manages the state of the persistent objects which it created or retrieved. You can get this state via the **IsModified** property. It returns **false** if none of the objects have been modified since they were retrieved or committed (see [CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges)). After an object has been created, modified or deleted, the **IsModified** property returns **true**. When this property's value is changed, the [ModifiedChanged](xref:DevExpress.ExpressApp.BaseObjectSpace.ModifiedChanged) event is raised.

You can change the **IsModified** property value via the [SetModified](xref:DevExpress.ExpressApp.BaseObjectSpace.SetModified*) method.

To get the list of modified objects, use the Object Space's [ModifiedObjects](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.ModifiedObjects) property.
