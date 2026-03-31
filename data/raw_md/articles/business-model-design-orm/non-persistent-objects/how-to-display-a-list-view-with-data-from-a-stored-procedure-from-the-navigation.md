---
uid: "403164"
seealso:
- linkId: "403168"
- linkId: "403189"
title: 'How to: Display a List View With Data From a Stored Procedure From the Navigation'
---
# How to: Display a List View With Data From a Stored Procedure From the Navigation

This example demonstrates how to show a List View with data fetched from a stored procedure from the Navigation. This example uses the [Non-Persistent Objects](xref:116516) to temporally store data from the stored procedure and the Northwind database. The stored procedure is defined as follows:

# [SQL](#tab/tabid-sql)
```SQL
CREATE Procedure GetEmployees
AS
    SET NOCOUNT ON;
    SELECT * FROM Employees
GO
```
***

## Create Non-Persistent Objects in the Platform-Agnostic Module

1. In the [platform-agnostic module](xref:118045) (_MySolution.Module_), create the following non-persistent class:

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp.DC;
    using DevExpress.Persistent.Base;

    namespace YourSolutionName.Module.BusinessObjects {
        [DomainComponent, DefaultClassOptions]
        public class MyNonPersistentObject {
            [DevExpress.ExpressApp.Data.Key]
            public int EmployeeID { get; internal set; }
            public string FirstName { get; internal set; }
            public string LastName { get; internal set; }
            public string Title { get; internal set; }
        }
    }
    ```

    ***

    > [!NOTE]
    > **Internal/Friend** setters are used in the non-persistent class to disable editing the properties because editing is not implemented in this example.

2. Handle the @DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated event in the Application Builder code to subscribe to the `NonPersistentObjectSpace` events as described in the following help topic: [How to: Display a Non-Persistent Object's List View from the Navigation](xref:114052).

    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;
    // ...
    builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
        NonPersistentObjectSpace npos = context.ObjectSpace as NonPersistentObjectSpace;
        if (npos != null) {
            // ...
        }
    };
    ```

    ***

3. ORM-dependent code executes a stored procedure (the code uses [](xref:DevExpress.Xpo.Session) in XPO and [DbContext](xref:Microsoft.EntityFrameworkCore.DbContext) in EF Core). You can access the `Session` or `DbContext` through the corresponding persistent `ObjectSpace`. To allow the `NonPersistentObjectSpace` to access persistent `ObjectSpaces`, populate the [CompositeObjectSpace.AdditionalObjectSpaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) collection in the `ObjectSpaceCreated` event handler.

    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

    # [C#](#tab/tabid-csharp)
    ```csharp{6-8}
    using DevExpress.ExpressApp;
    // ...
	builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
        CompositeObjectSpace os = context.ObjectSpace as CompositeObjectSpace;
        if (os != null && !(os.Owner is CompositeObjectSpace)) {
            var objectSpaceProviderService = context.ServiceProvider.GetRequiredService<IObjectSpaceProviderService>();
            var objectSpaceCustomizerService = context.ServiceProvider.GetRequiredService<IObjectSpaceCustomizerService>();
            os.PopulateAdditionalObjectSpaces(objectSpaceProviderService, objectSpaceCustomizerService);
        }
        NonPersistentObjectSpace npos = context.ObjectSpace as NonPersistentObjectSpace;
        if (npos != null) {
            // ...
        }
	};
	// ...
    ```

    ***

4. To be able to filter and sort a List View, use the `DynamicCollection` class in the `ObjectsGetting` event handler to populate the `e.Objects` collection. To separate the Module code from business logic to fetch data, create an adapter class to handle the `NonPersistentObjectSpace` events. The following example demonstrates how to implement this: [How to filter and sort Non-Persistent Objects](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Filtering-Demo).

    > [!NOTE]
    > The capability to filter and sort non-persistent objects is supported only in [Client](xref:118449) data access mode. In XAF Blazor, the default data access mode for List Views is [Queryable](xref:402925). Change the non-persistent List View's data access mode to `Client` in XAF Blazor applications as described in the following topic: [List View Data Access Modes](xref:113683).

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;
    using System.Collections.Generic;

    namespace YourSolutionName.Module.BusinessObjects {
        class MyNonPersistentObjectAdapter {
            NonPersistentObjectSpace objectSpace;
            public MyNonPersistentObjectAdapter(NonPersistentObjectSpace npos) {
                objectSpace = npos;
                objectSpace.ObjectsGetting += Npos_ObjectsGetting;
            }
            private void Npos_ObjectsGetting(object sender, ObjectsGettingEventArgs e) {
                if (e.ObjectType != typeof(MyNonPersistentObject)) {
                    return;
                }
                var collection = new DynamicCollection(objectSpace, e.ObjectType, e.Criteria, e.Sorting, e.InTransaction);
                collection.FetchObjects += DynamicCollection_FetchObjects;
                e.Objects = collection;
            }
            private void DynamicCollection_FetchObjects(object sender, FetchObjectsEventArgs e) {
                if (e.ObjectType == typeof(MyNonPersistentObject)) {
                    e.Objects = GetDataFromSproc();
                    e.ShapeData = true;
                }
            }
            List<MyNonPersistentObject> GetDataFromSproc() {
                // ...
            }
        }
    }
    ```

    ***

    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

    # [C#](#tab/tabid-csharp)
    ```csharp{12}
    using DevExpress.ExpressApp;
    // ...
	builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
        CompositeObjectSpace os = context.ObjectSpace as CompositeObjectSpace;
        if (os != null && !(os.Owner is CompositeObjectSpace)) {
            var objectSpaceProviderService = context.ServiceProvider.GetRequiredService<IObjectSpaceProviderService>();
            var objectSpaceCustomizerService = context.ServiceProvider.GetRequiredService<IObjectSpaceCustomizerService>();
            os.PopulateAdditionalObjectSpaces(objectSpaceProviderService, objectSpaceCustomizerService);
        }
        NonPersistentObjectSpace npos = context.ObjectSpace as NonPersistentObjectSpace;
        if (npos != null) {
            new MyNonPersistentObjectAdapter(npos);
        }
	};
	// ...
    ```

    ***

    The `GetDataFromSproc` method should contain ORM-dependent code to get data from a stored procedure.

## Create XPO-Dependent Code to Get Data from a Stored Procedure

In XPO, use the [Session.ExecuteQueryWithMetadata](xref:DevExpress.Xpo.Session.ExecuteQueryWithMetadata(System.String)) method to get data from a stored procedure. This method returns column names along with data. Refer to the following help topic for information on how to access data returned by the `ExecuteQueryWithMetadata` method: [How to: Access Data in SQL Query Results](xref:9216).

Use the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) property to access a [Session](xref:DevExpress.Xpo.Session) instance. You can access an `XPObjectSpace` instance from the [CompositeObjectSpace.AdditionalObjectSpaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) collection.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Xpo;
using DevExpress.Xpo;
using DevExpress.Xpo.DB;
using System.Linq;

class MyNonPersistentObjectAdapter {
    // ...
    List<MyNonPersistentObject> GetDataFromSproc() {
        XPObjectSpace persistentObjectSpace = objectSpace.AdditionalObjectSpaces.OfType<XPObjectSpace>().First();
        Session session = persistentObjectSpace.Session;
        SelectedData results = session.ExecuteQueryWithMetadata("GetEmployees");
        Dictionary<string, int> columnNames = new Dictionary<string, int>();
        for (int columnIndex = 0; columnIndex < results.ResultSet[0].Rows.Length; columnIndex++) {
            string columnName = results.ResultSet[0].Rows[columnIndex].Values[0] as string;
            columnNames.Add(columnName, columnIndex);
        }
        List<MyNonPersistentObject> objects = new List<MyNonPersistentObject>();
        foreach (SelectStatementResultRow row in results.ResultSet[1].Rows) {
            MyNonPersistentObject obj = new MyNonPersistentObject();
            obj.EmployeeID = (int)row.Values[columnNames["EmployeeID"]];
            obj.FirstName = row.Values[columnNames["FirstName"]] as string;
            obj.LastName = row.Values[columnNames["LastName"]] as string;
            obj.Title = row.Values[columnNames["Title"]] as string;
            objects.Add(obj);
        }
        return objects;
    }
}
```

***

## Create EF Core-Dependent Code to Get Data from a Stored Procedure

In EF Core, use the [DbSet](xref:Microsoft.EntityFrameworkCore.DbSet`1) object's [RelationalQueryableExtensions.FromSqlRaw](xref:Microsoft.EntityFrameworkCore.RelationalQueryableExtensions.FromSqlRaw*) extension method to get data from a stored procedure. Create an entity class that should store data fetched from a stored procedure.

# [C#](#tab/tabid-csharp1)
```csharp
namespace YourSolutionName.Module.BusinessObjects {
    public class Employees {
        [System.ComponentModel.DataAnnotations.Key]
        public virtual int EmployeeID { get; set; }
        public virtual string FirstName { get; set; }
        public virtual string LastName { get; set; }
        public virtual string Title { get; set; }
    }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
***

Add the new entity class to the solution's DbContext in the _YourSolutionName.Module\\BusinessObjects\\YourSolutionNameDbContext.cs_ file.

# [C#](#tab/tabid-csharp1)
```csharp
using Microsoft.EntityFrameworkCore;

public class YourSolutionNameEFCoreDbContext : DbContext {
    // ...
    public DbSet<Employees> Employees { get; set; }
}
```
***

Get an [EFCoreObjectSpace](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace) instance from the [CompositeObjectSpace.AdditionalObjectSpaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) collection in the `GetDataFromSproc` method. 

Access the `YourSolutionNameEFCoreDbContext` instance from the [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext) property. 

Call the `YourSolutionNameEFCoreDbContext.Employees.FromSqlRaw` method to get data from a stored procedure.

# [C#](#tab/tabid-csharp1)
```csharp
using DevExpress.ExpressApp.EFCore;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;

class MyNonPersistentObjectAdapter {
    // ...
    List<MyNonPersistentObject> GetDataFromSproc() {
        EFCoreObjectSpace persistentObjectSpace = objectSpace.AdditionalObjectSpaces.OfType<EFCoreObjectSpace>().First();
        YourSolutionNameEFCoreDbContext dbContext = (YourSolutionNameEFCoreDbContext)persistentObjectSpace.DbContext;
        IQueryable<Employees> results = dbContext.Employees.FromSqlRaw("GetEmployees");
        List<MyNonPersistentObject> objects = new List<MyNonPersistentObject>();
        foreach (Employees employees in results) {
            MyNonPersistentObject obj = new MyNonPersistentObject();
            obj.EmployeeID = employees.EmployeeID;
            obj.FirstName = employees.FirstName;
            obj.LastName = employees.LastName;
            obj.Title = employees.Title;
            objects.Add(obj);
        }
        return objects;
    }
}
```
***
