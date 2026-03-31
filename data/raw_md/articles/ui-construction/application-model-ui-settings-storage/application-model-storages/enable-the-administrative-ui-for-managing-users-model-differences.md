---
uid: "113704"
seealso: []
title: "Enable the Administrative UI to manage End-User Settings in the Database"
---
# Enable the Administrative UI to manage End-User Settings in the Database

This topic describes how to enable UI elements you can use to manage Model Differences [stored in the database](xref:113698).

The Administrative UI allows application administrators to manage user settings in user accounts - create, copy, export, and reset Model Differences. Follow the steps below to enable this UI in your WinForms or ASP.NET Core Blazor application: 

1. Open the _Module.cs_ file and add the following code to the Module constructor:

	# [C#](#tab/tabid-csharp)

	```csharp
	using DevExpress.Persistent.BaseImpl;
	// ...
	namespace MainDemo.Module {
      public sealed partial class MainDemoModule : ModuleBase {
         public MainDemoModule() {
            // ...
            AdditionalExportedTypes.Add(typeof(ModelDifference));
            AdditionalExportedTypes.Add(typeof(ModelDifferenceAspect));
         }
         // ...
      }
	}
	```
	***

   If you use the Entity Framework Core, ensure that your **DbContext** contains the following lines:

   # [C#](#tab/tabid-csharp-efonly)

   ```csharp
   using DevExpress.Persistent.BaseImpl.EF;
   // ...
   public class MyDbContext : DbContext {
      // ...
      public DbSet<ModelDifference> ModelDifferences { get; set; }
      public DbSet<ModelDifferenceAspect> ModelDifferenceAspects { get; set; }
   }
   ```

   ***

2. Run the [Model Editor](xref:112582) and [create a new Navigation Item](xref:402131) for the **ModelDifference_ListView** List View.

   ![Add the new Navigation Item](~/images/dbmodeldiffs_addnavitem117611.png)

Run the application and click this Navigation Item to open the Model Difference List View. Ensure that the Model Differences management Actions are available in the **Tools** category.

**WinForms**  

![Model Difference List View in a WinForms application](~/images/dbmodeldiffs_actions117610.png)

**ASP.NET Core Blazor**

![Model Difference List View in an ASP.NET Core Blazor application](~/images/DbModelDiffs_Actions_Blazor.png)


Users who used the application at least once have initialized Model Differences. The List View lists these Model Differences. This View also contains the **Shared Model Difference** record that stores global settings. Click **Create Model Differences** to create Model Differences for unlisted users. Click **Import Shared Model Difference** to load shared Model Differences created in Visual Studio (the _Model.xafml_ file). You can also copy, export, and reset a selected record. 

> [!NOTE]
> * The **Export Model Differences** Action saves model differences to the application's _ExportedModelDifferences_ subfolder. Use the **ModelDifferenceViewController.ExportedModelDifferencesPath** property to change the folder.
