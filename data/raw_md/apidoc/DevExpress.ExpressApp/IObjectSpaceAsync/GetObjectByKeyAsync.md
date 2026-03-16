---
uid: DevExpress.ExpressApp.IObjectSpaceAsync.GetObjectByKeyAsync(System.Type,System.Object,System.Threading.CancellationToken)
name: GetObjectByKeyAsync(Type, Object, CancellationToken)
type: Method
summary: Returns the persistent object that has the specified value for its key property.
syntax:
  content: Task<object> GetObjectByKeyAsync(Type objectType, object key, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object that is the type of objects to search for.
  - id: key
    type: System.Object
    description: An object that is the persistent object's key property value.
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  return:
    type: System.Threading.Tasks.Task{System.Object}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) that returns the searched object. `null` if no persistent object is found with the specified key.
seealso: []
---
The **GetObjectByKeyAsync** method searches the memory for the object that has the specified value for its key property. If such an object is found, it is not reloaded from the database. Otherwise, the object is retrieved from the database.

To get the key property value, use the @DevExpress.ExpressApp.IObjectSpace.GetKeyValue(System.Object) method.

[!include[GetObjectByKeyAsync](~/templates/GetObjectByKeyAsync.md)]
