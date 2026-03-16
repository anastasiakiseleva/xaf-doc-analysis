---
uid: DevExpress.ExpressApp.IObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)
name: SetTopReturnedObjectsCount(Object, Int32)
type: Method
summary: Returns the maximum number of objects to be retrieved by the specified collection from a data store.
syntax:
  content: void SetTopReturnedObjectsCount(object collection, int topReturnedObjects)
  parameters:
  - id: collection
    type: System.Object
    description: A collection from which a specific number of objects can be retrieved.
  - id: topReturnedObjects
    type: System.Int32
    description: An integer value specifying the maximum number of objects that can be retrieved from the database by the specified collection.
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)
---
The **SetTopReturnedObjectsCount** method sets the maximum number of objects that can be retrieved by the specified collection, if this collection type is supported by the current [Object Space](xref:113707).

Below is an example of using this method:

# [C#](#tab/tabid-csharp)

```csharp
IList objects = objectSpace.GetObjects(typeof(Product));
objectSpace.SetTopReturnedObjectsCount(objects, 500);
```
***