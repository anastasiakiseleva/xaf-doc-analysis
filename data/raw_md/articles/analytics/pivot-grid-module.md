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
owner: Vera Ulitina
---
# Pivot Grid Module

The Pivot Grid module is a comprehensive data analysis, data mining, and visual reporting solution for XAF applications. The module contains [List Editors](xref:113189) that adapt DevExpress [WinForms Pivot Grid](xref:3409) controls for XAF.

The feature enables you to summarize large amounts of data in a multi-dimensional pivot table where you can sort, group, and filter the data.

![PivotGridListEditor](~/images/pivotgridlisteditor116777.png)

End-users can customize the table's layout according to their analysis requirements with simple drag-and-drop operations.

For the Pivot Grid module's demonstration, access the **List Editors** | **PivotGrid** section in the **Feature Center** application supplied with XAF. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)]

> [!Note]
> Until the Pivot Grid Module supports Blazor UI, it is possible to integrate the [Blazor PivotGrid control](xref:DevExpress.Blazor.DxPivotGrid`1) into your Blazor application manually. The following topic describes how to do this: [Blazor - How to integrate the Pivot Grid into an XAF app](https://supportcenter.devexpress.com/ticket/details/t994515/blazor-how-to-integrate-the-pivot-grid-into-an-xaf-app).

## Getting Started
You can add the Pivot Grid module to an existing project by following the [How to: Display a List View as a Pivot Grid Table and Chart](xref:119740) tutorial.

> [!NOTE]
> [!include[ExtraModulesNote](~/templates/extramodulesnote11181.md)]
> * [!include[<@DevExpress.ExpressApp.Win.ApplicationBuilder.PivotGridApplicationBuilderExtensions.AddPivotGrid(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder})>,<WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]

## DevExpress Controls Used by the Pivot Grid Module
The Pivot Grid module uses the following DevExpress controls:

| Class | Description |
|---|---|
| [](xref:DevExpress.XtraPivotGrid.PivotGridControl) | Allows creating a pivot table in a WinForms application. |

You can access these controls and change their behavior in code. For more details, study the [](xref:402154) topic.

## Pivot Grid Module Components
The Pivot Grid module consists of the following platform-agnostic and platform-specific components:

![PivotGridModulesInToolbox](~/images/pivotgridmodulesintoolbox131707.png)

* [](xref:DevExpress.ExpressApp.PivotGrid.PivotGridModule)
	
	The module adds references to the _DevExpress.ExpressApp.PivotGrid.v<:xx.x:>.dll_ assembly.
* [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridWindowsFormsModule)
	
	The module references the _DevExpress.ExpressApp.PivotGrid.v<:xx.x:>.dll_ and _DevExpress.ExpressApp.PivotGrid.Win.v<:xx.x:>.dll_ assemblies.

For the Pivot Grid Module's best performance, add it to platform-specific projects only and customize the module there. Do not use the **PivotGridModule** component intended for the base module project.

## Pivot Grid Module Settings
The entities below allow you to adjust the Pivot Grid module's settings in the [Application Model](xref:112580):

| Interface | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.PivotGrid.IModelPivotListView) | Extends the [Application Model](xref:112580) with the PivotSettings node. |
| [](xref:DevExpress.ExpressApp.PivotGrid.IModelPivotSettings) | Provides access to the pivot grid List Editor a [List View](xref:112611) displays. |
| [](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings) | Declares members of classes that specify settings of the pivot grid List Editor a [List View](xref:112611) displays. |

These settings are available in the [Application Model](xref:112579)'s [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **PivotSettings** node.

![PivotGridSettingsAppModel](~/images/pivotgridsettingsappmodel131932.png)

The [IPivotSettings.CustomizationEnabled](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.CustomizationEnabled) property is set to **true** by default and allows end-users to modify their pivot table's settings.
[!include[PivotGrid_xafmlConflict](~/templates/pivotgrid_xafmlconflict112048.md)]

The [IPivotSettings.Settings](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.Settings) property value is a complex XML-formatted string. To manage these settings, click the **Settings**’ ellipsis button (![EllipsisButton](~/images/ellipsisbutton116182.png)).

![Ellipsis](~/images/ellipsis131933.png)

The button invokes the **PivotGrid** designer that allows you to modify the pivot table's layout and its other preferences.

![PivotGrid013-Designer](~/images/pivotgrid013-designer131901.png)

## Pivot Grid Module List Editors
The Pivot Grid module ships with the following [List Editors](xref:113189):

| Class | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor) | Represents the pivot grid [List Editor](xref:113189) XAF WinForms applications use. |

You can set the [IModelListView.EditorType](xref:DevExpress.ExpressApp.Model.IModelListView.EditorType) property value to this editor in the [Application Model](xref:112579) as the screenshot below illustrates:

The **EditorType** property value is set to "DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor" in the [WinForms module project](xref:118045).

![PivotGrid008-ChangeEditorWin](~/images/pivotgrid008-changeeditorwin131893.png)

> [!NOTE]
> Alternatively, you can invoke the [Model Editor](xref:112830) from the [application projects](xref:118045) and change the **EditorType** property value there.
