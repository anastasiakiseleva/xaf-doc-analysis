---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.ReloadObjectAsync(System.Object,System.Threading.CancellationToken)
name: ReloadObjectAsync(Object, CancellationToken)
type: Method
summary: Asynchronously reloads the state of the specified persistent object and its aggregated objects from the data store.
syntax:
  content: public Task<object> ReloadObjectAsync(object obj, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: obj
    type: System.Object
    description: An object which represents the persistent object whose state needs to be reloaded.
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  return:
    type: System.Threading.Tasks.Task{System.Object}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) that returns an object. This object is the object specified by the _obj_ parameter after it has been reloaded.
seealso: []
---
If the specified persistent object is a new object, the **ReloadObjectAsync** method does nothing. To ensure that the persistent object is not a new object, use the [XPObjectSpace.IsNewObject](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.IsNewObject(System.Object)) method.

It is not required that the specified object belong to the current Object Space. If it does not belong, it is retrieved by the current Object Space, and then its state is reloaded.

A **CannotReloadPurgedObjectException** is thrown if the specified persistent object is permanently deleted from the data store.

[!include[ReloadObjectAsync](~/templates/ReloadObjectAsync.md)]
