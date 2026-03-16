---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObjectAsync(System.Object,System.Threading.CancellationToken)
name: GetObjectAsync(Object, CancellationToken)
type: Method
summary: Asynchronously retrieves an object that corresponds to an @DevExpress.ExpressApp.IObjectRecord wrapper or object from another Object Space.
syntax:
  content: public Task<object> GetObjectAsync(object obj, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: obj
    type: System.Object
    description: An object that represents a template object from another Object Space.
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  return:
    type: System.Threading.Tasks.Task{System.Object}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) that returns an object. This object represents the evaluated value.
seealso: []
---
This method retrieves the object specified as the _obj_ parameter from the database via the current Object Space's [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session). If the passed object is not persistent, it's returned as is.

[!include[GetObjectAsync](~/templates/GetObjectAsync.md)]
