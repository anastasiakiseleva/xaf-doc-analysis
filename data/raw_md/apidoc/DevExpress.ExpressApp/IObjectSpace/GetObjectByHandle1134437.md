---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjectByHandle(System.String)
name: GetObjectByHandle(String)
type: Method
summary: Returns the object with the specified handle.
syntax:
  content: object GetObjectByHandle(string handle)
  parameters:
  - id: handle
    type: System.String
    description: A string holding the key property value and type of the specified object, representing the handle of the object that will be retrieved.
  return:
    type: System.Object
    description: An object which has the specified handle.
seealso: []
---
The object handle is a string of the following format:

``Solution1.Module.BusinessObjects.MyEntityObject(1)``

Here, **Solution1.Module.BusinessObjects.MyEntityObject** is the [FullName](https://learn.microsoft.com/en-us/dotnet/api/system.type.fullname#System_Type_FullName) of the object type and **1** is the object's key property value. To get the handle of an existing object, use the [IObjectSpace.GetObjectHandle](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectHandle(System.Object)) method.

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObjectByHandle** method. It's implemented in the **BaseObjectSpace** class. The **BaseObjectSpace.GetObjectByHandle** method parses the handler passed as the _handle_ parameter using the **DevExpress.ExpressApp.ObjectHandleHelper** class and calls the [BaseObjectSpace.GetObjectByKey](xref:DevExpress.ExpressApp.BaseObjectSpace.GetObjectByKey(System.Type,System.Object)) method to get the object to return.
