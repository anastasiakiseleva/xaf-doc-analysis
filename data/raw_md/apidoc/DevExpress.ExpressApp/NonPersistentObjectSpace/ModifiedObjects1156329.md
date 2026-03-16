---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.ModifiedObjects
name: ModifiedObjects
type: Property
summary: Gets a list of non-persistent objects modified within the current [](xref:DevExpress.ExpressApp.NonPersistentObjectSpace).
syntax:
  content: public override IList ModifiedObjects { get; }
  parameters: []
  return:
    type: System.Collections.IList
    description: An [](xref:System.Collections.IList) of modified objects.
seealso: []
---
The **New**, **Delete** and **Save** Actions are available for [non-persistent objects](xref:116516). The **ModifiedObjects** property provides access to all created, deleted and modified objects within a [](xref:DevExpress.ExpressApp.NonPersistentObjectSpace), unless the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges), [IObjectSpace.Refresh](xref:DevExpress.ExpressApp.IObjectSpace.Refresh) or [IObjectSpace.Rollback](xref:DevExpress.ExpressApp.IObjectSpace.Rollback(System.Boolean)) methods are called. An example is provided in the [How to: Perform CRUD Operations with Non-Persistent Objects](xref:115672) topic.