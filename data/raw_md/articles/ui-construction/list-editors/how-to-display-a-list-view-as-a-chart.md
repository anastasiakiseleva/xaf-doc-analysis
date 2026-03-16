---
uid: "113314"
seealso:
- linkId: "113302"
- linkId: DevExpress.ExpressApp.Chart.ChartListEditorBase
- linkId: DevExpress.ExpressApp.Chart.Win.ChartListEditor
- linkId: DevExpress.ExpressApp.Chart.IModelChartSettings
title: 'How to: Display a List View as a Chart (Windows Forms)'
owner: Ekaterina Kiseleva
---
# How to: Display a List View as a Chart (Windows Forms)

The default [List Editor](xref:113189) that visualizes [Views](xref:112611) in XAF applications is [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) (used in WinForms applications). This default List Editor visualizes List Views as grids. This topic demonstrates the capabilities of the [Chart Module](xref:113302) you can use to visualize a List View as a chart. The List View, visualized by [](xref:DevExpress.ExpressApp.Chart.Win.ChartListEditor), is defined in the [Application Model](xref:112580). Customizations of the Chart settings using the [Chart Designer](xref:114070) are also shown.

> [!NOTE]
> If you want to display a List View as a chart in an XAF ASP.NET Core Blazor application, refer to the following topic: [](xref:113302).

> [!TIP]
> You can see examples with Chart List Editors in the **FeatureCenter** demo shipped with XAF. This demo is located in the _[!include[](~/templates/path-to-feature-center.md)]_ folder, by default.

Follow the steps below to implement the sample application demonstrating the use of Chart List Editors.

## Implement Sample Persistent Object
Consider the following `Employee` persistent class or similar Entity Framework Core class:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
//...
[DefaultClassOptions,DefaultProperty(nameof(FullName)),ImageName("BO_Person")]
public class Employee : BaseObject {
    [HideInUI(HideInUI.ListViewColumn)]
    public virtual string FirstName { get; set; }
    [HideInUI(HideInUI.ListViewColumn)]
    public virtual string LastName { get; set; }
    [HideInUI(HideInUI.DetailViewEditor)]
    public string FullName {
        get { return String.Format("{0} {1}", FirstName, LastName); }
    }
    public virtual string Position { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
[`HideInUI`]: xref:DevExpress.Persistent.Base.HideInUIAttribute

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using System.ComponentModel;
//...
[DefaultClassOptions, DefaultProperty(nameof(FullName)), ImageName("BO_Person")]
public class Employee : BaseObject {
    public Employee(Session session) : base(session) {}
    private string firstName;
    private string lastName;
    private string position;
    [HideInUI(HideInUI.ListViewColumn)]
    public string FirstName {
        get { return firstName; }
        set { SetPropertyValue(nameof(FirstName), ref firstName, value); }
    }
    [HideInUI(HideInUI.ListViewColumn)]
    public string LastName {
        get { return lastName; }
        set { SetPropertyValue(nameof(LastName), ref lastName, value); }
    }
    [HideInUI(HideInUI.DetailViewEditor)]
    public string FullName {
        get { return String.Format("{0} {1}", FirstName, LastName); }
    }
    public string Position {
        get { return position; }
        set { SetPropertyValue(nameof(Position), ref position, value); }
    }
}
```

***

> [!NOTE]
> Although `Employee` is an XPO persistent class, the technique demonstrated here can also be used with Entity Framework.

In this example, we will create the `Employee` chart, which can be used to compare the number of Employees with different Positions.

## Create a New List View Node
Follow the steps below to create a List View node, which defines a List View to be visualized by a Chart List Editor.

* Invoke the [Model Editor](xref:112582) for the [platform-agnostic module project](xref:118045).
* Navigate to the **Views** | **Employee_ListView** node generated for the `Employee` persistent object. Right-click this node and select **Clone**.
	
	![ChartsCloneNode](~/images/chartsclonenode116825.png)
	
	A copy of the List View node will be created.
* Change the new node's [IModelView.Id](xref:DevExpress.ExpressApp.Model.IModelView.Id) property to "Employee_ListView_Chart".
	
	![ChartsSetNodeId](~/images/chartssetnodeid116826.png)

## Create the Navigation Item for the Chart List View
The **Employee_ListView_Chart** List View created at the previous stage should be accessible by end users. Create the **Employee Chart** [Navigation Item](xref:113198) and set the [IModelNavigationItem.View](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.View) property to "Employee_ListView_Chart".

![ChartsNavigationItem](~/images/chartsnavigationitem116827.png)

The creation of Navigation Items is detailed in the [Add an Item to the Navigation Control](xref:402131) tutorial.

> [!NOTE]
> Alternatively, you can define a [View Variant](xref:113011) pointing to the **Employee_ListView_Chart** List View. End users will be able to choose whether to display the `Employee` List View as a grid or as a chart. The chart List View can also be used as a Dashboard Item (see [How to: Display Several Views Side-by-Side](xref:113296)).

## Add the Chart Module
Chart List Editors are shipped with the **Chart Module**. Add corresponding platform-specific modules to the _MySolution.Win_ project.

1. Add the required platform-specific NuGet packages from the following table:

    {|
    |-
    ! Package
    ! Project
    |-
    
    | DevExpress.ExpressApp.Chart.Win
    | WinForms-specific application project  
    (_MySolution.Win_)
    |}


2. In the application constructor, add the platform-specific Charts Module to the @DevExpress.ExpressApp.XafApplication.Modules collection:

    **Windows Forms**  

    # [MySolution.Win\Startup.cs](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp.Chart.Win;

    namespace MySolution.Win {
        public class ApplicationBuilder : IDesignTimeApplicationFactory {
            public static WinApplication BuildApplication(string connectionString) {
                var builder = WinApplication.CreateBuilder();
                builder.UseApplication<MySolutionWindowsFormsApplication>();
                builder.Modules
                    .AddCharts()
                    // ...
            }
            // ...
        }
        // ...
    }
    ```
    ***

## Change the List View's List Editor
After the Chart Module is added, the Chart List Editor can be specified using the **List View** node's [IModelListView.EditorType](xref:DevExpress.ExpressApp.Model.IModelListView.EditorType) property.

* Invoke the **Model Editor** for the _MySolution.Win\\Model.xafml_ file. Navigate to the **Views** | **Employee_ListView_Chart** node. In the **EditorType** property's drop-down, select "DevExpress.ExpressApp.Chart.Win.ChartListEditor".
	
	![ChartSetEditorWin](~/images/chartseteditorwin116830.png)

## Specify Chart Settings

The Chart Module extends **List View** nodes with the **ChartSettings** ([](xref:DevExpress.ExpressApp.Chart.IModelChartSettings)) child node. To specify chart settings for the WinForms application, invoke the Model Editor for the WinForms application project and perform the following steps.

* Navigate to the **Views** | **Employee_ListView_Chart** | **ChartSettings** node. Click the ellipsis button to the right of the [IModelChartSettings.Settings](xref:DevExpress.ExpressApp.Chart.IModelChartSettings.Settings) property value.
	
	![ChartSettings](~/images/chartsettings116832.png)
	
	XAF displays the [Chart Designer](xref:114070) form. The form initially displays the **Options** page that contains appearance, behavior, and border settings.

* Click the **+** button next to the **Series (0)** item in the series list on the left-hand side. Select the **Bar** view type in the popup menu.
	
	![XAF Windows Forms Chart Designer, Add Series Item, DevExpress](~/images/chartsdesigner2116833.png)

* Set the new series **Name** property to `Positions`.
	
	![XAF Windows Forms Chart Designer, Series Name, DevExpress](~/images/chartdesigner5122947.png)

* Switch to the **Properties** tab. To define chart data, navigate to the **Data** properties section and find the **Argument Data Member** property. Open the property's drop-down menu and double-click the **Position** item.
	
	![XAF Windows Forms Chart Designer, Argument Data Member, DevExpress](~/images/chartsdesigner3122911.png)

* In the **Data** group, expand the **Qualitative Summary Options** sub-group. Find the **Summary Function** property and click the ellipsis button on the right. In the invoked window, choose **Count** and click **OK**.
	
	![XAF Windows Forms Chart Designer, Summary Function, DevExpress](~/images/chartsdesigner4116834.png)

* Click **OK** to close the **Chart Designer**. XAF sets the chart settings in XML format to the **Settings** property in the **Model Editor**.

> [!NOTE]
> Users can invoke the **Chart Designer** at runtime by right-clicking a chart and selecting **Invoke Wizard**. You can turn this feature off by setting the **ChartSettings** node's [ICustomizationEnabledProvider.CustomizationEnabled](xref:DevExpress.ExpressApp.Chart.ICustomizationEnabledProvider.CustomizationEnabled) property to `false`.
> For more information about the Chart Designer capabilities, refer to the following topic: [Chart Designer](xref:114070).

## Run the Application
Run the WinForms application. Create several **Employee** objects with different positions to provide data for the chart.

![XAF Windows Forms, Employee List Editor, DevExpress](~/images/chartsrunwinapp1116835.png)

Select the **Employee Chart** navigation item. The chart will be displayed.

![XAF Windows Forms, Positions Chart List Editor, DevExpress](~/images/chartsrunwinapp2116836.png)
