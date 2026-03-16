---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.ToListAsync``1(System.Object,System.Threading.CancellationToken)
name: ToListAsync<T>(Object, CancellationToken)
type: Method
summary: Asynchronously enumerates all elements in a collection and saves them to a list.
syntax:
  content: public Task<List<T>> ToListAsync<T>(object collection, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: collection
    type: System.Object
    description: A collection to be enumerated.
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  typeParameters:
  - id: T
    description: The type of elements in the specified collection.
  return:
    type: System.Threading.Tasks.Task{System.Collections.Generic.List{{T}}}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) that returns a list of objects.
seealso: []
---
Use the @DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObjectsQuery``1(System.Boolean) method to get the @DevExpress.Xpo.XPQuery`1 object to pass it as the @DevExpress.ExpressApp.Xpo.XPObjectSpace.ToListAsync``1(System.Object,System.Threading.CancellationToken)'s _collection_ parameter. You can also create this object manually.

[!include[ToListAsync``1](~/templates/ToListAsync``1.md)]
