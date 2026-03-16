---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)
name: SetTopReturnedObjectsCount(Object, Int32)
type: Method
summary: Sets the maximum number of objects that can be retrieved from the specified collection in a data store.
syntax:
  content: public override void SetTopReturnedObjectsCount(object collection, int topReturnedObjectsCount)
  parameters:
  - id: collection
    type: System.Object
    description: A collection from which a number of objects will be retrieved.
  - id: topReturnedObjectsCount
    type: System.Int32
    description: An integer value specifying the maximum number of objects that can be retrieved by the specified collection from the database. **0** indicates that all objects will be retrieved.
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.TopReturnedObjects
---
This method supports [](xref:DevExpress.Xpo.XPBaseCollection) and [](xref:DevExpress.ExpressApp.Xpo.XpoDataView) collection types. When a negative value is passed, an **ArgumentException** is thrown. An example of using this method is provided in the [IObjectSpace.SetTopReturnedObjectsCount](xref:DevExpress.ExpressApp.IObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)) topic.