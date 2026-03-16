---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetTopReturnedObjectsCount(System.Object)
name: GetTopReturnedObjectsCount(Object)
type: Method
summary: Returns the maximum number of objects to be retrieved by the specified collection from a data store.
syntax:
  content: public override int GetTopReturnedObjectsCount(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection that is the subject for determining the number of objects that can be retrieved by it.
  return:
    type: System.Int32
    description: An integer value specifying the maximum number of objects that can be retrieved by the specified collection from the database. **0** indicates that all objects will be retrieved.
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.TopReturnedObjects
---
This method is used internally by Collection Sources, and generally, you do not need to use it.