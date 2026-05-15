---
uid: "113303"
seealso:
- linkId: DevExpress.XtraPivotGrid
- linkType: HRef
  linkId: https://www.devexpress.com/Products/NET/Controls/WinForms/Pivot_Grid/
  altText: WinForms Pivot Table
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/xaf/archive/2013/01/16/how-to-rule-the-pivot.aspx
  altText: How to Rule the Pivot
- linkType: HRef
  linkId: https://www.youtube.com/watch?v=xGXfxCXcWB0
  altText: 'DevExpress WinForms Pivot Grid: Getting Started (YouTube)'
title: Pivot Grid Module
---
# Pivot Grid Module

The Pivot Grid module is a comprehensive data analysis, data mining, and visual reporting solution for XAF ASP.NET Core Blazor and Windows Forms applications. The module includes [List Editors](xref:113189) that adapt DevExpress Pivot Grid controls to XAF.

The module allows you to summarize large amounts of data in a multidimensional pivot table where users can sort, group, and filter the data.

> [!ImageGallery]
> ![Blazor Pivot Grid List Editor](~/images/pivot-grid/xaf-blazor-pivot-grid-module.png)
> ![Windows Forms Pivot Grid List Editor](~/images/pivot-grid/xaf-win-pivot-grid-module.png)

## DevExpress Controls Used by the Pivot Grid Module
The Pivot Grid module uses the following DevExpress controls:

| Platform | XAF List Editor | Underlying Control |
|---|---|---|
| ASP.NET Core Blazor | @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor | @DevExpress.Blazor.PivotTable.DxPivotTable
| Windows Forms | @DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor | @DevExpress.XtraPivotGrid.PivotGridControl

You can access these controls and change their behavior in code. For additional details, refer to the [](xref:402154) topic.


## Add the Pivot Grid Module to Your Application

The Pivot Grid module for **Blazor** is included in the main Blazor module (_DevExpress.ExpressApp.Blazor_), making it readily available without any additional configuration.

To enable the Pivot Grid module in your **Windows Forms** application, follow the steps below:

1. Install the NuGet package that contains the Office module: [DevExpress.ExpressApp.PivotGrid.Win](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.PivotGrid.Win).
2. Navigate to the _SolutionName.Win\Startup.cs_ file and call the [AddPivotGrid](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.PivotGridApplicationBuilderExtensions.AddPivotGrid(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder})) method:

    # [SolutionName.Win\Startup.cs](#tab/tabid-appbuilder-winforms)
          
    ```csharp{11}
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Design;
    using DevExpress.ExpressApp.Win;
    using DevExpress.ExpressApp.Win.ApplicationBuilder;
    // ...
    public class ApplicationBuilder : IDesignTimeApplicationFactory {
        public static WinApplication BuildApplication(string connectionString) {
            var builder = WinApplication.CreateBuilder();
            builder.UseApplication<SolutionNameWindowsFormsApplication>();
            builder.Modules
                .AddPivotGrid()
                // ...
    ```
    ***

XAF offers other methods to integrate the Pivot Module into a newly created or existing application. For additional information, refer to the following topic: <xref:118047>.


## Display Pivot Grid List Editors in a List View

To display a List View as a Pivot Grid, follow these steps:

1. Open the [Model Editor](xref:112582) for the following files:
    * **Blazor**: _SolutionName.Blazor.Server\Model.xafml_
    * **WinForms**: _SolutionName.Win\Model.xafml_
2. Navigate to the required List View node: **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView**.
3. Set the @DevExpress.ExpressApp.Model.IModelListView.EditorType property to the following values:
    * **Blazor**: `DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor`
    * **WinForms**: `DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor`

![PivotGrid list editor in the Model Editor](~/images/pivot-grid/xaf-blazor-pivot-grid-model-editor.png)

## Customize Pivot Grid Settings (Blazor)

You can customize the Pivot Grid settings in the following ways:

Specify Column Model Settings
:   Use the [Model Editor](xref:112582) to configure the following Pivot Grid column settings: @DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotFieldArea, @DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotGroupInterval, and @DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotSummaryType.
Customize the Pivot Grid Model
:   The @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.PivotGridModel replicates parameters of the underlying @DevExpress.Blazor.PivotTable.DxPivotTable component. Use these parameters to configure the Pivot Grid before it is created. 
Handle the ComponentCaptured Event
:   The @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.PivotGridModel does not allow direct access to the current component state or its methods. Handle the @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.ComponentCaptured event to access the underlying component instance and its full API.

## Customize Pivot Grid Settings (WinForms)
The entities below allow you to adjust the Pivot Grid module's settings in the [Application Model](xref:112580):

| Interface | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.PivotGrid.IModelPivotListView) | Extends the [Application Model](xref:112580) with the PivotSettings node. |
| [](xref:DevExpress.ExpressApp.PivotGrid.IModelPivotSettings) | Includes settings for the pivot grid List Editor that a [List View](xref:112611) displays. |
| [](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings) | Declares members of classes that specify settings of the pivot grid List Editor that a [List View](xref:112611) displays. |

These settings are available in the [Application Model](xref:112579)'s [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **PivotSettings** node.

![PivotGridSettingsAppModel](~/images/pivotgridsettingsappmodel131932.png)

The [IPivotSettings.CustomizationEnabled](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.CustomizationEnabled) property is set to `true` (**default**) and allows end users to modify their pivot table settings.
[!include[PivotGrid_xafmlConflict](~/templates/pivotgrid_xafmlconflict112048.md)]

The [IPivotSettings.Settings](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.Settings) property value is a complex XML-formatted string. To manage these settings, click the **Settings** ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)).

![Ellipsis](~/images/ellipsis131933.png)

The button invokes the **PivotGrid** designer that allows you to modify the pivot table's layout and other preferences.

![PivotGrid013-Designer](~/images/pivotgrid013-designer131901.png)


## Examples
You can find examples of the Pivot Grid List Editor implementation in the following demos:

* In the [Employee Management Demo (Blazor)](xref:113577#employee-management-demo-xpoef-core), navigate to **Payroll** > **Views** > **Pivot View** (see the [online demo](https://demos.devexpress.com/XAF/BlazorMainDemo/)).
* In the [Feature Center Demo (XPO)](xref:113577#feature-center-demo-xpo), navigate to **List Editors** > **Pivot Grid** (see the [online demo](https://demos.devexpress.com/XAF/featurecenter)).