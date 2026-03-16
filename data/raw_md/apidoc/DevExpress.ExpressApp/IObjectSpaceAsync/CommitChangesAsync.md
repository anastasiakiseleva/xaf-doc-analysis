---
uid: DevExpress.ExpressApp.IObjectSpaceAsync.CommitChangesAsync(System.Threading.CancellationToken)
name: CommitChangesAsync(CancellationToken)
type: Method
summary: Asynchronously saves all the changes made to the persistent objects that belong to the current Object Space to the database.
syntax:
  content: Task CommitChangesAsync(CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  return:
    type: System.Threading.Tasks.Task
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) object.
seealso: []
---
[!include[CommitChangesAsync](~/templates/CommitChangesAsync.md)]
