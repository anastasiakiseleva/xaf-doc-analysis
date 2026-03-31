---
uid: "403617"
title: Load Objects
---
# Load Objects

In your business logic you may need to fetch another object or a collection of objects to calculated values based on that object properties. You can implement the logic to obtain an existing object in a Controller or in a business class.

## Load Objects in a Controller

> [!spoiler][Useful API]
>
> 
> Object Space exposes the following methods to find an existing object.
> 
> [IObjectSpace.FirstOrDefault\<ObjectType>](xref:DevExpress.ExpressApp.IObjectSpace.FirstOrDefault*) 
> :   [!summary-include(DevExpress.ExpressApp.IObjectSpace.FirstOrDefault``1(System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}}))]
> 
> [IObjectSpace.FindObject](xref:DevExpress.ExpressApp.IObjectSpace.FindObject*)
> :   [!summary-include(DevExpress.ExpressApp.IObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean))]
> 
> [IObjectSpace.FindObject\<ObjectType>](xref:DevExpress.ExpressApp.IObjectSpace.FindObject*)
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.FindObject``1(DevExpress.Data.Filtering.CriteriaOperator,System.Boolean))]
> 
> [IObjectSpace.GetObject](xref:DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object))
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object))]
> 
> [IObjectSpace.GetObjectByKey](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectByKey(System.Type,System.Object))
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObjectByKey(System.Type,System.Object))]
> 
> [IObjectSpace.GetObjectByKey\<ObjectType>](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectByKey``1(System.Object))
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObjectByKey``1(System.Object))]
> 
> [IObjectSpace.GetObjectByHandle](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectByHandle(System.String))
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObjectByHandle(System.String))]
> 
> [IObjectSpace.IsObjectFitForCriteria](xref:DevExpress.ExpressApp.IObjectSpace.IsObjectFitForCriteria*)
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.IsObjectFitForCriteria*)]
> 
> ----------------------------
> 
> The following Object Space methods return a collection of objects.
> 
> [IObjectSpace.GetObjects](xref:DevExpress.ExpressApp.IObjectSpace.GetObjects*)
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObjects(System.Type))]
> 
> [IObjectSpace.GetObjects\<T>](xref:DevExpress.ExpressApp.IObjectSpace.GetObjects*)
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObjects``1)]
> 
> [IObjectSpace.CreateCollection](xref:DevExpress.ExpressApp.IObjectSpace.CreateCollection*)
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.CreateCollection*)]
> 
> [IObjectSpace.GetObjectsQuery\<T>](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsQuery``1(System.Boolean))
> :    [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObjectsQuery``1(System.Boolean))]

[!include[<19,22-23><20,23-24>](~/templates/objectspace_getobject.md)]

You can use the [IObjectSpace.GetObjectsQuery\<T>](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsQuery``1(System.Boolean)) method to load objects. It allows you to use [LINQ](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/) expressions to specify the required request.

# [C#](#tab/tabid-csharp)

```csharp
IQueryable<Product> query = this.ObjectSpace.GetObjectsQuery<Product>();
```
***

Business logic can depend on a number of records in a database. In this scenario, use the [IObjectSpace.GetObjectsCount](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsCount(System.Type,DevExpress.Data.Filtering.CriteriaOperator)) method to get a number of records without fetching records.

## In a Data Model (in an XPO Business Class)

An XPO Session available via the [Session](xref:DevExpress.Xpo.PersistentBase.Session) property in a business class implements [methods](xref:DevExpress.Xpo.Session._methods) to find and read an object from a database.

[!include[<7,12-13><7,13-14>](~/templates/createobjectinxpo.md)]

To get a collection of objects in an XPO business class, instantiate a new [](xref:DevExpress.Xpo.XPCollection).

# [C#](#tab/tabid-csharp)

```csharp{9}
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
// ...
public class Order : BaseObject {    
    private XPCollection<Accessory> fAvailableAccessories;
    public XPCollection<Accessory> AvailableAccessories {
        get {
            if (fAvailableAccessories == null) {
                fAvailableAccessories = new XPCollection<Accessory>(Session);
            }
            return fAvailableAccessories;
        }
    }
}

public class Accessory : BaseObject { }
```
***

It's possible to use the [](xref:DevExpress.Xpo.Session) methods like [GetObjects](xref:DevExpress.Xpo.Session.GetObjects(DevExpress.Xpo.Metadata.XPClassInfo,DevExpress.Data.Filtering.CriteriaOperator,DevExpress.Xpo.SortingCollection,System.Int32,System.Boolean,System.Boolean)) to fetch a collection of objects.

## In an EF Core Business Class

Inside an EF Core business class, implement the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface in the class. XAF will automatically assign an Object Space instance to the `IObjectSpaceLink.ObjectSpace` property. Use the assigned Object Space APIs listed above to get an existing object.

[!include[<8,14>](~/templates/createobjectinefcore.md)]
