---
uid: DevExpress.ExpressApp.BaseObjectSpace.IsObjectFitForCriteria(System.Object,DevExpress.Data.Filtering.CriteriaOperator)
name: IsObjectFitForCriteria(Object, CriteriaOperator)
type: Method
summary: Specifies whether the specified object satisfies the specified criteria.
syntax:
  content: public bool? IsObjectFitForCriteria(object obj, CriteriaOperator criteria)
  parameters:
  - id: obj
    type: System.Object
    description: A persistent object to be tested.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **CriteriaOperator** object representing a criteria to be tested.
  return:
    type: System.Nullable{System.Boolean}
    description: '**true** if the specified object passed as the _obj_ parameter satisfies the criteria passed as the _criteria_ parameter; otherwise, **false**.'
seealso: []
---
This method is intended for internal use only.