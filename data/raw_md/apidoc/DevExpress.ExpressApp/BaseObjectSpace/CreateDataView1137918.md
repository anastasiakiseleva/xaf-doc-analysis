---
uid: DevExpress.ExpressApp.BaseObjectSpace.CreateDataView(System.Type,System.Collections.Generic.IList{DevExpress.ExpressApp.Utils.DataViewExpression},DevExpress.Data.Filtering.CriteriaOperator,System.Collections.Generic.IList{DevExpress.Xpo.SortProperty})
name: CreateDataView(Type, IList<DataViewExpression>, CriteriaOperator, IList<SortProperty>)
type: Method
summary: Returns a list of data records retrieved from the database without loading complete business classes (a data view).
syntax:
  content: public IList CreateDataView(Type objectType, IList<DataViewExpression> expressions, CriteriaOperator criteria, IList<SortProperty> sorting)
  parameters:
  - id: objectType
    type: System.Type
    description: A **Type** of requested objects.
  - id: expressions
    type: System.Collections.Generic.IList{DevExpress.ExpressApp.Utils.DataViewExpression}
    description: An **IList\<**[](xref:DevExpress.ExpressApp.Utils.DataViewExpression)**>** list that specifies data view column names and [expressions](xref:4928) used to compute column values. These column names can be used for sorting and filtering the data view via the _criteria_ and _sorting_ parameters.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) object that specifies criteria associated with the data view.
  - id: sorting
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: An **IList\<**[](xref:DevExpress.Xpo.SortProperty)**>** collection whose elements identify the sorted columns within the data view.
  return:
    type: System.Collections.IList
    description: An **IList** object that returns a lightweight list of data records.
seealso: []
---
This method does not return real objects. Instead, a lightweight read-only list of data records that can be viewed much more quickly than a real objects collection is returned.

This method result can be directly cast to [](xref:DevExpress.ExpressApp.XafDataView).