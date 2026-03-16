---
uid: DevExpress.ExpressApp.XafDataView.Expressions
name: Expressions
type: Property
summary: Specifies data view column names and [expressions](xref:4928) used to compute column values.
syntax:
  content: public IList<DataViewExpression> Expressions { get; set; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{DevExpress.ExpressApp.Utils.DataViewExpression}
    description: An **IList\<**[](xref:DevExpress.ExpressApp.Utils.DataViewExpression)**>** list that specifies data view column names and [expressions](xref:4928) used to compute column values.
seealso: []
---
When the [](xref:DevExpress.ExpressApp.XafDataView) object is instantiated via the [IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*) method overload that takes the _expressions_ parameter of the string type, each column name is a column's expression text.