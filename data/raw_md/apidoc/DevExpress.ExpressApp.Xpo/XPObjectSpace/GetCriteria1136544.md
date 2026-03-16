---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetCriteria(System.Object)
name: GetCriteria(Object)
type: Method
summary: Returns the criteria used to filter a particular collection on the server side.
syntax:
  content: public override CriteriaOperator GetCriteria(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection whose server-side filter must be retrieved.
  return:
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** object that specifies the criteria used to filter objects on the server side.
seealso: []
---
Generally, you do not need to use this method, since it is intended for internal use.