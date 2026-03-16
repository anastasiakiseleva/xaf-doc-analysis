---
uid: "403620"
title: Evaluate Scalar Values and Fetch a Portion of Data
owner: Dmitry Egorov
---
# Evaluate Scalar Values and Fetch a Portion of Data

Custom business logic may involve a limited number of business class properties or a limited number of business objects. You may need to evaluate a scalar value calculated at the database level without fetching real objects. To improve the performance and memory consumption, it's possible to fetch business class property value and calculated values needed for the task. 

<!-- Use the following methods to calculate this information.

## In a Controller with the Object Space Methods

[IObjectSpace.GetObjectsQuery](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsQuery``1(System.Boolean))
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObjectsQuery``1(System.Boolean))]

[IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*)
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.CreateDataView(System.Type,System.String,DevExpress.Data.Filtering.CriteriaOperator,System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}))]

[IObjectSpace.SetTopReturnedObjectsCount](xref:DevExpress.ExpressApp.IObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32))
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32))]

[IObjectSpace.Evaluate](xref:DevExpress.ExpressApp.IObjectSpace.Evaluate(System.Type,DevExpress.Data.Filtering.CriteriaOperator,DevExpress.Data.Filtering.CriteriaOperator))
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.Evaluate(System.Type,DevExpress.Data.Filtering.CriteriaOperator,DevExpress.Data.Filtering.CriteriaOperator))]
-->



## Use LINQ

To fetch data in small portions or evaluate scalar values, use the [IObjectSpace.GetObjectsQuery](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsQuery``1(System.Boolean)) method to get an [](xref:System.Linq.IQueryable`1) object and apply a [LINQ](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/) expression to it.


### Get a Portion of Data From a Database

You can fetch only a necessary number of first records. To fetch them, use the [Take](https://learn.microsoft.com/en-us/dotnet/api/system.linq.queryable.take) method.

# [C#](#tab/tabid-csharp)

```csharp
IQueryable<Product> query = this.ObjectSpace.GetObjectsQuery<Product>();
List<Product> top500 = query.Take(500).ToList();
```
***

### Get Only Certain Properties from a Database

To fetch only particular properties of your business class, use [Projection Operations](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/projection-operations) to specify what properties you need to fetch. 

The following example fetches the **ID** and **Name** properties of the **Product** business class and calculates the total amount of sold products from the **Sales** collection property.

# [C#](#tab/tabid-csharp)

```csharp
IQueryable<Product> query = this.ObjectSpace.GetObjectsQuery<Product>();
var list = query.Select(p => new { p.ID, p.Name, Total = p.Sales.Sum(s => s.Count * s.Price) }).ToList();
int id = list[0].ID;
decimal total = list[0].Total;
```
***

This code generates the following SQL query to fetch the required data that does not fetch the rest properties of the **Product** business class.

# [SQL](#tab/tabid-sql)
```SQL
SELECT N0."ID",
       N0."Name",
  (SELECT sum((Cast((N1."Count") AS MONEY) * N1."Price")) AS Res0
   FROM "dbo"."Sale" N1
   WHERE ((N0."ID" = N1."Product")
          AND N1."GCRecord" IS NULL))
FROM "dbo"."Product" N0
```
***

### Evaluate a Scalar Value

You can use LINQ's [Projection Operations](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/projection-operations) to fetch a scalar value. The following example illustrates how to calculate a number of completed **Tasks** of a current **Employee**.

# [C#](#tab/tabid-csharp)

```csharp
Employee employee = (Employee)View.CurrentObject;
IQueryable<Employee> query = ObjectSpace.GetObjectsQuery<Employee>();
int result = query.Where(e => e.ID == employee.ID).Select(e => e.Tasks.Where(t => t.Status == Status.Completed).Count()).Single();
```
***

This expression produces the following SQL query to calculate a scalar value at the database level.

# [SQL](#tab/tabid-sql)
```SQL
SELECT top 2
  (SELECT count(*) AS Res0
   FROM "dbo"."Task" N1
   WHERE ((N0."ID" = N1."Employee")
          AND (N1."Status" = 0)))
FROM "dbo"."Employee" N0
WHERE (N0."OID" = 1)
```
***

## Use ObjectSpace API

### Get a Portion of Data from a Database

When you get a collection of objects using the [IObjectSpace.GetObjects](xref:DevExpress.ExpressApp.IObjectSpace.GetObjects*) method, use the [IObjectSpace.SetTopReturnedObjectsCount](xref:DevExpress.ExpressApp.IObjectSpace.SetTopReturnedObjectsCount(System.Object,System.Int32)) method to limit a number of objects to return.

# [C#](#tab/tabid-csharp)

```csharp
IList objects = objectSpace.GetObjects(typeof(Product));
objectSpace.SetTopReturnedObjectsCount(objects, 500);
```
***

### Get Only Certain Properties from a Database

Use [](xref:DevExpress.ExpressApp.XafDataView) to fetch particular properties of a business class. Use the [IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*) method to create an `XafDataView` instance. The [XafDataView.Expressions](xref:DevExpress.ExpressApp.XafDataView.Expressions) list specifies what properties and [expressions](xref:4928) to fetch.

The following example creates an `XafDataView` instance to fetch the **ID** and **Name** properties of the **Product** business class and calculated the total amount of sold products from the **Sales** collection property.

# [C#](#tab/tabid-csharp)

```csharp
XafDataView dataView = (XafDataView)objectSpace.CreateDataView(
    typeof(Product), "ID;Name;Sales.Sum([Count] * Price)", null, null);
```
***

After this, access a data record by [its index](xref:DevExpress.ExpressApp.XafDataView.Item(System.Int32)). An [](xref:DevExpress.ExpressApp.XafDataViewRecord) object is returned.

# [C#](#tab/tabid-csharp)

```csharp
XafDataViewRecord dataRecord = dataView[0];
```
***

To get a column value from a data record, use the [XafDataViewRecord.Item](xref:DevExpress.ExpressApp.XafDataViewRecord.Item*) property as follows:

# [C#](#tab/tabid-csharp)

```csharp
int id = dataView[0]["ID"];
int total = dataView[0]["Sales.Sum(Count * Price)"];
```
***

### Evaluate a Scalar Value

Use the [IObjectSpace.Evaluate](xref:DevExpress.ExpressApp.IObjectSpace.Evaluate(System.Type,DevExpress.Data.Filtering.CriteriaOperator,DevExpress.Data.Filtering.CriteriaOperator)) method to calculate an [expression](xref:4928). The following example illustrates how to calculate a number of completed **Tasks** of a current **Employee**.

# [C#](#tab/tabid-csharp)

```csharp
CriteriaOperator expression = CriteriaOperator.Parse("Tasks[Status = 'Completed'].Count()");
CriteriaOperator criteria = new BinaryOperator(nameof(Employee.ID), ObjectSpace.GetKeyValue(View.CurrentObject));
int result = (int)ObjectSpace.Evaluate(typeof(Employee), expression, criteria);
```
***

<!-- TODO: ## In XPO Business Class

## In EF Core Business Class -->
