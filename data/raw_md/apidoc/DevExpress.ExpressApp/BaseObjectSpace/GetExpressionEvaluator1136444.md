---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetExpressionEvaluator(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: GetExpressionEvaluator(Type, CriteriaOperator)
type: Method
summary: Creates an **ExpressionEvaluator** object that is used to evaluate whether objects of the specified type satisfy a particular criteria.
syntax:
  content: public ExpressionEvaluator GetExpressionEvaluator(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: A **Type** object that is the type of the objects for which the created evaluator works.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **CriteiraOperator** object that is the criteria used to in the expression to be evaluated.
  return:
    type: DevExpress.Data.Filtering.Helpers.ExpressionEvaluator
    description: An **ExpressionEvaluator** object initialized for the specified type.
seealso: []
---
This method creates an instance of the **DevExpress.Data.Filtering.Helpers.ExpressionEvaluator** class.