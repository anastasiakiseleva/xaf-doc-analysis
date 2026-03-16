---
uid: DevExpress.ExpressApp.IObjectSpace.GetTopReturnedObjectsCount(System.Object)
name: GetTopReturnedObjectsCount(Object)
type: Method
summary: Returns the maximum number of objects to be retrieved by the specified collection from a data store.
syntax:
  content: int GetTopReturnedObjectsCount(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection that is the source for determining the number of objects that can be retrieved by it.
  return:
    type: System.Int32
    description: An integer value specifying the maximum number of objects that can be retrieved by the specified collection from the database.
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetTopReturnedObjectsCount(System.Object)
---
This property is intended for internal use. It is supposed to return the maximum number of objects that can be retrieved by the specified collection if this collection is of the type with which the current Object Space can operate (e.g. XPCollection for an XPObjectSpace or EFCollection for an EFObjectSpace). When implementing this property, consider the case when a server collection is passed as the _collection_ parameter.