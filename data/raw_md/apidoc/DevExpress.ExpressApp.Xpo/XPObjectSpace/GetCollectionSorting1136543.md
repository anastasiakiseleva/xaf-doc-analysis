---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetCollectionSorting(System.Object)
name: GetCollectionSorting(Object)
type: Method
summary: Returns the sort settings for a particular collection.
syntax:
  content: public override IList<SortProperty> GetCollectionSorting(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: An Object that is the collection whose sort settings are requested.
  return:
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: A list of **SortProperty** objects specifying the sort order for the _collection_.
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.Sorting
---
This method is used internally by Collection Sources, and generally, you do not need to use it.