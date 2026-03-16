---
uid: "404206"
title: Create and Preview a Report
owner: Anastasiya Kisialeva
---
# Create and Preview a Report

This lesson explains how to create reports in the integrated reporting system. This system is based on the DevExpress [Reporting](xref:2162) library.

The instructions below show how to do the following:

- Add the Reports V2 Module to the application.
- Create a report that displays a list of **Employee** objects with their names and email addresses.

## Add Reports V2 Module

1. Add the **DevExpress.ExpressApp.ReportsV2** NuGet package to the _MySolution.Module_ project. See the following topic for more information on how to install DevExpress NuGet packages: [](xref:116042).
	
2. Add the **DevExpress.ExpressApp.ReportsV2.Blazor** NuGet package to the _MySolution.Blazor.Server_ project and the **DevExpress.ExpressApp.ReportsV2.Win** NuGet package to the _MySolution.Win_ project.
	
3. Go to the _MySolution.Module\MySolutionDbContext_ file and add a DbSet of `ReportDataV2` type:

   ```csharp
   public class MySolutionEFCoreDbContext : DbContext {
       //...
	   public DbSet<ReportDataV2> ReportData { get; set; }
   }
   ```

4. In the _MySolution.Blazor.Server_ project, open the _Startup.cs_ file and add the Reports V2 module to the application builder. Do the same in the _Startup.cs_ file in the _MySolution.Win_ folder.

   # [C# (ASP.NET Core Blazor)](#tab/tabid-csharp-blazor)
 
   ```csharp{10-14}
   public class Startup {
   // ...
       public void ConfigureServices(IServiceCollection services) {
           // ...
           services.AddXaf(Configuration, builder => {
               builder.UseApplication<MySolutionBlazorApplication>();
               builder.Modules
                   // ...
                   .AddFileAttachments()
                   .AddReports(options => {
                       options.EnableInplaceReports = true;
                       options.ReportDataType = typeof(DevExpress.Persistent.BaseImpl.EF.ReportDataV2);
                       options.ReportStoreMode = DevExpress.ExpressApp.ReportsV2.ReportStoreModes.XML;
                   });
               // ...
           });
           // ...
       }
   }
   ```

   # [C# (Windows Forms)](#tab/tabid-csharp-winforms)

   ```csharp{8-12}
   public class ApplicationBuilder : IDesignTimeApplicationFactory {
       public static WinApplication BuildApplication(string connectionString) {
       var builder = WinApplication.CreateBuilder();
       builder.UseApplication<MySolutionWindowsFormsApplication>();
       builder.Modules
       //...
            .AddFileAttachments()
            .AddReports(options => {
                options.EnableInplaceReports = true;
                options.ReportDataType = typeof(DevExpress.Persistent.BaseImpl.EF.ReportDataV2);
                options.ReportStoreMode = DevExpress.ExpressApp.ReportsV2.ReportStoreModes.XML;
            });			

       }
   }
   ```

   ***

   If you add the Reports V2 module when you create an XAF application, the [Template Kit](xref:405447) generates the code used to add the Reports V2 module automatically.

5. Run the application. In the navigation control, expand the **Reports** group and select the **Reports** item to invoke the **Report** List View.

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor Report List View|](~/images/tutorial-report-listview-blazor.png)

   Windows Forms

   :   ![Windows Forms Report List View](~/images/tutorial-report-listview-winforms.png)

## Create a Report

In ASP.NET Core Blazor or Windows Forms runtime, the steps to create a report are the same. This lesson demonstrates these steps in the ASP.NET Core Blazor application.

1. In the Report List View, click the **New** button to invoke the **New Report Wizard Parameters** pop-up window.

2. Specify _Employee List_ as the name of the report in the application UI and select **Employee** in the **Data Type** drop-down list. Click **Create**.  XAF uses data of this type to generate the report.

   ![|ASP.NET Core Blazor Report Wizard Parameters|](~/images/tutorial-report-wizard-parameters-blazor.png)  

   > [!TIP]
   > The **Data Type** drop-down list only shows the entity classes with [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute).

3. In the **Report Wizard**, select **Table Report** and click **Next**.

   ![|ASP.NET Core Blazor Report Wizard Table Report|](~/images/tutorial-report-wizard-table-blazor.png)

4. Select the **FirstName**, **LastName**, and **Email** data fields and click **Next**.

   ![|ASP.NET Core Blazor Report Wizard Report Layout|](~/images/tutorial-report-wizard-define-layout-blazor.png)

   XAF displays values of these fields in the report.

5. Select the **Grey** report color scheme and specify _Employee List_ as the report's title. Click **Finish**.

   ![|ASP.NET Core Blazor Report Wizard Page Settings|](~/images/tutorial-report-wizard-page-settings-blazor.png)

6. XAF displays the [Runtime Report Designer](https://devexpress.github.io/dotnet-eud/reporting-for-web/articles/report-designer.html).

   ![|ASP.NET Core Blazor Report Wizard Report Layout|](~/images/tutorial-report-customization-blazor.png)

7. Click the **Preview** button in the upper right corner to preview the report's print version.

   ![|ASP.NET Core Blazor Report Preview|](~/images/tutorial-report-preview-blazor.png)

   The current order of the columns in the table header is arbitrary. Let's change it to the following:

   * First Name
   * Last Name
   * Email

8. Click the **Design** button in the upper right corner to exit the preview mode. In the menu on the right, switch to the **Report Explorer**.

   ![|ASP.NET Core Blazor Report Explorer|](~/images/tutorial-report-explorer-blazor.png)

9. Expand the **Report** | **GroupHeader** | **table** | **tableRow1** item and rearrange its sub-items as displayed in the animation below. Do the same for the **Detail** | **table2** | **tableRow2** | item.

   ![|ASP.NET Core Blazor Rearrange Cells|](~/images/tutorial-report-explorer-field-order-blazor.gif)

   The **GroupHeader** item contains the table header cells. The **Detail** item contains cells with report data. You have to adjust both, so that the data matches the column header names.

10. Adjust the width of the cells.

    ![|ASP.NET Core Blazor Cells Width|](~/images/tutorial-report-explorer-cells-width-blazor.gif)

    The **LastName** and **Email** cells in the table header have no separator between them. Let's use cell borders to separate the header cells from each other visually.

11. Select the **Email** cell. Click the gear icon in the menu on the right to open the cell's properties. Navigate to the **Appearance** section and select the left border option.

    ![|ASP.NET Core Blazor Cell Properties|](~/images/tutorial-report-cell-properties.png)

12. Specify the same option for the **LastName** cell and set no borders for the **FirstName** cell.

13. Save the report and go back to the **Report** List View. Click the **Employee List** item in the grid and see the report.

    ![|ASP.NET Core Blazor Complete Report|](~/images/tutorial-report-final-blazor.png)

The created report is also available in the Windows Forms application.

![Windows Forms Complete Report](~/images/tutorial-report-final-winforms.png)

At runtime, you can use the search function, print the report, and export it in different formats such as PDF, XLS, CSV, and so on. Click the gear icon in the menu on the right to access the export settings for the available formats.

> [!NOTE]
> * You can create predefined reports at design time. For additional information, see the following article: [](xref:113645).
> * You can [sort](xref:113595) and [filter](xref:113594) the report data based on the parameter that the end user defines.

## Next Lesson

[](xref:404204)
