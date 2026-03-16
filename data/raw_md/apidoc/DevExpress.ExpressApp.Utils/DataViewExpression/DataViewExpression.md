---
uid: DevExpress.ExpressApp.Utils.DataViewExpression
name: DataViewExpression
type: Class
summary: Specifies a data view column name and  [expression](xref:4928) used to compute the column value.
syntax:
  content: public class DataViewExpression
seealso:
- linkId: DevExpress.ExpressApp.Utils.DataViewExpression._members
  altText: DataViewExpression Members
- linkId: DevExpress.ExpressApp.IObjectSpace.CreateDataView*
---
Use this class when it is required to create a list of data records retrieved from a database without loading complete business classes (a data view). Values in each data record can be obtained from specific business class properties directly, or be evaluated by the database server using complex expressions. The **IList\<**[](xref:DevExpress.ExpressApp.Utils.DataViewExpression)**>** list can be passed to the [IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*) method, [XafDataView](xref:DevExpress.ExpressApp.XafDataView.#ctor(DevExpress.ExpressApp.IObjectSpace,System.Type,System.Collections.Generic.IList{DevExpress.ExpressApp.Utils.DataViewExpression},DevExpress.Data.Filtering.CriteriaOperator,System.Collections.Generic.IList{DevExpress.Xpo.SortProperty})) constructor or [XafDataView.Expressions](xref:DevExpress.ExpressApp.XafDataView.Expressions) property.

# [C#](#tab/tabid-csharp)

```csharp
List<DataViewExpression> dataViewExpressions = new List<DataViewExpression>();
dataViewExpressions.Add(
    new DataViewExpression("ID", new OperandProperty("ID")));
dataViewExpressions.Add(new DataViewExpression(
    "Name.UpperCase", new FunctionOperator(FunctionOperatorType.Upper, new OperandProperty("Name"))));
dataViewExpressions.Add(new DataViewExpression(
    "Count", new AggregateOperand("Sales", Aggregate.Count)));
var dataView = objectSpace.CreateDataView(typeof(Sale), dataViewExpressions, null, null);
```
***