---
uid: "113302"
seealso:
- linkId: "113314"
title: Chart Module
owner: Ekaterina Kiseleva
---
# Chart Module

XAF includes [List Editors](xref:113189) that allow you to visualize data using the DevExpress chart components for ASP.NET Core Blazor and Windows Forms Chart components offer a comprehensive set of 2D and 3D charts to address a broad range of business needs with ease.

![|XAF ASP.NET Core Blazor Chart List Editor, DevExpress](~/images/xaf-blazor-chartlist-editor-devexpress.png)

## Chart Module Components

| Platform | Module | NuGet package |
| -------- | ------ | ------------- |
| Platform-agnostic | @DevExpress.ExpressApp.Chart.ChartModule | **DevExpress.ExpressApp.Chart** |
| ASP.NET Core Blazor | `DevExpress.ExpressApp.Blazor.SystemModule.SystemBlazorModule` | **DevExpress.ExpressApp.Blazor** |
| Windows Forms | @DevExpress.ExpressApp.Chart.Win.ChartWindowsFormsModule | **DevExpress.ExpressApp.Chart.Win** |

> [!NOTE]
> [!include[ExtraModulesNote](~/templates/extramodulesnote11181.md)]
> * [!include[<@DevExpress.ExpressApp.Win.ApplicationBuilder.ChartsApplicationBuilderExtensions.AddCharts(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder})>,<WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]

You can find a step-by step guide to using the Chart module for Windows Forms in the following topic: [How to: Display a List View as a Chart](xref:113314). The charting List Editor for this platform is demonstrated in the **List Editors** section of the **Feature Center** demo. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)]

## Chart List Editors

| Platform | Editor | Control |
| -------- | ------ | ------------- |
| ASP.NET Core Blazor | @DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor | @DevExpress.Blazor.DxChart`1, @DevExpress.Blazor.DxPolarChart`1, @DevExpress.Blazor.DxPieChart`1 |
| Windows Forms | @DevExpress.ExpressApp.Chart.Win.ChartListEditor | @DevExpress.XtraCharts.ChartControl |

![|XAF Windows Forms Pie Chart, DevExpress](~/images/chartlisteditor116775.png)

To display a List View as a chart, follow these steps:

1. Navigate to the required project: _YourSolutionName.Blazor.Server_, _YourSolutionName.Win_, or _YourSolutionName.Web_.
2. Invoke the [Model Editor](xref:112582) for the _Model.xafml_ file.
3. Navigate to the required List View node and change the [IModelListView.EditorType](xref:DevExpress.ExpressApp.Model.IModelListView.EditorType) property value to the platform-specific List Editor.

## Configure Chart

### ASP.NET Core Blazor

The @DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor receives a Razor file with the required graph layout and series settings as input. XAF ASP.NET Core Blazor automatically binds the control to the current View data. For more information about the relationship between Razor components and XAF UI elements, refer to the following topic: [](xref:404767).

> [!NOTE]
> This scenario is based on the `MainDemo Blazor Server` demo application that ships with XAF. You can find this demo in the following folder: _[!include[PathToAllXafDemos](~/templates/path-to-all-xaf-demos.md)]\\MainDemo.NET.EFCore\CS\MainDemo.Blazor.Server_.

1. Navigate to the _MainDemo.Blazor.Server_ project. Create a Razor Component, name it `PaycheckSettings`, and specify [DxChart](xref:DevExpress.Blazor.DxChart`1)'s configuration components:

	# [MainDemo.Blazor.Server\Charts\PaycheckSettings.razor](#tab/tabid-razor)
	```Razor
	@using DevExpress.Blazor
	@using DevExpress.ExpressApp
	@using DevExpress.ExpressApp.Blazor.Editors
	@using DevExpress.ExpressApp.Utils
	@using MainDemo.Module.BusinessObjects
	@using System.Linq.Expressions

	@*Define the chart data series*@
	<DxChartLineSeries Name="Gross Pay"
					ArgumentField="(Paycheck p) => p.PaymentDate"
					ValueField="(Paycheck p) => p.GrossPay"
					SummaryMethod="Enumerable.Sum" />
	<DxChartLineSeries Name="Net Pay"
					ArgumentField="(Paycheck p) => p.PaymentDate"
					ValueField="(Paycheck p) => p.NetPay"
					SummaryMethod="Enumerable.Sum" />
	@*Configure the chart legend settings*@
	<DxChartLegend Position="RelativePosition.Outside"
			   HorizontalAlignment="HorizontalAlignment.Center"
			   VerticalAlignment="VerticalEdge.Bottom" />
	```
	***

2. Make sure that the `BuildAction` property of the Razor file is set to `Content`.

3. In the _MainDemo.Blazor.Server_ project, open the _Model.xafml_ file. Navigate to the **Views** | **MainDemo.Module.BusinessObjects** | **Paycheck** | **Paycheck_ListView** node. Right-click the node and select the **Clone** command from the drop-down menu.

4. In the newly created node settings, set the `EditorType` property to `DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor`.

5. Set the `SettingsTypeName` property to the full name of your Razor Component: `MainDemo.Blazor.Server.Charts.PaycheckSettings`.

	![XAF ASP.NET Core Blazor Model Editor Chart List View Setup, DevExpress](~/images/xaf-blazor-chart-editor-model-editor-settings-devexpress.png)

	> [!NOTE]
	> If you want to display your data as a [Pie Chart](xref:DevExpress.Blazor.DxPieChart`1) or [Polar Chart](xref:DevExpress.Blazor.DxPolarChart`1), set the `ChartType` property to `DxPieChart` or `DxPolarChart` respectively. For more information on DevExpress Blazor Chart component configuration, refer to the corresponding [online demos](https://demos.devexpress.com/blazor/Charts) and [product documentation](xref:401180). These resources are a prerequisite to use XAF's `DxChartListEditor`.

If you want to customize the appearance of your chart (for example, apply a custom CSS style or color palette), use the cascading parameter to access the component's model:

# [MainDemo.Blazor.Server\Charts\PaycheckSettings.razor](#tab/tabid-razor)
```Razor
@using DevExpress.Blazor
@using DevExpress.ExpressApp
@using DevExpress.ExpressApp.Blazor.Editors
@using DevExpress.ExpressApp.Utils
@using MainDemo.Module.BusinessObjects
@using System.Linq.Expressions

@* ... *@

@code {
	[CascadingParameter] public DxChartListEditor Editor { get; set; }

	protected override void OnParametersSet() {
		base.OnParametersSet();
		// Specify your settings.
		Editor.ChartModel.Width = "100%";
	}
}
```
***

To access specific chart settings, cast `ChartModel` to the corresponding type:

# [MainDemo.Blazor.Server\Charts\PaycheckSettings.razor](#tab/tabid-razor)
```Razor
@using DevExpress.Blazor
@using DevExpress.ExpressApp
@using DevExpress.ExpressApp.Blazor.Editors
@using DevExpress.ExpressApp.Utils
@using MainDemo.Module.BusinessObjects
@using System.Linq.Expressions

@code {
	[CascadingParameter] public DxChartListEditor Editor { get; set; }

	protected override void OnParametersSet() {
		base.OnParametersSet();
		if(Editor.ChartModel is DxPieChartModel pieChart) {
			pieChart.SegmentDirection = PieChartSegmentDirection.CounterClockwise;
			pieChart.StartAngle = 45;
			pieChart.Diameter = 0.7;
			pieChart.InnerDiameter = 0.5;
		}
	}
}
```
***

#### Enable Data View Access Mode for Large Amounts of Data or Complex Data Models

For improved performance, we recommend that you use [Data View](xref:118452) mode. In this mode, the chart loads only the data projection you specified in the Model Editor for the List View node instead of the entire object graph (with all references, collection properties, and their nested fields). For example, if the `Gross Pay` column is hidden or removed in the **Views** | **MainDemo.Module.BusinessObjects** | **Paycheck** | **Paycheck_ListView_Chart** | **Columns** node, the chart does not load the corresponding data.

1. In the Razor Component, use `DataViewExpressionConverter` to update data series properties in the chart settings for the @DevExpress.ExpressApp.XafDataViewRecord type.

	# [MainDemo.Blazor.Server\Charts\PaycheckSettings.razor](#tab/tabid-razor)
	```Razor
	@* ... *@
	<DxChartLineSeries Name="Gross Pay"
					ArgumentField="DataViewExpressionConverter.Convert((Paycheck p) => p.PaymentDate)"
					ValueField="DataViewExpressionConverter.Convert((Paycheck p) => p.GrossPay)"
					SummaryMethod="Enumerable.Sum" />

	<DxChartLineSeries Name="Net Pay"
					ArgumentField="DataViewExpressionConverter.Convert((Paycheck p) => p.PaymentDate)"
					ValueField="DataViewExpressionConverter.Convert((Paycheck p) => p.NetPay)"
					SummaryMethod="Enumerable.Sum" />
	@* ... *@
	```
	***

2. In the _MainDemo.Blazor.Server_ project, invoke the Model Editor for the _Model.xafml_ file. Navigate to the **Views** | **MainDemo.Module.BusinessObjects** | **Paycheck** | **Paycheck_ListView_Chart** node that you created in the previous step and set the `DataAccessMode` property to `DataView`.

### Windows Forms

1. In the _YourSolutionName.Win_ project, invoke the [Model Editor](xref:112582) for the _Model.xafml_ file.
2. Navigate to the required List View's **ChartSettings** node, find the `Settings` property and click the ellipsis button to invoke the [Chart Designer](xref:114070).

	![ModelEditor_SpecialEditors_ChartWizard](~/images/modeleditor_specialeditors_chartwizard116849.png)

You can also invoke the designer at runtime and reset settings to default values using the chart's context menu. To enable this functionality, set the [Application Model](xref:112580)'s [ICustomizationEnabledProvider.CustomizationEnabled](xref:DevExpress.ExpressApp.Chart.ICustomizationEnabledProvider.CustomizationEnabled) property of the List View's **ChartSettings** node to `true`.

![ChartContextMenu](~/images/chartcontextmenu116782.png)

Runtime settings are saved to [user differences](xref:112580#application-model-layers) (the _Model.User.xafml_ file).

## Chart Customization in a View Controller

### ASP.NET Core Blazor

Some advanced scenarios require that you create a custom Controller to access and modify `DxChartListEditor` settings. For example, the following code snippet implements a **SingleChoiceAction** that allows a user to select one of several available chart types for display:

# [MainDemo.Blazor.Server\Controllers\SelectChartActionController.cs](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.SystemModule;
using DevExpress.ExpressApp.Utils;
using MainDemo.Blazor.Server.Charts;
using MainDemo.Module.BusinessObjects;

namespace MainDemo.Blazor.Server.Controllers;
public class SelectChartActionController : ObjectViewController<ListView, Paycheck> {
	private SingleChoiceAction setChartAction;
	private ChoiceActionItem setGrossPayChart;
	private ChoiceActionItem setNetPayChart;
	private ChoiceActionItem setCommonPayChart;

	public SelectChartActionController() {
		setChartAction = new SingleChoiceAction(this, "SelectPaycheckChart", 
		DevExpress.Persistent.Base.PredefinedCategory.Edit) {
			Caption = "Set Chart",
			SelectionDependencyType = SelectionDependencyType.Independent,
			ImageName = "Task",
		};
		setChartAction.Execute += SetChartAction_Execute;

		setGrossPayChart = new ChoiceActionItem(CaptionHelper.GetMemberCaption(typeof(Paycheck), 
		nameof(Paycheck.GrossPay)), typeof(PaycheckGrossChart));
		setChartAction.Items.Add(setGrossPayChart);
		setNetPayChart = new ChoiceActionItem(CaptionHelper.GetMemberCaption(typeof(Paycheck), 
		nameof(Paycheck.NetPay)), typeof(PaycheckNetChart));
		setChartAction.Items.Add(setNetPayChart);
		setCommonPayChart = new ChoiceActionItem(CaptionHelper.GetMemberCaption(typeof(Paycheck), 
		nameof(Paycheck.NetPay)) + " per Employee", typeof(PaycheckChartPerEmployee));
		setChartAction.Items.Add(setCommonPayChart);
	}

	protected override void OnViewControlsCreated() {
		base.OnViewControlsCreated();
		if (View.Editor is DxChartListEditor editor) {
			foreach (var item in setChartAction.Items) {
				if (editor.SettingType == (Type)item.Data) {
					setChartAction.SelectedItem = item;
					break;
				}
			}
		}
	}

	private void SetChartAction_Execute(object sender, SingleChoiceActionExecuteEventArgs e) {
		if (View.Editor is DxChartListEditor editor) {
			Type chartSettingsType = (Type)e.SelectedChoiceActionItem.Data;
			editor.SettingType = chartSettingsType;
		}
	}
}
```
***

### Windows Forms

Some chart control settings are unavailable in the **Chart Wizard**, but you can change them in code by accessing chart control properties. You can also change chart behavior by handling the control's events. To access a chart control instance in code, implement a [View Controller](xref:112621) and override the `OnViewControlsCreated` method:

# [YourSolutionName.Win\Controllers\MyWinController](#tab/tabid-csharp)
```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Chart.Win;
using DevExpress.XtraCharts;

namespace YourSolutionName.Win.Controllers;

public class MyWinController : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if (View.Editor is ChartListEditor chartListEditor && chartListEditor != null) {
            ChartControl chart = chartListEditor.Control;
            if (chart != null) {
                // Place your chart configuration code here.
            }
        }
    }
}
```
***

## Export And Print Charts

Since Chart List Editors implement the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface, charts can be exported using the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) Action and printed using the [PrintingController.PrintAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintAction) Action. You can customize the behavior of these Actions by handling the events of the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) and [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController) classes (see [How to: Customize Export Options of the Printing System](xref:113283) and [How to: Customize the Export Action Behavior](xref:113287)).

### ASP.NET Core Blazor

Export
:   ![|XAF ASP.NET Core Blazor, Export Chart List Editor, DevExpress](~/images/xaf-blazor-chart-export-action-devexpress.png)

### Windows Forms

Export
:   ![|XAF Windows Forms, Export Chart List Editor, DevExpress](~/images/export_chartlisteditor116970.png)

Print Preview
:   ![|XAF Windows Forms, Print Chart List Editor, DevExpress](~/images/printing_chartlisteditor116972.png)
