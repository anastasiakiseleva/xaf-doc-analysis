---
uid: DevExpress.ExpressApp.IObjectSpace.GetCollectionSorting(System.Object)
name: GetCollectionSorting(Object)
type: Method
summary: Returns the sort settings for a particular collection.
syntax:
  content: IList<SortProperty> GetCollectionSorting(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: An Object that is the collection whose sort settings are requested.
  return:
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: A list of **SortProperty** objects specifying the sort order for the _collection_.
seealso:
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.GetCollectionSorting(System.Object)
  altText: EFCoreObjectSpace.GetCollectionSorting(Object)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetCollectionSorting(System.Object)
  altText: XPObjectSpace.GetCollectionSorting(Object)
---
This property is intended for internal use. It is supposed to return the sort settings of the specified collection, if this collection is of the type with which the current Object Space can operate. When implementing this property, consider the case when a server collection is passed as the _collection_ parameter.