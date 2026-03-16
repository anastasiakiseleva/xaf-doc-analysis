---
uid: "404698"
title: "How to: Show a Custom Data-Bound Control in an XAF View (Blazor) - External Data"
owner: Irina Nikolaeva
---
# How to: Show a Custom Data-Bound Control in an XAF View (Blazor) - External Data

This topic demonstrates how to add a custom data-bound (data-aware) control to a View in a Blazor application. It also explains how to extend app navigation and add a navigation item to the new View.

![|DevExpress XAF - A Custom Data-Bound Control](~/images/custom-data-bound-control-blazor-basic-result.png)

This topic is based on the `MainDemo Blazor Server` demo application that ships with XAF. You can find this demo in the following folder: _[!include[PathToAllXafDemos](~/templates/path-to-all-xaf-demos.md)]\\MainDemo.NET.EFCore\CS\MainDemo.Blazor.Server_.

## Create a Razor Component

Blazor apps are built using [Razor components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/). In this example, we implement a custom Razor component based on a [DxChart](xref:DevExpress.Blazor.DxChart`1) control that displays a graph of incomplete tasks.

> [!NOTE]
> Use the built-in `DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor` to display charts in your applications. This article only uses `DxChart` as an example.

To add this component to your project, follow the steps below:

1. In the **Solution Explorer**, right-click your Blazor project's name and select **Add** | **New Item** from the ensuing context menu.
2. Specify a component name (`TaskChartComponent.razor`).
3. Add the following code to the created file.

    [!include[<MainDemo.Blazor.Server\\TaskChartComponent.razor>](~/templates/platform_specific_file_path.md)]
    # [C#](#tab/tabid-csharp)

    ```Razor
    @using DevExpress.ExpressApp.Blazor.Editors
    @using DevExpress.ExpressApp.Utils
    @using MainDemo.Module.BusinessObjects
    @using DevExpress.Blazor

    @implements IDisposable

    <DxChart T="DemoTask"
            Data="@DataSource"
            Width="100%">
        <DxChartTitle Text="Tasks">
            <DxChartSubTitle Text="Breakdown by department"></DxChartSubTitle>
        </DxChartTitle>
        <DxChartCommonSeries NameField="(DemoTask task) => CaptionHelper.GetDisplayText(task.Priority)"
                            ArgumentField="task => GetDepartmentName(task)"
                            ValueField="task => IsTaskCompleted(task)"
                            SummaryMethod="Enumerable.Sum">
            <SeriesTemplate Context="settings">
                <DxChartStackedBarSeries Settings="settings" />
            </SeriesTemplate>
        </DxChartCommonSeries>
        <DxChartTooltip Enabled="true"
                        Position="RelativePosition.Outside">
            <div style="margin: 0.5rem">
                <div class="fw-bold">@context.Point.Argument</div>
                <div>Priority: @context.Point.SeriesName</div>
                <div>Tasks in progress: @($"{context.Point.Value:N0}")</div>
            </div>
        </DxChartTooltip>
        <DxChartLegend Position="RelativePosition.Outside"
                    HorizontalAlignment="HorizontalAlignment.Center"
                    VerticalAlignment="VerticalEdge.Bottom" />
    </DxChart>

    @code {
        [CascadingParameter] public BlazorControlViewItem ViewItem { get; set; }

        public IEnumerable<DemoTask> DataSource { get; set; }

        private string GetDepartmentName(DemoTask task) => (task.AssignedTo as Employee)?.Department?.Title ?? "None";
        private int IsTaskCompleted(DemoTask task) => task.Status == MainDemo.Module.BusinessObjects.TaskStatus.Completed ? 0 : 1;
        private void ObjectSpace_Reloaded(object sender, EventArgs args) => UpdateDataSource();
        private void UpdateDataSource() => DataSource = ViewItem.ObjectSpace.GetObjects<DemoTask>().AsEnumerable();
        protected override void OnInitialized() {
            base.OnInitialized();
            UpdateDataSource();
            ViewItem.ObjectSpace.Reloaded += ObjectSpace_Reloaded;
        }
        void IDisposable.Dispose() {
            ViewItem.ObjectSpace.Reloaded -= ObjectSpace_Reloaded;
        }
    }
    ```
    ***

4. In the **Properties** window, set this file's `Build Action` to `Content`.

5. Rebuild your solution.

The component in this example uses the `CascadingParameter` of `DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem` to access an `ObjectSpace` instance. It uses the [Object Space API](xref:113711) to read the required data and then initialize the data source or refresh the data if necessary.

## Add the Control to a View

1. In the Blazor application project, double-click the _Model.xafml_ file to start the [Model Editor](xref:112582). Right-click the **Views** node and choose **Add…** | **DashboardView**.

    ![|DevExpress XAF - Add a View](~/images/custom-data-bound-control-blazor-add-view.png)

2. Set the `Id` property to `TaskChartView`.

    ![|DevExpress XAF - View ID](~/images/custom-data-bound-control-blazor-view-id.png)

3. Right-click the **Views** | **Unspecified** | **TaskChartView** | **Items** node and choose **Add…** | **ControlDetailItem**.

    ![|DevExpress XAF - Add a ControlDetailItem](~/images/custom-data-bound-control-blazor-add-detil-item.png)

4. Set the `Id` property to `TaskChartView`, and the [IModelControlDetailItem.ControlTypeName](xref:DevExpress.ExpressApp.Model.IModelControlDetailItem.ControlTypeName) property - to the type of the custom User Control you created (e.g., `MainDemo.Blazor.Server.TaskChartComponent`).

    ![|DevExpress XAF - Specify a Control Type](~/images/custom-data-bound-control-blazor-control-type.png)

> [!NOTE]
> You can add the [](xref:DevExpress.ExpressApp.Layout.ControlViewItem) View Item to any existing Detail View or Dashboard View instead of creating a new Dashboard View.

## Create a Navigation Item to Show the View

1. Navigate to the **NavigationItems** | **Items** | **Default** | **Items** node. Right-click the **Items** node and select **Add…** | **NavigationItem** from the invoked context menu.

    ![|DevExpress XAF - Add a Navigation Item](~/images/custom-data-bound-control-blazor-add-navigation-item.png)

2. For the newly added node, in the [IModelNavigationItem.View](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.View) dropdown list, select the View you created earlier (`TaskChartView`).

    ![|DevExpress XAF - Specify a View for the Navigation Item](~/images/custom-data-bound-control-blazor-specify-view.png)

3. Run your Blazor application and click **TaskChartView** in the navigation tree. The Chart View bound to the `DemoTask` collection is displayed.

    ![|DevExpress XAF - A Custom Data-Bound Control](~/images/custom-data-bound-control-blazor-basic-result.png)
