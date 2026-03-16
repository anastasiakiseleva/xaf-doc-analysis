---
uid: DevExpress.ExpressApp.XafDataView.SyncRoot
name: SyncRoot
type: Property
summary: Gets an object that can be used to synchronize access to the data view. Always returns the [](xref:DevExpress.ExpressApp.XafDataView) instance itself, because the data view's underlying store is not is not publicly available (see the **Remarks** section of the [ICollection.SyncRoot Property](https://learn.microsoft.com/en-us/dotnet/api/system.collections.icollection.syncroot#System_Collections_ICollection_SyncRoot) topic).
syntax:
  content: public object SyncRoot { get; }
  parameters: []
  return:
    type: System.Object
    description: An object that can be used to synchronize access to the data view.
seealso: []
---
Introduced to provide [](xref:System.Collections.ICollection) support.
