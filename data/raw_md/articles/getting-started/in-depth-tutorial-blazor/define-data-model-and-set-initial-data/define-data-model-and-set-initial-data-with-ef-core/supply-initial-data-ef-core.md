---
uid: "402985"
title: Supply Initial Data
owner: Alexey Kazakov
seealso: []
---
# Supply Initial Data

This lesson explains how to specify initial data in your application.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> * [](xref:402981)
> * [](xref:404256)

## Step-by-Step Instructions

1. Expand the _MySolution.Module_ project in the Solution Explorer and go to the _DatabaseUpdate_ folder. Open the _Updater.cs_ file and add the following code to the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method:

    ```csharp{9-16,18}
    using MySolution.Module.BusinessObjects;
    //...

    public class Updater : DevExpress.ExpressApp.Updating.ModuleUpdater {
        //...
        public override void UpdateDatabaseAfterUpdateSchema() {
            base.UpdateDatabaseAfterUpdateSchema();

            Employee employeeMary = ObjectSpace.FirstOrDefault<Employee>(x => x.FirstName == "Mary" && x.LastName == "Tellitson");
            if(employeeMary == null) {
                employeeMary = ObjectSpace.CreateObject<Employee>();
                employeeMary.FirstName = "Mary";
                employeeMary.LastName = "Tellitson";
                employeeMary.Email = "tellitson@example.com";
                employeeMary.Birthday = new DateTime(1980, 11, 27);
            }
            
            ObjectSpace.CommitChanges(); //Uncomment this line to persist created object(s).
        }
    }
    ```
    XAF uses an [Object Space](xref:113707) instance to manipulate persistent objects (see [Create, Read, Update and Delete Data](xref:113711)).
    
    In the sample code above, the [BaseObjectSpace.FirstOrDefault](xref:DevExpress.ExpressApp.BaseObjectSpace.FirstOrDefault*) method checks the `Employee` list for an entry that matches the name "Mary Tellitson". If such employee doesn't exist, the [BaseObjectSpace.CreateObject](xref:DevExpress.ExpressApp.BaseObjectSpace.CreateObject``1) method creates it and adds the corresponding entry to the database.
    
2. Run the application.

   XAF compares the application version with the database version. If the database version is older than the application version, then the application raises the [](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event. Each platform-specific project in your solution handles this event in the descendant of the [](xref:DevExpress.ExpressApp.XafApplication) class: `BlazorApplication` class (ASP.NET Core Blazor) and `WinApplication` class (Windows Forms).
   
   The application creates a database if the database does not exist. After that, the application calls the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method. The method saves the required objects to the database.

3. Select the **Employee** item in the navigation control and invoke the Detail View for the new employee:

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor supply initial data|](~/images/tutorial_bmd_lesson_efcore_2_5.png)

   Windows Forms

   :   ![Windows Forms supply initial data](~/images/tutorial-initial-data-winforms.png)
    
> [!TIP]
> You can also use [Data Seeding](https://learn.microsoft.com/en-us/ef/core/modeling/data-seeding) to specify initial data.

## Next Lesson

[](xref:402984)
