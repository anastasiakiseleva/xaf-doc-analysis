---
uid: "114159"
seealso: []
title: 'How to: Show a Custom Data-Bound Control in an XAF View (WinForms)'
owner: Ekaterina Kiseleva
---
# How to: Show a Custom Data-Bound Control in an XAF View (WinForms)

This example demonstrates how you can add a custom data-bound (data-aware) control to a View and display this View from the navigation in a WinForms XAF application.

![DataBoundControlWin](~/images/databoundcontrolwin118515.png)
> [!TIP]
> Similar examples for ASP.NET Core Blazor applications are available here: 
>
> * [External Data](xref:404698)
> * [Current Object Data](xref:404700)

## Create a User Control
Create a [User Control](https://learn.microsoft.com/en-us/previous-versions/dotnet/articles/aa302342(v=msdn.10)) in the [WinForms application project](xref:118045) (_MySolution.Win_). Right-click the project and choose **Add** | **User Control (Windows Forms)…**:

![DataBoundControlWin1](~/images/databoundcontrolwin1118504.png)

Add the required control, e.g., [](xref:DevExpress.XtraGrid.GridControl) from the **Toolbox** to the designer.

![DataBoundControlWin2](~/images/databoundcontrolwin2118505.png)

Customize the control as required; e.g., convert the [GridControl.MainView](xref:DevExpress.XtraGrid.GridControl.MainView) to [](xref:DevExpress.XtraGrid.Views.Card.CardView).

![DataBoundControlWin3](~/images/databoundcontrolwin3118506.png)

> [!TIP]
> You can also add the [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) component from the **DX.<:xx.x:>: XAF Data Sources for Reports** toolbox group and then bind the control to this component. Use the [DataSourceBase.ObjectTypeName](xref:DevExpress.Persistent.Base.ReportsV2.DataSourceBase.ObjectTypeName) property to specify the required business object type. This will allow you to see the data columns in the designer and customize them as required. Actual data binding will be performed further in code.

## Bind the Control to Data Using Object Space
Close the designer, right-click the _UserControl1.cs_ (_UserControl1.vb_) file and choose **View Code** to edit the **User Control** code. Implement the [](xref:DevExpress.ExpressApp.Editors.IComplexControl) interface. In the [IComplexControl.Setup](xref:DevExpress.ExpressApp.Editors.IComplexControl.Setup(DevExpress.ExpressApp.IObjectSpace,DevExpress.ExpressApp.XafApplication)) method, you can access the [Object Space](xref:113707) using the _objectSpace_ parameter, use the [Object Space API](xref:113711) to read the required data and then initialize the control's data source. In the [IComplexControl.Refresh](xref:DevExpress.ExpressApp.Editors.IComplexControl.Refresh) method (that is executed when a user clicks the **Refresh** Action), you can recreate the control's data source. The code below demonstrates the collection of **DemoTask** objects assigned to the [GridControl.DataSource](xref:DevExpress.XtraGrid.GridControl.DataSource) property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
// ...
public partial class UserControl1 : UserControl, IComplexControl {
    public UserControl1() {
        InitializeComponent();
    }
    private IObjectSpace objectSpace;
    void IComplexControl.Setup(IObjectSpace objectSpace, XafApplication application) {
        gridControl1.DataSource = objectSpace.GetObjects<EFDemo.Module.Data.DemoTask>();
        this.objectSpace = objectSpace;
    }
    void IComplexControl.Refresh() {
        gridControl1.DataSource = objectSpace.GetObjects<EFDemo.Module.Data.DemoTask>();
    }
}
```
***

> [!TIP]
> You can also use the _application_ parameter to access certain [Application Model](xref:112579) settings using the [XafApplication.Model](xref:DevExpress.ExpressApp.XafApplication.Model) property and customize the control accordingly.

## Add a ControlViewItem View Item to a View
In the WinForms application project, double-click the _Model.xafml_ file to start the [Model Editor](xref:112582). Right-click the **Views** node and choose **Add** | **DashboardView**.

![DataBoundControlWin4](~/images/databoundcontrolwin4118508.png)

Set the **Id** property to **TaskCardView**.

![DataBoundControlWin5](~/images/databoundcontrolwin5118509.png)

Right-click the **Views** | **TaskCardView** | **Items** node and choose **Add…** | **ControlDetailItem**.

![DataBoundControlWin6](~/images/databoundcontrolwin6118510.png)

Set the **Id** property to **TaskCardView**, and the [IModelControlDetailItem.ControlTypeName](xref:DevExpress.ExpressApp.Model.IModelControlDetailItem.ControlTypeName) property - to the type of the custom User Control you created (e.g., **EFDemo.Win.UserControl1**).

![DataBoundControlWin7](~/images/databoundcontrolwin7118511.png)

Focus the **Layout** node. Right click the designer surface to the right and choose **Customize Layout**. Then, right-click the **TaskCardView** layout item and choose **Hide Text**.

![DataBoundControlWin7.1](~/images/databoundcontrolwin7.1118514.png)

> [!NOTE]
> You can add the [](xref:DevExpress.ExpressApp.Layout.ControlViewItem) View Item to any existing Detail View or Dashboard View instead of creating a new Dashboard View.

## Create a Navigation Item that Shows the View with the Custom Control
Navigate to the **NavigationItems** | **Items** | **Default** | **Items** node.  Right-click the **Items** node and select **Add…** | **NavigationItem** from the invoked context menu.

![DataBoundControlWin8](~/images/databoundcontrolwin8118512.png)

For the newly added node, in the [IModelNavigationItem.View](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.View) dropdown list, select the View you created earlier (TaskCardView).

![DataBoundControlWin9](~/images/databoundcontrolwin9118513.png)

Run the WinForms application and click **Task Card View** in the navigation. The Card View bound to the DemoTask collection will be displayed (see the image in the beginning of this topic).
