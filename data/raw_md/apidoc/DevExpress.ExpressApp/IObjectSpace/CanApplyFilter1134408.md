---
uid: DevExpress.ExpressApp.IObjectSpace.CanApplyFilter(System.Object)
name: CanApplyFilter(Object)
type: Method
summary: Indicates whether a particular collection can be filtered on the client side.
syntax:
  content: bool CanApplyFilter(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection whose client-side filtering capability must be determined.
  return:
    type: System.Boolean
    description: '**true**, if the specified collection can be filtered on the client side; otherwise, **false**.'
seealso: []
---
In this method, check whether the objects retrieved to the collection specified as the _collection_ parameter can be filtered again after they have been filtered by the [IObjectSpace.ApplyCriteria](xref:DevExpress.ExpressApp.IObjectSpace.ApplyCriteria(System.Object,DevExpress.Data.Filtering.CriteriaOperator)) method on the storage side.