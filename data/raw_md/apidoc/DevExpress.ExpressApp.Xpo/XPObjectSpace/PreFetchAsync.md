---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.PreFetchAsync(System.Object,System.String[],System.Threading.CancellationToken)
name: PreFetchAsync(Object, String[], CancellationToken)
type: Method
summary: Asynchronously forces associated collection data loading and [delayed](xref:2024) property loading for specified parent objects.
syntax:
  content: public Task PreFetchAsync(object collection, string[] propertyNames, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: collection
    type: System.Object
    description: A collection of parent objects.
  - id: propertyNames
    type: System.String[]
    description: An array of strings which are the names of the associated collection properties or delayed properties.
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  return:
    type: System.Threading.Tasks.Task
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) object.
seealso: []
---
[!include[PreFetchAsync](~/templates/PreFetchAsync.md)]
