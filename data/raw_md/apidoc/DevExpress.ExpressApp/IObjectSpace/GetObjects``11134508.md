---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjects``1
name: GetObjects<T>()
type: Method
summary: Retrieves objects of the specified type from the current Object Space. Returns an **IList** collection.
syntax:
  content: IList<T> GetObjects<T>()
  typeParameters:
  - id: T
    description: The @System.Type of objects that are retrieved.
  return:
    type: System.Collections.Generic.IList{{T}}
    description: A [](xref:System.Collections.IList) collection that contains the persistent objects of the specified type.
seealso:
- linkId: "113707"
- linkId: "113711"
---
To load a single object, use the `FindObject` or `FirstOrDefault` method instead of this overload.