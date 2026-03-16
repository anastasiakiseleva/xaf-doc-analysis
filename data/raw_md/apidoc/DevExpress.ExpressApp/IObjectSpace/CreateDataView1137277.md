---
uid: DevExpress.ExpressApp.IObjectSpace.CreateDataView(System.Type,System.String,DevExpress.Data.Filtering.CriteriaOperator,System.Collections.Generic.IList{DevExpress.Xpo.SortProperty})
name: CreateDataView(Type, String, CriteriaOperator, IList<SortProperty>)
type: Method
summary: Returns a list of data records retrieved from a database without loading complete business classes (a data view). Values in each data record can be obtained from specific business class properties directly, or be evaluated by the database server using complex expressions.
syntax:
  content: IList CreateDataView(Type objectType, string expressions, CriteriaOperator criteria, IList<SortProperty> sorting)
  parameters:
  - id: objectType
    type: System.Type
    description: The **Type** of requested objects.
  - id: expressions
    type: System.String
    description: A string that contains a semicolon separated list of [expressions](xref:4928) that specify data view column values.
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

> [!NOTE]
> [!include[DataView_PropertyName_Note](~/templates/dataview_propertyname_note111145.md)]

# [C#](#tab/tabid-csharp)

```csharp
XafDataView dataView = (XafDataView)objectSpace.CreateDataView(
    typeof(Product), "ID;Name;Sales.Sum([Count] * Price)", null, null);
```
***
