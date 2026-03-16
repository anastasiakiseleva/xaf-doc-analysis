---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetCriteria(System.Object)
name: GetCriteria(Object)
type: Method
summary: Returns the criteria used to filter a particular collection on the server side.
syntax:
  content: public virtual CriteriaOperator GetCriteria(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection whose server-side filter must be retrieved.
  return:
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** object that specifies the criteria used to filter objects on the server side.
seealso: []
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns `null`, but this behavior is overridden in descendants (see [EFCoreObjectSpace.GetCriteria](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.GetCriteria(System.Object)) and [XPObjectSpace.GetCriteria](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.GetCriteria(System.Object))).