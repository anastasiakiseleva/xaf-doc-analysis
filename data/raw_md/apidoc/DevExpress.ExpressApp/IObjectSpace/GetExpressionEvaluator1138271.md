---
uid: DevExpress.ExpressApp.IObjectSpace.GetExpressionEvaluator(DevExpress.Data.Filtering.Helpers.EvaluatorContextDescriptor,DevExpress.Data.Filtering.CriteriaOperator)
name: GetExpressionEvaluator(EvaluatorContextDescriptor, CriteriaOperator)
type: Method
summary: Creates an **ExpressionEvaluator** object that is used to evaluate whether objects of the specified type satisfy a particular criteria.
syntax:
  content: ExpressionEvaluator GetExpressionEvaluator(EvaluatorContextDescriptor evaluatorContextDescriptor, CriteriaOperator criteria)
  parameters:
  - id: evaluatorContextDescriptor
    type: DevExpress.Data.Filtering.Helpers.EvaluatorContextDescriptor
    description: An **EvaluatorContextDescriptor** object.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **CriteiraOperator** object that is the criteria used to in the expression to be evaluated.
  return:
    type: DevExpress.Data.Filtering.Helpers.ExpressionEvaluator
    description: An **ExpressionEvaluator** object initialized for the specified type.
seealso: []
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to implement this method. The **BaseObjectSpace.GetExpressionEvaluator** method creates an instance of the **DevExpress.Data.Filtering.Helpers.ExpressionEvaluator** class.