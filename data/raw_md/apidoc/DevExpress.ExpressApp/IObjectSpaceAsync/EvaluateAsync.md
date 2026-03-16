---
uid: DevExpress.ExpressApp.IObjectSpaceAsync.EvaluateAsync(System.Type,DevExpress.Data.Filtering.CriteriaOperator,DevExpress.Data.Filtering.CriteriaOperator,System.Threading.CancellationToken)
name: EvaluateAsync(Type, CriteriaOperator, CriteriaOperator, CancellationToken)
type: Method
summary: Asynchronously evaluates the specified [criteria](xref:4928) for business objects of the given type.
syntax:
  content: Task<object> EvaluateAsync(Type objectType, CriteriaOperator expression, CriteriaOperator criteria, CancellationToken cancellationToken = default(CancellationToken))
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object that identifies the type of objects against which the expression is evaluated.
  - id: expression
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) object that specifies the expression to evaluate.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) object that specifies the filter criteria. The objects that match this criteria are used to evaluate the expression.
  - id: cancellationToken
    type: System.Threading.CancellationToken
    defaultValue: "null"
    description: A [CancellationToken](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) object that delivers a cancellation notice to the running operation.
  return:
    type: System.Threading.Tasks.Task{System.Object}
    description: A [Task](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1) that returns an object. This object represents the evaluated value. `null` if no persistent object is found that matches the criteria.
seealso: []
---
You can use the static [CriteriaOperator.Parse](xref:DevExpress.Data.Filtering.CriteriaOperator.Parse*) method to construct the _expression_ and _criteria_. This method takes a string representation of the required expression and creates the [](xref:DevExpress.Data.Filtering.CriteriaOperator) object that corresponds to this expression.

[!include[EvaluateAsync](~/templates/EvaluateAsync.md)]
