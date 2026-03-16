---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetCollectionSorting(System.Object)
name: GetCollectionSorting(Object)
type: Method
summary: Returns the sort settings for a particular collection.
syntax:
  content: public virtual IList<SortProperty> GetCollectionSorting(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: An Object that is the collection whose sort settings are requested.
  return:
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: A list of **SortProperty** objects specifying the sort order for the _collection_.
seealso: []
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns null, but this behavior is overridden in descendants (see [EFCoreObjectSpace.GetCollectionSorting](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.GetCollectionSorting(System.Object)) and [XPObjectSpace.GetCollectionSorting](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.GetCollectionSorting(System.Object))).