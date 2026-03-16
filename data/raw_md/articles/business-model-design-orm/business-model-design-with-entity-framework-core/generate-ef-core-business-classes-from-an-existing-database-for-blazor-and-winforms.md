---
uid: "402971"
title: Generate EF Core Business Classes from an Existing Database for Blazor and WinForms Applications (Database First)
owner: Yekaterina Kiseleva
seealso:
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/ef/core/
    altText: Entity Framework Core Documentation
  - linkType: HRef
    linkId: https://www.entityframeworktutorial.net/efcore/create-model-for-existing-database-in-ef-core.aspx
    altText: Creating a Model for an Existing Database in Entity Framework Core
---
# Generate EF Core Business Classes from an Existing Database for Blazor and WinForms Applications (Database First)

You can use the [PMC](https://learn.microsoft.com/en-us/ef/core/cli/powershell) or [CLI](https://learn.microsoft.com/en-us/ef/core/cli/dotnet) tool to generate a business model from an existing database with Entity Framework Core (database-first approach). For implementation details of the code-first approach, refer to the following tutorial: [](xref:402981). The sections below describe the general approach for Blazor or WinForms XAF applications.

## Set Up the Project

1. Create a new Blazor XAF or WinForms XAF project and name it _MyEFSolution_, for example.
1. Add the [Microsoft.EntityFrameworkCore.Tools](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.Tools/) NuGet package to the _MyEFSolution.Module_ project. The package version must correspond to the [EF Core version currently supported in XAF](xref:401886). You can use the following [Package Manager Console](https://learn.microsoft.com/en-us/nuget/consume-packages/install-use-packages-powershell) command: 

    ```Console
    install-package Microsoft.EntityFrameworkCore.Tools -version 7.0.5 -ProjectName MyEFSolution.Module
    ```

1. Build the solution.
1. In the application configuration file, change the connection string's `Initial Catalog` parameter to use the existing database:

    # [appsettings.json (Blazor)](#tab/tabid-blazor)
    ```JSON
    {
        "ConnectionStrings": {
            "ConnectionString": "Integrated Security=SSPI;Pooling=false;MultipleActiveResultSets=true;Data Source=(localdb)\\mssqllocaldb;Initial Catalog=MyDataBase;ConnectRetryCount=0;",
            // ...
        }
        // ...
    }
    ```
    # [App.config (WinForms)](#tab/tabid-win)
    ```XML
    <connectionStrings>
    <!-- ... -->
    <add name="ConnectionString" connectionString="Integrated Security=SSPI;MultipleActiveResultSets=True;Data Source=(localdb)\mssqllocaldb;Initial Catalog=MyDataBase" providerName="System.Data.SqlClient" />
    </connectionStrings>
    ```
    ***

    In this example, `MyDataBase` is the name of the existing database.

## Integrate the Model into the Project
    
1. Run the `Scaffold-DbContext` command. This command generates models from the **MyTask** and **Contact** tables of the **MyDataBase** database and places them in the _Model_ folder:

    ```Console
    Scaffold-DbContext "Server=(localdb)\mssqllocaldb; DataBase=MyDataBase; Trusted_Connection=True;" Microsoft.EntityFrameworkCore.SqlServer -OutputDir MyModels -Project MyEFSolution.Module -StartupProject MyEFSolution.Module -Tables MyTask,Contact -Context MyEFSolutionEFCoreDbContextNew -NoOnConfiguring -DataAnnotations
    ```
    
    For more information about scaffolding, review the following:

    * Refer to the following EF tutorial: [Creating a Model for an Existing Database in Entity Framework Core](https://www.entityframeworktutorial.net/efcore/create-model-for-existing-database-in-ef-core.aspx).
    * Use the following command in the **Package Manager** console: `get-help scaffold-dbcontext –detailed`.

    Your app now has two `DbContext` entities:

    * `MyEFSolutionEFCoreDbContext` (located in _MyEFSolution.Module\BusinessObjects_) created by the [Template Kit](xref:405447).
    * `MyEFSolutionEFCoreDbContextNew` (located in _MyEFSolution.Module\MyModels_) created in the previous step.

1. Change the namespace of all scaffolded classes to `MyEFSolution.Module.BusinessObjects` and mark all of their properties as [virtual](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual) to support [UseChangeTrackingProxies](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.proxiesextensions.usechangetrackingproxies). **For more information, refer to** [The Importance of Property Change Notifications for Automatic UI Updates](xref:117395) **and** [Change Tracking in EF Core DbContext and Performance Considerations](xref:404292).


1. Remove the `TypesInfoInitializer` attribute from the `MyEFSolutionEFCoreDbContext` class and add this attribute to the `MyEFSolutionEFCoreDbContextNew` class. Add the required `using` statement and modify the `OnModelCreating` method:

    ```csharp{1,4,10}
    using DevExpress.ExpressApp.Design;

    namespace MyEFSolution.Module.BusinessObjects {
        [TypesInfoInitializer(typeof(DbContextTypesInfoInitializer<MyEFSolutionEFCoreDbContextNew>))]
        public partial class MyEFSolutionEFCoreDbContextNew : DbContext {
            // ...
        }
        protected override void OnModelCreating(ModelBuilder modelBuilder) {
            //..
            OnModelCreatingPartial(modelBuilder);
            modelBuilder.HasChangeTrackingStrategy(ChangeTrackingStrategy.ChangingAndChangedNotificationsWithOriginalValues);
            modelBuilder.UsePropertyAccessMode(PropertyAccessMode.PreferFieldDuringConstruction);
        }
    }
    ```
1. Remove the `MyEFSolutionEFCoreDbContext` class declaration. Rename the _MyEFSolutionEFCoreDbContextNew_ file to _MyEFSolutionEFCoreDbContext_. In the invoked window, click **Yes** to rename all corresponding references.

    ![Update class references](~/images/efCore_existing1.png)

1. In the default configuration, the [EF Core scaffolder](https://learn.microsoft.com/en-us/ef/core/managing-schemas/scaffolding/templates#customize-the-entity-types) generates `List<T>` for the inner implementations of collection properties (if you have relationships between business objects). Replace `List<T>` with `ObservableCollection<T>` manually or [automatically based on T4 templates](https://learn.microsoft.com/en-us/ef/core/managing-schemas/scaffolding/templates#customize-the-entity-types) to ensure correct operation of UI updates and other standard XAF functionality. For more information, refer to the following topics:
* [The Importance of Property Change Notifications for Automatic UI Updates](xref:117395)
* [Configure a One-to-Many Relationship](xref:402984)

1. Show the `Contact` and `MyTask` classes in the [Navigation Control](xref:402131).

After this, you can see data from the existing database in your application:

![Use MyEFSolutionEFCoreDbContextNew](~/images/efCore_existing4.png)

For more information on EF Core scaffolding, refer to the following Microsoft help topic: [Reverse Engineering](https://learn.microsoft.com/en-us/ef/core/managing-schemas/scaffolding).

[!example[XAF EF Core - How to use an existing database](https://github.com/DevExpress-Examples/XAF_EFCore_How_to_use_existing_base)]

> [!IMPORTANT]
> [!include[composite-key-properties-template](~/templates/composite-key-properties-template.md)]
