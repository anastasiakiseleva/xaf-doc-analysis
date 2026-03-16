---
uid: DevExpress.ExpressApp.CompositeObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)
name: SetTopReturnedObjectsCount(Object, Int32)
type: Method
summary: Sets the maximum number of objects that the specified collection can retrieve from a data store.
syntax:
  content: public override void SetTopReturnedObjectsCount(object collection, int topReturnedObjectsCount)
  parameters:
  - id: collection
    type: System.Object
    description: A collection whose maximum number of retrieved objects this method returns.
  - id: topReturnedObjectsCount
    type: System.Int32
    description: The maximum number of objects that the specified collection can retrieve from the database. **0** indicates that the collection can retrieve all objects.
seealso: []
---
When a negative value is passed, an **ArgumentException** is thrown. An example of using this method is provided in the [IObjectSpace.SetTopReturnedObjectsCount](xref:DevExpress.ExpressApp.IObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)) topic.