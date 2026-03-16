---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjects(System.Type)
name: GetObjects(Type)
type: Method
summary: Retrieves objects of the specified type from the current Object Space. Returns an **IList** collection.
syntax:
  content: IList GetObjects(Type type)
  parameters:
  - id: type
    type: System.Type
    description: The type of objects that are retrieved.
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) collection that contains the persistent objects of the specified type.
seealso:
- linkId: "113707"
- linkId: "113711"
---
Use the FindObject overload with a *criteria* parameter instead of this overload.