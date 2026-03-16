---
uid: DevExpress.ExpressApp.IObjectSpace.GetExpressionEvaluator(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: GetExpressionEvaluator(Type, CriteriaOperator)
type: Method
summary: Creates an **ExpressionEvaluator** object that is used to evaluate whether objects of the specified type satisfy a particular criteria.
syntax:
  content: ExpressionEvaluator GetExpressionEvaluator(Type type, CriteriaOperator criteria)
  parameters:
  - id: type
    type: System.Type
    description: A **Type** object that is the type of the objects for which the created evaluator works.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **CriteiraOperator** object that is the criteria used to in the expression to be evaluated.
  return:
    type: DevExpress.Data.Filtering.Helpers.ExpressionEvaluator
    description: An **ExpressionEvaluator** object initialized for the specified type.
seealso:
- linkId: DevExpress.ExpressApp.BaseObjectSpace.GetEvaluatorContextDescriptor(System.Type)
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to implement this method. The **BaseObjectSpace.GetExpressionEvaluator** method creates an instance of the **DevExpress.Data.Filtering.Helpers.ExpressionEvaluator** class.