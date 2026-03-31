---
uid: "402981"
title: "Implement a Data Model: Basics"
seealso:
  - linkId: "112570"
  - linkId: "112571"
  - linkId: "112847"
  - linkId: "402971"
---
# Implement a Data Model: Basics

This lesson explains how to implement entity classes for your application and describes the basics of automatic user interface construction based on data.

During this lesson, you will do the following:

- Add a simple entity class.
- Display the entity class in the application's navigation control.

Entity classes do not depend on the application UI. Implement them in a [platform-independent module project](xref:118045). This way, other XAF or non-XAF applications can share entities.

Inherit your entity classes from the [base persistent class](xref:113146) @DevExpress.Persistent.BaseImpl.EF.BaseObject. The `BaseObject` class implements the [](xref:DevExpress.ExpressApp.IXafEntityObject) and [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interfaces. This means that CRUD operations for the declared objects are available automatically and you don't need to implement them in your code.

For additional information on these concepts, refer to the following topic: [](xref:112611).

## Step-by-Step Instructions

1. Expand the _MySolution.Module_ project and right-click the _Business Objects_ folder. Choose **Add** | **Class…**. Specify _Employee.cs_ as the new class name and click **Add**. Replace the auto-generated code with the following class declaration:

    ```csharp
    using DevExpress.Persistent.BaseImpl.EF;

    namespace MySolution.Module.BusinessObjects;

    public class Employee : BaseObject {
        public virtual String FirstName { get; set; }
        public virtual String LastName { get; set; }
        public virtual String MiddleName { get; set; }
    }
    ```

2. Go to the _MySolution.Module\BusinessObjects\MySolutionDbContext_ file and add the following property to the `MySolutionEFCoreDbContext` entity container class:

    # [C#](#tab/tabid-csharp)
    
    ```csharp{6}
    using MySolution.Module.BusinessObjects;

    namespace  MySolution.Module.BusinessObjects {
        public class MySolutionEFCoreDbContext : DbContext {
            //...
            public DbSet<Employee> Employees { get; set; }
        }
    }
    ``` 
    ***

    This property is a collection of `Employee` class objects. XAF creates a table with the same name in the database and then maps this collection to the table.

    > [!Note]
    > * If you inherit an entity class from another entity class, you can register both entities in the `DbContext` class. This way, your application can work with collections of ancestor class objects.
    > * [!include[composite-key-properties-template](~/templates/composite-key-properties-template.md)]

## Propagate Data Model Structure Changes to the Database

Your application now contains data objects. This means that the application requires a database. You have the following options to choose from: 

- **Use a DBMS to maintain the database** _(default option)_

  XAF automatically updates database table structure after your data model structure changes. Refer to the following topic for additional information: [Automatic Database Schema Update](xref:405418#automatic-database-schema-update).
  
- **Use an in-memory database**

  This option works best during the development/debugging stage. To enable this option, open the _MySolution.Blazor.Server\Startup.cs_ file, comment the `UseSqlServer` option, and uncomment the `UseInMemoryDatabase` option as displayed in the code snippet below. Do the same in the _MySolution.Win\Startup.cs_ file.

    # [ASP.NET Core Blazor](#tab/tabid-csharp-blazor)

    ```csharp{20,27}
    //..
    namespace MySolution.Blazor.Server;

    public class Startup {
        public Startup(IConfiguration configuration) {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // ...
        public void ConfigureServices(IServiceCollection services) {
            services.AddSingleton(typeof(Microsoft.AspNetCore.SignalR.HubConnectionHandler<>), typeof(ProxyHubConnectionHandler<>));
            //...
            services.AddXaf(Configuration, builder => {
                //...
                builder.ObjectSpaceProviders
                    .AddEFCore().WithDbContext<MySolution.Module.BusinessObjects.MySolutionEFCoreDbContext>((serviceProvider, options) => {
                        // ...
                        options.UseInMemoryDatabase("InMemory");
                        string connectionString = null;
                        if(Configuration.GetConnectionString("ConnectionString") != null) {
                            connectionString = Configuration.GetConnectionString("ConnectionString");
                        }
                        //...
                        ArgumentNullException.ThrowIfNull(connectionString);
                        //options.UseSqlServer(connectionString);
                        options.UseChangeTrackingProxies();
                        options.UseObjectSpaceLinkProxies();
                        options.UseLazyLoadingProxies();
                    })
                    // ...
            });
        }
    }
    ```
    # [Windows Forms](#tab/tabid-csharp-winforms)

    ```csharp{10-11}
    // ...
    namespace MySolution.Win;

    public class ApplicationBuilder : IDesignTimeApplicationFactory {
        public static WinApplication BuildApplication(string connectionString) {
            // ...
            builder.ObjectSpaceProviders
                .AddEFCore().WithDbContext<MySolution.Module.BusinessObjects.MySolutionEFCoreDbContext>((application, options) => {
                    // ...
                    options.UseInMemoryDatabase("InMemory");
                    //options.UseSqlServer(connectionString);
                    options.UseChangeTrackingProxies();
                    options.UseObjectSpaceLinkProxies();
                })
                
            // ...
        }

        // ...
    }

    ``` 
    ***

## Application Run

1. Run the application. You can see that the UI did not change. To make the `Employee` item visible in the application's navigation control, add the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) attribute to the corresponding class:

    ```csharp{5}
    //...

    namespace MySolution.Module.BusinessObjects;

    [DefaultClassOptions]
    public class Employee : BaseObject {

        //...
    }

    //...
    ```
    [`DefaultClassOptions`]: xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute

    With this attribute, you can also use `Employee` objects as data sources to generate reports. For additional information, refer to the following lesson of this tutorial: [Create and Preview a Report](xref:404206).
    
    To apply each option separately, use the [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) and [](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute) attributes.
   
2. Run the application. XAF generates a user interface that is based on the specified data structures. The List View displays the collection of objects of the `Employee` class. Since there are no objects of this type, the **Employee** List View is empty for now:

   ASP.NET Core Blazor
        
   :   ![|XAF ASP.NET Core Blazor App List View|](~/images/btutor_bmd_lesson2_listview.png)
   
   Windows Forms

   :   ![|XAF Windows Forms App List View|](~/images/employee-listview-winforms.png)

3. Click the **New** button to invoke the [Detail View](xref:112611) for a new object of the `Employee` type. XAF renders the properties of the entity class as data fields. The Detail View contains editors for each data field.

   ASP.NET Core Blazor
        
   :   ![|ASP.NET Core Blazor List View|](~/images/tutorial-employee-detailview-blazor.png)
   
   Windows Forms

   :   ![|XAF Windows Forms List View|](~/images/tutorial-employee-detailview-winforms.png)


## Next Lesson

[](xref:404256)