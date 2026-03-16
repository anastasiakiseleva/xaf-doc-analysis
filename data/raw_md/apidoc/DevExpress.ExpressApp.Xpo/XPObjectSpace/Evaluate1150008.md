---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.Evaluate(System.Type,DevExpress.Data.Filtering.CriteriaOperator,DevExpress.Data.Filtering.CriteriaOperator)
name: Evaluate(Type, CriteriaOperator, CriteriaOperator)
type: Method
summary: Evaluates the specified [criteria](xref:4928) for business objects of the given type.
syntax:
  content: public override object Evaluate(Type objectType, CriteriaOperator expression, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object that identifies the type of objects against which the expression will be evaluated.
  - id: expression
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) object that specifies the expression to evaluate.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) object that specifies the filter criteria. The objects that match this criteria will be used to evaluate the expression.
  return:
    type: System.Object
    description: The value evaluated.
seealso: []
---
To construct _expression_ and _criteria_, the static [CriteriaOperator.Parse](xref:DevExpress.Data.Filtering.CriteriaOperator.Parse*) method can be used. It takes a string representation of the required expression and retrieves the [](xref:DevExpress.Data.Filtering.CriteriaOperator) object that corresponds to this expression.