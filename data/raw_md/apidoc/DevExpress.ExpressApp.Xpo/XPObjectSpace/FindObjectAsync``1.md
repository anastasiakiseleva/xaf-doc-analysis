---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.FindObjectAsync``1(DevExpress.Data.Filtering.CriteriaOperator,System.Threading.CancellationToken)
name: FindObjectAsync<ObjectType>(CriteriaOperator, CancellationToken)
type: Method
summary: Asynchronously searches for an object that matches the specified criteria. This object's type is designated by the specified generic parameter.
syntax:
  content: public Task<ObjectType> FindObjectAsync<ObjectType>(CriteriaOperator criteria, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) descendant which represents the criteria the persistent object must match.
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  typeParameters:
  - id: ObjectType
    description: A type of objects to search for.
  return:
    type: System.Threading.Tasks.Task{{ObjectType}}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) that returns an object. This object represents a persistent object that matches the specified criteria. `null` if no persistent object is found that matches the criteria.
seealso: []
---
[!include[FindObjectAsync``1](~/templates/FindObjectAsync``1.md)]
