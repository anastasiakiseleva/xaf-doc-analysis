---
uid: DevExpress.ExpressApp.BaseObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)
name: SetTopReturnedObjectsCount(Object, Int32)
type: Method
summary: Sets the maximum number of objects that can be retrieved from the specified collection in a data store.
syntax:
  content: public virtual void SetTopReturnedObjectsCount(object collection, int topReturnedObjectsCount)
  parameters:
  - id: collection
    type: System.Object
    description: A collection from which a number of objects will be retrieved.
  - id: topReturnedObjectsCount
    type: System.Int32
    description: An integer value specifying the maximum number of objects that can be retrieved by the specified collection from the database. **0** indicates that all objects will be retrieved.
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)
---
This method supports the [](xref:DevExpress.Xpo.XPBaseCollection), [](xref:DevExpress.ExpressApp.Xpo.XpoDataView), **EFCollection**, and `DevExpress.ExpressApp.EFCore.EFCoreDataView` collection types. An example of using this method is provided in the @DevExpress.ExpressApp.IObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32) topic.