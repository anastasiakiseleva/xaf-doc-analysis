---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.FindObjectAsync``1(DevExpress.Data.Filtering.CriteriaOperator,System.Boolean,System.Threading.CancellationToken)
name: FindObjectAsync<ObjectType>(CriteriaOperator, Boolean, CancellationToken)
type: Method
summary: Asynchronously searches for an object that matches the specified criteria. The specified generic parameter determines the object's type.
syntax:
  content: public Task<ObjectType> FindObjectAsync<ObjectType>(CriteriaOperator criteria, bool inTransaction, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
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
  typeParameters:
  - id: ObjectType
    description: The type of objects to search for.
  return:
    type: System.Threading.Tasks.Task{{ObjectType}}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) that returns an object. This object represents a persistent object that matches the specified criteria. `null` if no persistent object is found that matches the criteria.
seealso: []
---
[!include[FindObjectAsync``1_1](~/templates/FindObjectAsync``1_1.md)]
