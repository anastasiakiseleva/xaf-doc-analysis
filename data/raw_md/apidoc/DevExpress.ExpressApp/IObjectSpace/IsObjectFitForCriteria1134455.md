---
uid: DevExpress.ExpressApp.IObjectSpace.IsObjectFitForCriteria(System.Type,System.Object,DevExpress.Data.Filtering.CriteriaOperator)
name: IsObjectFitForCriteria(Type, Object, CriteriaOperator)
type: Method
summary: Specifies whether a particular object satisfies the specified criteria.
syntax:
  content: bool? IsObjectFitForCriteria(Type objectType, object obj, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of the object to be tested.
  - id: obj
    type: System.Object
    description: A persistent object to be tested.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A `CriteriaOperator` object representing a criteria to be tested.
  return:
    type: System.Nullable{System.Boolean}
    description: '`true` if the specified object passed as the _obj_ parameter satisfies the criteria passed as the _criteria_ parameter; otherwise, `false`. `null` if the method could not return a value due to an exception.'
seealso: []
---
To learn how to specify a criteria correctly, refer to the [Ways to Build Criteria](xref:113052), [Criteria Operators](xref:2129), [How to: Build Complex Criteria](xref:2047) and [How to: Build Simple Criteria](xref:2132) topics in the XPO documentation.

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, you do not have to implement the `IsObjectFitForCriteria` method. It is implemented by the `BaseObjectSpace` class. In this method, the expression evaluator provided by the [BaseObjectSpace.GetExpressionEvaluator](xref:DevExpress.ExpressApp.BaseObjectSpace.GetExpressionEvaluator*) method is used to check whether the specified object fits for the specified criteria. The type passed as the _objectType_ parameter must be assignable from the type of the object passed as the _obj_ parameter.