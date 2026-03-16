---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetFilter(System.Object)
name: GetFilter(Object)
type: Method
summary: Returns the criteria used to filter a particular collection on the client side.
syntax:
  content: public override CriteriaOperator GetFilter(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: An object representing the collection whose client-side filter must be retrieved.
  return:
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** object that specifies the criteria used to filter objects on the client side.
seealso: []
---
Generally, you do not need to use this method since it is intended for internal use.