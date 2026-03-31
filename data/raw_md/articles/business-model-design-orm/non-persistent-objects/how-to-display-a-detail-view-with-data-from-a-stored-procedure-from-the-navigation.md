---
uid: "403168"
seealso:
- linkId: "403189"
- linkId: "403164"
title: 'How to: Display a Detail View With Data From a Stored Procedure From the Navigation'
---
# How to: Display a Detail View With Data From a Stored Procedure From the Navigation

This example demonstrates how to show a Detail View for data fetched from a stored procedure from the Navigation. 

This example uses the Northwind database and [Non-Persistent Objects](xref:116516) to store data from the stored procedure. The stored procedure is defined as follows:

# [SQL](#tab/tabid-sql)
```SQL
CREATE PROCEDURE GetEmployee
    @ID INT
AS
BEGIN
    SET NOCOUNT ON;
    SELECT * FROM Employees
    WHERE EmployeeID = @ID
END
GO
```
***

## Create Non-Persistent Objects in the Platform-Agnostic Module

1. In the [platform-agnostic](xref:118045) _MySolution.Module_ project, create the following non-persistent class:

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

2. Handle the @DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated event in the Application Builder code to subscribe to the `NonPersistentObjectSpace` events as described in the following topic: [How to: Display a Non-Persistent Object's Detail View](xref:113471).

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
	// ...
    ```

    ***

3. ORM-dependent code executes a stored procedure (the code uses [](xref:DevExpress.Xpo.Session) in XPO and [DbContext](xref:Microsoft.EntityFrameworkCore.DbContext) in EF Core). You can access the `Session` or `DbContext` through the corresponding persistent `ObjectSpace`. To allow the `NonPersistentObjectSpace` to access persistent `ObjectSpaces`, populate the [CompositeObjectSpace.AdditionalObjectSpaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) collection in the `ObjectSpaceCreated` event handler.

    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

    # [C#](#tab/tabid-csharp)
    ```csharp{6-8}
    using DevExpress.ExpressApp;
    // ...
	builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
        CompositeObjectSpace os = e.ObjectSpace as CompositeObjectSpace;
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

4. To separate the Module code from business logic to fetch data, create an adapter class to handle the `NonPersistentObjectSpace` events. Handle the [NonPersistentObjectSpace.ObjectByKeyGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectByKeyGetting) event to return a displayed object.

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;

    namespace YourSolutionName.Module.BusinessObjects {
        class MyNonPersistentObjectAdapter {
            NonPersistentObjectSpace objectSpace;
            public MyNonPersistentObjectAdapter(NonPersistentObjectSpace npos) {
                objectSpace = npos;
                objectSpace.ObjectByKeyGetting += ObjectSpace_ObjectByKeyGetting;
            }

            private void ObjectSpace_ObjectByKeyGetting(object sender, ObjectByKeyGettingEventArgs e) {
                if (e.ObjectType != typeof(MyNonPersistentObject)) {
                    return;
                }
                e.Object = GetObjectFromSproc(e.Key);
            }
            MyNonPersistentObject GetObjectFromSproc(object key) {
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
        CompositeObjectSpace os = e.ObjectSpace as CompositeObjectSpace;
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

    The `GetObjectFromSproc` method should contain ORM-dependent code to get data from a stored procedure.

5. Add a navigation item for the _MyNonPersistentObject_ Detail View with the object key as described in the following topic: [How to: Display a Non-Persistent Object's Detail View](xref:113471).

## Create XPO-Dependent Code to Get Data from a Stored Procedure

Use the [Session.ExecuteQueryWithMetadata](xref:DevExpress.Xpo.Session.ExecuteQueryWithMetadata(System.String)) method to get data from a stored procedure. This method returns column names along with data. Refer to the following help topic for instructions on how to access data from the `ExecuteQueryWithMetadata` method: [How to: Access Data in SQL Query Results](xref:9216). 

Use the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) property to access a [Session](xref:DevExpress.Xpo.Session) instance. You can access an `XPObjectSpace` instance from the [CompositeObjectSpace.AdditionalObjectSpaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) collection.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Xpo;
using DevExpress.Xpo;
using DevExpress.Xpo.DB;
using System.Linq;

class MyNonPersistentObjectAdapter {
    // ...
    MyNonPersistentObject GetObjectFromSproc(object key) {
        XPObjectSpace persistentObjectSpace = objectSpace.AdditionalObjectSpaces.OfType<XPObjectSpace>().First();
        Session session = persistentObjectSpace.Session;
        SelectedData results = session.ExecuteQueryWithMetadata($"GetEmployee @ID={key}");
        Dictionary<string, int> columnNames = new Dictionary<string, int>();
        for (int columnIndex = 0; columnIndex < results.ResultSet[0].Rows.Length; columnIndex++) {
            string columnName = results.ResultSet[0].Rows[columnIndex].Values[0] as string;
            columnNames.Add(columnName, columnIndex);
        }
        MyNonPersistentObject obj = new MyNonPersistentObject();
        if (results.ResultSet[1].Rows.Length > 0) {
            SelectStatementResultRow row = results.ResultSet[1].Rows[0];
            obj.EmployeeID = (int)row.Values[columnNames["EmployeeID"]];
            obj.FirstName = row.Values[columnNames["FirstName"]] as string;
            obj.LastName = row.Values[columnNames["LastName"]] as string;
            obj.Title = row.Values[columnNames["Title"]] as string;
        }
        return obj;
    }
}
```

***

## Create EF Core-Dependent Code to Get Data from a Stored Procedure

In EF Core, use the [DbSet](xref:Microsoft.EntityFrameworkCore.DbSet`1) object's [RelationalQueryableExtensions.FromSqlRaw](xref:Microsoft.EntityFrameworkCore.RelationalQueryableExtensions.FromSqlRaw*) extension method to get data from a stored procedure. Create an entity class that should store data fetched from a stored procedure.

# [C#](#tab/tabid-csharp-ef)
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

# [C#](#tab/tabid-csharp-ef)
```csharp
using Microsoft.EntityFrameworkCore;

public class YourSolutionNameEFCoreDbContext : DbContext {
    // ...
    public DbSet<Employees> Employees { get; set; }
}
```
***

Get an [EFCoreObjectSpace](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace) instance from the [CompositeObjectSpace.AdditionalObjectSpaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) collection in the `GetObjectFromSproc` method. 

Access the `YourSolutionNameEFCoreDbContext` instance from the [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext) property. 

Call the `YourSolutionNameEFCoreDbContext.Employees.FromSqlRaw` method to get data from a stored procedure.

# [C#](#tab/tabid-csharp-ef)
```csharp
using DevExpress.ExpressApp.EFCore;
using Microsoft.EntityFrameworkCore;

class MyNonPersistentObjectAdapter {
    // ...
    MyNonPersistentObject GetObjectFromSproc(object key) {
        EFCoreObjectSpace persistentObjectSpace = objectSpace.AdditionalObjectSpaces.OfType<EFCoreObjectSpace>().First();
        YourSolutionNameEFCoreDbContext dbContext = (YourSolutionNameEFCoreDbContext)persistentObjectSpace.DbContext;
        IQueryable<Employees> results = dbContext.Employees.FromSqlRaw($"GetEmployee @ID={key}");
        MyNonPersistentObject obj = new MyNonPersistentObject();
        Employees employees = results.ToList().FirstOrDefault();
        if (employees != null) {
            obj.EmployeeID = employees.EmployeeID;
            obj.FirstName = employees.FirstName;
            obj.LastName = employees.LastName;
            obj.Title = employees.Title;
        }
        return obj;
    }
}
```
***
