---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetFilter(System.Object)
name: GetFilter(Object)
type: Method
summary: Returns the criteria used to filter a particular collection on the client side.
syntax:
  content: public virtual CriteriaOperator GetFilter(object collection)
  parameters:
  - id: collection
    type: System.Object
    description: A collection to be tested.
  return:
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** object that specifies the criteria used to filter objects on the client side.
seealso: []
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns `null`, but this behavior is overridden in descendants (see [XPObjectSpace.GetFilter](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.GetFilter(System.Object))).