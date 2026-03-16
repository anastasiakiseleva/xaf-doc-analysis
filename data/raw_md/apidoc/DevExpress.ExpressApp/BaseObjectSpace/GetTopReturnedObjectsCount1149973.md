---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetTopReturnedObjectsCount(System.Object)
name: GetTopReturnedObjectsCount(Object)
type: Method
summary: Returns the maximum number of objects to be retrieved by the specified collection from a data store.
syntax:
  content: public virtual int GetTopReturnedObjectsCount(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection that is the subject for determining the number of objects that can be retrieved by it.
  return:
    type: System.Int32
    description: An integer value specifying the maximum number of objects that can be retrieved by the specified collection from the database.
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetTopReturnedObjectsCount(System.Object)
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns zero, but this behavior is overridden in descendants.