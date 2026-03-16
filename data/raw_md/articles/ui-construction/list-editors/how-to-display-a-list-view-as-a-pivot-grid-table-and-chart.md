---
uid: "119740"
seealso: []
title: 'How to: Display a List View as a Pivot Grid Table and Chart'
owner: Vera Ulitina
---
# How to: Display a List View as a Pivot Grid Table and Chart

This topic demonstrates how to display a default [List View](xref:112611) as a pivot table in XAF applications:

* [Add the Pivot Grid Module](#add-the-pivot-grid-module)
* [Change the List View's List Editor](#change-the-list-views-list-editor)
* [Specify Chart Settings](#specify-pivot-grid-settings)
* [Run the Application](#run-the-application)

> [!Note]
> ASP.NET Core Blazor applications do not support the [Pivot Grid Module](xref:113303).

The article uses a sample `Order` [business object](xref:112570) with the `Customer`, `Product Name`, `Product Category`, `Price`, and `Units Purchased` fields.

![PivotGridBefore1](~/images/pivotgridbefore1132470.png)

You can display the **Order** [List View](xref:112611) as a pivot table by adding the [Pivot Grid Module](xref:113303) to your application and replacing the default [Grid List Editor](xref:113189) with the Pivot Grid List Editor. The screenshot below demonstrates the result.

![PivotGridModuleResult](~/images/pivotgridmoduleresult132198.png)

You can see examples with Pivot Grid List Editors in the **FeatureCenter** demo shipped with XAF. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)]

## Add the Pivot Grid Module
[!include[ExtraModulesNote](~/templates/extramodulesnote11181.md)]

* [!include[<@DevExpress.ExpressApp.Win.ApplicationBuilder.PivotGridApplicationBuilderExtensions.AddPivotGrid(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder})>,<WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]

## Change the List View's List Editor
1. Double-click the **Module.Win** project's _Model.DesignedDiffs.xafml_ file to invoke the [Model Editor](xref:112582) for this project.
2. Navigate to the **Views** | **Order_ListView** node. In the **EditorType** ([IModelListView.EditorType](xref:DevExpress.ExpressApp.Model.IModelListView.EditorType)) property's drop-down, select "DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor" instead of XAF's default List Editor.
	
	![PivotGrid008-ChangeEditorWin](~/images/pivotgrid008-changeeditorwin131893.png)

## Specify Pivot Grid Settings
1. Invoke the [Model Editor](xref:112582) from the **Module.Win** project.
2. Navigate to the **Views** | **Order_ListView_PivotGrid** | **PivotSettings** node.
	
	![PivotGrid010-SettingsAgnostic](~/images/pivotgrid010-settingsagnostic131895.png)
3. Set the [IPivotSettings.ShowChart](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.ShowChart) property value to `true` and [IPivotSettings.CustomizationEnabled](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.CustomizationEnabled) to `false`.
4. Select the [IPivotSettings.Settings](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.Settings) property and click the ellipsis button to invoke the [PivotGrid Designer](xref:1825).
	
	![PivotGrid012-AgnosticSettingsEllipsis](~/images/pivotgrid012-agnosticsettingsellipsis131897.png)
5. In the **PivotGrid** Designer, navigate to **Main** | **Layout**. Place the **Product Name** field in the [Row Header Area](xref:1685), the **Customer** field in the [Column Header Area](xref:1686) area, and the **Units Purchased** field into the [Data Header Area](xref:1688)  – as shown in the screenshot. Drag the **Product Category** and **Price** fields onto the [Filter Header Area](xref:1684) area to exclude them from the pivot table. This yields a pivot grid table that summarizes sales by customer.
	
	![PivotGrid013-Designer](~/images/pivotgrid013-designer131901.png)

## Run the Application
1. Run the Windows Forms application and select the **Order** [Navigation Item](xref:113198) to display the pivot table.
	
	![PivotGrid020-settings](~/images/pivotgrid020-settings131923.png)

> [!TIP]
> For additional information on working with pivot tables, refer to the Pivot Grid control article ([Windows Forms](xref:3409)) and watch the DevExpress Pivot Grid: Getting Started ([Windows Forms](https://www.youtube.com/watch?v=xGXfxCXcWB0)) video.
