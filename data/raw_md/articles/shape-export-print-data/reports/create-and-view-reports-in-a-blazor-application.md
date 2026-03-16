---
uid: "402306"
seealso:
- linkId: "113591"
- linkId: "404243"
- linkId: "113647"
- linkId: "113602"
title: Create and View Reports in an ASP.NET Core Blazor Application
---
# Create and View Reports in an ASP.NET Core Blazor Application

This topic describes how to create and view a report at runtime in an ASP.NET Core Blazor application.

> [!NOTE]
> ASP.NET Core Blazor Report Designer supports only desktop browsers.

## Prerequisites

The **Reports V2** module is installed for your XAF ASP.NET Core Blazor application. If not, [add the Reports V2 module](xref:404243) to your application.

## Limitations

In ASP.NET Core Blazor Report Designer, you cannot create reports that use [ViewDataSource](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource). New reports use [CollectionDataSource](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource).

## Copy a Predefined Report

1. Select a predefined report in the **Reports** List View.
2. Click the **Copy Predefined Report** button. 

    ![|XAF ASP.NET Core Blazor ReportsV2 Copy Predefined Report, DevExpress](~/images/ReportsV2_CopyPredefined_Blazor.png)
3. Select the created copy and [modify the report](xref:113647).

## Create a New Report from Scratch

To create a report at runtime, follow these steps:

1. Choose the **Reports** item in the [Navigation](xref:113198).
2. Click **New**.
3. In the [Report Wizard](xref:400946) dialog that opens, specify the following and click **Next**.
	
	* **Display Name** - the report's name.
    * **Data Type** - the business object type to be used in the report. Only the types that have the [DefaultClassOptionsAttribute](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [VisibleInReportsAttribute](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute) attribute applied can be selected.

    ![XAF ASP.NET Core Blazor ReportsV2 Wizard, DevExpress](~/images/ReportsV2_Wizard_Blazor.png)

4. Select the [report type](xref:117577).
	
	![|XAF ASP.NET Core Blazor ReportsV2 Wizard Report Type, DevExpress](~/images/ReportsV2_Wizard_Type_Blazor.png)

5. Follow the wizard's prompts to specify report columns and other settings.

    ![|XAF ASP.NET Core Blazor ReportsV2 Wizard Report Layout, DevExpress](~/images/ReportsV2_Wizard_ReportLayout_Blazor.png)

6. Click the **Finish** button to display the new report in the [Report Designer](xref:119176) where you can access advanced report layout customization options.

    ![|XAF ASP.NET Core Blazor ReportsV2 Designer, DevExpress](~/images/ReportsV2_Designer_Blazor.png)

This adds the data source component and sets its `ObjectTypeName` property to the business object type selected on the first page of the Report Wizard.

When the [VisibleInReports](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute) attribute is applied to a business class property, it specifies whether the target property is visible in the [Report Designer field list](xref:17567). In the Report Designer, you can modify the existing field layout and add more fields.

After a report is saved in the designer, it is added to the **Reports** List View. You can click a report to preview it.

![|XAF ASP.NET Core Blazor ReportsV2 Preview, DevExpress](~/images/ReportsV2_Preview_Blazor.png)

## Add a New Data Source

You can add a new data source in the Report Wizard.

1. In the Report Wizard, select **Add Data Source** from the side menu.

    ![|XAF ASP.NET Core Blazor ReportsV2 Add Data Source, DevExpress](~/images/ReportsV2_AddDataSource_Blazor.png)

2. Select the `CollectionDataSource` type and click **Next**.

    ![|XAF ASP.NET Core Blazor ReportsV2 Select Data Source Type, DevExpress](~/images/ReportsV2_AddDataSourceType_Blazor.png)

3. Choose an existing business class that you want to use in this Collection Data Source. Click **Finish** to open the report in Report Designer.

Alternatively, you can add a new data source in the Report Designer. The option is available in the Report Designer's menu.

## Display a Report in a Popup Window

XAF Blazor ReportsV2 module displays the Report Designer and the **Report Preview** window in the root Detail View. Set the `ReportsBlazorModuleV2.DesignAndPreviewDisplayMode` property to `Popup` if you want to keep the current view visible while designing/previewing reports.

**File:** _SolutionName.Blazor.Server/Startup.cs_

# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.Services;
using DevExpress.ExpressApp.ReportsV2.Blazor;

namespace SolutionName.Blazor.Server;

public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            // ...
            builder.Modules
                // ...
                .AddReports(options => {
                    options.DesignAndPreviewDisplayMode = DesignAndPreviewDisplayModes.Popup;
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
***

By design, XAF ASP.NET Core Blazor ReportsV2 module shows [In-Place Reports](xref:113602) from a nested list view in a popup.