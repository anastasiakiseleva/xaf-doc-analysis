---
uid: DevExpress.ExpressApp.XafDataView
name: XafDataView
type: Class
summary: A lightweight read-only list of data records (a data view) retrieved from a database without loading complete business objects. Can be queried much more quickly than a real objects collection.
syntax:
  content: 'public abstract class XafDataView : IBindingList, ICollection, IEnumerable, IList, ITypedList, IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.XafDataView._members
  altText: XafDataView Members
---
You can query data via the **XafDataView**. To create an instance of the **XafDataView**, use the [IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*) method.

The data view column names and [expressions](xref:4928) used to compute column values are specified by the [XafDataView.Expressions](xref:DevExpress.ExpressApp.XafDataView.Expressions) list. By default, this list is empty and you should populate it manually. Both simple properties and complex expressions can be passed via the _expressions_ parameter. The valid separator is a semicolon (;).

# [C#](#tab/tabid-csharp)

```csharp
XafDataView dataView = (XafDataView)objectSpace.CreateDataView(
    typeof(Product), "ID;Name;Sales.Sum([Count] * Price)", null, null);
```
***

Alternatively, you can pass the **IList\<**[](xref:DevExpress.ExpressApp.Utils.DataViewExpression)**>** list via the _expressions_ parameter. The data can be filtered and sorted with the _criteria_ and _sorting_ parameters.

# [C#](#tab/tabid-csharp)

```csharp
List<DataViewExpression> dataViewExpressions = new List<DataViewExpression>();
dataViewExpressions.Add(
    new DataViewExpression("ID", new OperandProperty("ID")));
dataViewExpressions.Add(new DataViewExpression(
    "Name.UpperCase", new FunctionOperator(FunctionOperatorType.Upper, new OperandProperty("Name"))));
dataViewExpressions.Add(new DataViewExpression(
    "Count", new AggregateOperand("Sales", Aggregate.Count)));
CriteriaOperator criteria = new BinaryOperator(
    "Sales.Count", 0, BinaryOperatorType.Greater);
SortProperty[] sorting = new SortProperty[] { 
    new SortProperty("Name", SortingDirection.Ascending)
};
EFCoreDataView dataView = new EFCoreDataView(objectSpace, typeof(Sale), dataViewExpressions, criteria, sorting);
```
***

When you access a particular data record by its index (see [XafDataView.Item](xref:DevExpress.ExpressApp.XafDataView.Item(System.Int32))), an [](xref:DevExpress.ExpressApp.XafDataViewRecord) object is returned.

# [C#](#tab/tabid-csharp)

```csharp
XafDataViewRecord dataRecord = dataView[0];
```
***

To get a column value within a particular data record, use the [XafDataViewRecord.Item](xref:DevExpress.ExpressApp.XafDataViewRecord.Item*) property as follows:

# [C#](#tab/tabid-csharp)

```csharp
int id = dataView[0]["ID"];
```
***

Here, the "ID" string is the name of the column within the [XafDataView.Expressions](xref:DevExpress.ExpressApp.XafDataView.Expressions) list. If you use a semicolon-separated string to specify the columns set in the **XafDataView** constructor, the column name coincides with the expression text:

# [C#](#tab/tabid-csharp)

```csharp
int total = dataView[0]["Sales.Sum(Count * Price)"];
```
***

Data records are not retrieved from the database when the **XafDataView** object is created. Instead, the database is queried when you access a specific record by its index or call one of the following methods for the first time:

* [IBindingList.Find](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.ibindinglist.find#System_ComponentModel_IBindingList_Find_System_ComponentModel_PropertyDescriptor_System_Object_)
* [IEnumerable.GetEnumerator](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable.getenumerator#System_Collections_IEnumerable_GetEnumerator)
* [XafDataView.Contains](xref:DevExpress.ExpressApp.XafDataView.Contains(System.Object))
* [XafDataView.CopyTo](xref:DevExpress.ExpressApp.XafDataView.CopyTo(System.Array,System.Int32))
* [XafDataView.Count](xref:DevExpress.ExpressApp.XafDataView.Count)
* [XafDataView.IndexOf](xref:DevExpress.ExpressApp.XafDataView.IndexOf(System.Object))

Later, the cached data records are used by these methods. To refresh data, use the [XafDataView.Reload](xref:DevExpress.ExpressApp.XafDataView.Reload) method, which clears the cache.

You can limit the number of retrieved data records by using the [XafDataView.TopReturnedObjectsCount](xref:DevExpress.ExpressApp.XafDataView.TopReturnedObjectsCount) property.

An **XafDataView** implements the [IBindingList](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.ibindinglist) and [ITypedList](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.itypedlist) interfaces, so it can serve as a data source for a visual data-aware control.

The **XafDataView** class has two ORM-specific descendants. Depending on the current Object Space type, the [IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*) method returns either `DevExpress.ExpressApp.EFCore.EFCoreDataView` (for Entity Framework Core) or [](xref:DevExpress.ExpressApp.Xpo.XpoDataView) (for XPO) object.
