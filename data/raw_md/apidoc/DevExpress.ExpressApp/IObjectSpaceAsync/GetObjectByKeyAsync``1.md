---
uid: DevExpress.ExpressApp.IObjectSpaceAsync.GetObjectByKeyAsync``1(System.Object,System.Threading.CancellationToken)
name: GetObjectByKeyAsync<ObjectType>(Object, CancellationToken)
type: Method
summary: Returns the persistent object that has the specified value for its key property.
syntax:
  content: Task<ObjectType> GetObjectByKeyAsync<ObjectType>(object key, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: key
    type: System.Object
    description: An object that is the persistent object's key property value.
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  typeParameters:
  - id: ObjectType
    description: The type of an object to search for.
  return:
    type: System.Threading.Tasks.Task{{ObjectType}}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) that returns the searched object. `null` if no persistent object is found with the specified key.
seealso: []
---
The **GetObjectByKeyAsync** method searches the memory for the object that has the specified value for its key property. If such an object is found, it is not reloaded from the database. Otherwise, the object is retrieved from the database.

To get the key property value, use the [IObjectSpace.GetKeyValue](xref:DevExpress.ExpressApp.IObjectSpace.GetKeyValue(System.Object)) method.

[!include[GetObjectByKeyAsync``1](~/templates/GetObjectByKeyAsync``1.md)]
