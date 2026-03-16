---
uid: "403189"
seealso:
- linkId: "403168"
- linkId: "403164"
title: 'How to: Display a List View With Data From a Stored Procedure With a Parameter'
owner: Dmitry Egorov
---
# How to: Display a List View With Data From a Stored Procedure With a Parameter

This example demonstrates how to show a List View for data fetched from a stored procedure that accepts a parameter. This example uses [Non-Persistent Objects](xref:116516) to temporally store data from the stored procedure and the Northwind database.

The Northwind database has the _CustOrderHist_ stored procedure that returns the number of products a customer purchased. In this example, a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) from the Customers List View invokes a pop-up window that shows data from the stored procedure.

## Create the Customers Persistent Class in the Platform-Agnostic Module

In the [platform-agnostic module](xref:118045) (_MySolution.Module_), create the following _Customers_ class:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
using System.ComponentMode.DataAnnotations;

namespace YourSolutionName.Module.BusinessObjects {
    [DefaultClassOptions]
    public class Customers {
        [Key]
        public virtual string CustomerID { get; set; }
        // other properties
    }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)
```csharp
using DevExpress.Persistent.Base;
using DevExpress.Xpo;

namespace YourSolutionName.Module.BusinessObjects {
    [DefaultClassOptions]
    public class Customers : XPLiteObject {
        public Customers(Session session) : base(session) { }
        string fCustomerID;
        [DevExpress.Xpo.Key]
        public string CustomerID {
            get => fCustomerID;
            set => SetPropertyValue(nameof(CustomerID), ref fCustomerID, value);
        }
        // other properties
    }
}
```
***

**File**: _YourSolutionName.Module\\BusinessObjects\\YourSolutionNameDbContext.cs_.

# [C#](#tab/tabid-csharp-efonly)
```csharp
using Microsoft.EntityFrameworkCore;

public class YourSolutionNameEFCoreDbContext : DbContext {
	// ...
	public DbSet<Customers> Customers { get; set; }
}
```
***

## Create Non-Persistent Objects in the Platform-Agnostic Module

1. The _CustOrderHist_ stored procedure returns records with two fields: **ProductName** (string) and **Total** (integer). Create a non-persistent class with corresponding properties in the platform-agnostic module (_MySolution.Module_).

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp.DC;

    namespace YourSolutionName.Module.BusinessObjects {
        [DomainComponent]
        public class OrderHist {
            [DevExpress.ExpressApp.Data.Key]
            public string ProductName { get; internal set; }
            public int Total { get; internal set; }
        }
    }
    ```
    ***

    > [!NOTE]
    > **Internal/Friend** setters are used in the non-persistent class to disable editing the properties because editing is not implemented in this example.

    In the Model Editor, add the **ProductName** column to **OrderHist_ListView** as described in [List View Columns Customization](xref:113679).

2. Create a controller for _Customers_ Views and add a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) in the controller. The scenario in this example requires that a single _Customers_ object is selected. To ensure this, set the Action [SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property to **SelectionDependencyType.RequireSingleObject**.

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    using YourSolutionName.Module.BusinessObjects;

    namespace YourSolutionName.Module.Controllers {
        public class CustomersViewController : ObjectViewController<ObjectView, Customers> {
            public CustomersViewController() {
                PopupWindowShowAction action = new PopupWindowShowAction(this, "Order Hist", DevExpress.Persistent.Base.PredefinedCategory.View);
                action.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
                action.CustomizePopupWindowParams += Action_CustomizePopupWindowParams;
            }

            private void Action_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
                // ...
            }
        }
    }
    ```
    ***

3. In the **CustomizePopupWindowParams** event handler, call the [XafApplication.CreateObjectSpace(Type)](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type)) method to create a **NonPersistentObjectSpace** from the **OrderHist** class and handle the [NonPersistentObjectSpace.ObjectsGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting) event. Call the [XafApplication.CreateListView(IObjectSpace, Type, Boolean)](xref:DevExpress.ExpressApp.XafApplication.CreateListView(DevExpress.ExpressApp.IObjectSpace,System.Type,System.Boolean)) method to create a List View from the **OrderHist** and pass this List View to the **e.View** parameter.

    # [C#](#tab/tabid-csharp)
    ```csharp
    private void Action_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
        NonPersistentObjectSpace objectSpace = (NonPersistentObjectSpace)Application.CreateObjectSpace(typeof(OrderHist));
        objectSpace.ObjectsGetting += ObjectSpace_ObjectsGetting;
        e.View = Application.CreateListView(objectSpace, typeof(OrderHist), true);
    }

    private void ObjectSpace_ObjectsGetting(object sender, ObjectsGettingEventArgs e) {
        // ...
    }
    ```
    ***

4. To allow users to filter and sort a List View, use the **DynamicCollection** class in the **ObjectsGetting** event handler to populate the **e.Objects** collection. The following example demonstrates how to implement this: [How to filter and sort Non-Persistent Objects](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Filtering-Demo).

    > [!NOTE]
    > Filtering and sorting non-persistent object is supported only in the [Client](xref:118449) data access mode. In XAF Blazor, List Views have the [Queryable](xref:402925) data access mode by default. Change the non-persistent List View  data access mode to **Client** in XAF Blazor applications as described in [List View Data Access Modes](xref:113683).

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;
    using System.Collections.Generic;

    // ...
    private void ObjectSpace_ObjectsGetting(object sender, ObjectsGettingEventArgs e) {
        NonPersistentObjectSpace objectSpace = (NonPersistentObjectSpace)sender;
        var collection = new DynamicCollection(objectSpace, e.ObjectType, e.Criteria, e.Sorting, e.InTransaction);
        collection.FetchObjects += DynamicCollection_FetchObjects;
        e.Objects = collection;
    }
    private void DynamicCollection_FetchObjects(object sender, FetchObjectsEventArgs e) {
        Customers customer = (Customers)View.SelectedObjects[0];
        e.Objects = GetDataFromSproc(customer.CustomerID);
        e.ShapeData = true;
    }
    List<OrderHist> GetDataFromSproc(string key) {
        // ...
    }
    ```
    ***

    The **GetDataFromSproc** method should contain ORM-dependent code to get data from a stored procedure.

## Create XPO-Dependent Code to Get Data from a Stored Procedure

Use the [Session.ExecuteQueryWithMetadata](xref:DevExpress.Xpo.Session.ExecuteQueryWithMetadata(System.String)) method to get data from a stored procedure. This method returns column names along with data. Refer to the following article to access data returned by the **ExecuteQueryWithMetadata** method [How to: Access Data in SQL Query Results](xref:9216). 

Use the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) property to access a [Session](xref:DevExpress.Xpo.Session) instance. The created controller is created for a persistent class. Cast the **ViewController.ObjectSpace** property to **XPObjectSpace** to get an **XPObjectSpace** instance in the **GetDataFromSproc** method. Use the [ObjectViewController<ViewType, ObjectType>.ViewCurrentObject](xref:DevExpress.ExpressApp.ObjectViewController`2.ViewCurrentObject) property to get a selected _Customers_ object.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Xpo;
using DevExpress.Xpo.DB;
using DevExpress.Xpo;

// ...
List<OrderHist> GetDataFromSproc(string key) {
    XPObjectSpace persistentObjectSpace = (XPObjectSpace)ObjectSpace;
    Session session = persistentObjectSpace.Session;
    SelectedData results = session.ExecuteQueryWithMetadata($"CustOrderHist @CustomerID={key}");
    Dictionary<string, int> columnNames = new Dictionary<string, int>();
    for (int columnIndex = 0; columnIndex < results.ResultSet[0].Rows.Length; columnIndex++) {
        string columnName = results.ResultSet[0].Rows[columnIndex].Values[0] as string;
        columnNames.Add(columnName, columnIndex);
    }
    List<OrderHist> objects = new List<OrderHist>();
    foreach (SelectStatementResultRow row in results.ResultSet[1].Rows) {
        OrderHist obj = new OrderHist();
        obj.ProductName = row.Values[columnNames["ProductName"]] as string;
        obj.Total = (int)row.Values[columnNames["Total"]];
        objects.Add(obj);
    }
    return objects;
}
```
***

## Create EF Core-Dependent Code to Get Data from a Stored Procedure

In EF Core, use the [DbSet](xref:Microsoft.EntityFrameworkCore.DbSet`1) object's [RelationalQueryableExtensions.FromSqlRaw](xref:Microsoft.EntityFrameworkCore.RelationalQueryableExtensions.FromSqlRaw*) extension method to get data from a stored procedure. Create an entity class that should store data fetched from a stored procedure.

# [C#](#tab/tabid-csharp-efonly)
```csharp
namespace YourSolutionName.Module.BusinessObjects {
    public class CustOrderHist {
        [System.ComponentModel.DataAnnotations.Key]
        public virtual string ProductName { get; set; }
        public virtual int Total { get; set; }
    }
}
```
***

Add the new entity class to the solution's DbContext in the _YourSolutionName.Module\\BusinessObjects\\YourSolutionNameDbContext.cs_ file.

# [C#](#tab/tabid-csharp-efonly)
```csharp
using Microsoft.EntityFrameworkCore;

public class YourSolutionNameEFCoreDbContext : DbContext {
	// ...
	public DbSet<CustOrderHist> CustOrderHists { get; set; }
}
```
***

The created controller is created for a persistent class. Cast the **ViewController.ObjectSpace** property to [EFCoreObjectSpace](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace) to get an **EFCoreObjectSpace** instance in the **GetDataFromSproc** method. Access your **YourSolutionNameEFCoreDbContext** instance from the [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext) property. Call the **YourSolutionNameEFCoreDbContext.Employees.FromSqlRaw** method to get data from a stored procedure. Use the [ObjectViewController<ViewType, ObjectType>.ViewCurrentObject](xref:DevExpress.ExpressApp.ObjectViewController`2.ViewCurrentObject) property to get a selected _Customers_ object.

# [C#](#tab/tabid-csharp-efonly)
```csharp
using DevExpress.ExpressApp.EFCore;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;

// ...
List<OrderHist> GetDataFromSproc(string key) {
    EFCoreObjectSpace persistentObjectSpace = (EFCoreObjectSpace)ObjectSpace;
    YourSolutionNameEFCoreDbContext dbContext = (YourSolutionNameEFCoreDbContext)persistentObjectSpace.DbContext;
    IQueryable<CustOrderHist> results = dbContext.CustOrderHists.FromSqlRaw($"CustOrderHist @CustomerID={key}");
    List<OrderHist> objects = new List<OrderHist>();
    foreach (CustOrderHist coh in results) {               
        OrderHist obj = new OrderHist();
        obj.ProductName = coh.ProductName;
        obj.Total = coh.Total;
        objects.Add(obj);
    }
    return objects;
}
```
***
