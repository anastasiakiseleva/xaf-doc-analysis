---
uid: DevExpress.ExpressApp.IObjectSpace.ApplyFilter(System.Object,DevExpress.Data.Filtering.CriteriaOperator)
name: ApplyFilter(Object, CriteriaOperator)
type: Method
summary: Filters a particular collection on the client side.
syntax:
  content: void ApplyFilter(object collection, CriteriaOperator filter)
  parameters:
  - id: collection
    type: System.Object
    description: A collection to be filtered.
  - id: filter
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** object that specifies the criteria used to filter objects.
seealso: []
---
While the [IObjectSpace.ApplyCriteria](xref:DevExpress.ExpressApp.IObjectSpace.ApplyCriteria(System.Object,DevExpress.Data.Filtering.CriteriaOperator)) method applies criteria used to filter objects on the storage side, the **ApplyFilter** method is intended to filter these objects again, after they are retrieved to the collection. Implement this method if the collection type, with which your Object Space works, supports filtering of this kind.