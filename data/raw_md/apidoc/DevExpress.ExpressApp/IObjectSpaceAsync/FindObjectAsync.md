---
uid: DevExpress.ExpressApp.IObjectSpaceAsync.FindObjectAsync(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean,System.Threading.CancellationToken)
name: FindObjectAsync(Type, CriteriaOperator, Boolean, CancellationToken)
type: Method
summary: Asynchronously searches for an object that matches the specified criteria.
syntax:
  content: Task<object> FindObjectAsync(Type objectType, CriteriaOperator criteria, bool inTransaction, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of objects to search for.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) descendant which represents the criteria the persistent object must match.
  - id: inTransaction
    type: System.Boolean
    description: '**true**, to enable the [InTransaction mode](xref:DevExpress.Xpo.Session.InTransactionMode); otherwise, **false**.'
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  return:
    type: System.Threading.Tasks.Task{System.Object}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) that returns an object. This object represents a persistent object that matches the specified criteria. `null` if no persistent object that matches the criteria is found.
seealso: []
---
[!include[FindObjectAsync](~/templates/FindObjectAsync.md)]
