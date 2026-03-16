---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjects(System.Type)
name: GetObjects(Type)
type: Method
summary: Returns an **IList** collection of objects of the specified type, retrieved to the current Object Space.
syntax:
  content: public IList GetObjects(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of the objects to be retrieved.
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) collection that contains the persistent objects of the specified type.
seealso: []
---
To get objects of the specified type, this method invokes a protected virtual **CreateCollection** method that does nothing and returns null. So, the details on how the objects are retrieved depend on how the **CreateCollection** method is overridden in a particular descendant of the **BaseObjectSpace** class.