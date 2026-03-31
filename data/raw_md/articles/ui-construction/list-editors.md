---
uid: "113189"
seealso:
- linkId: "112611"
- linkId: "113610"
title: List Editors
---
# List Editors

[List Views](xref:112611) are visualized by means of List Editors. A List Editor has a control that is used to display an object collection supplied by a List View. A List Editor handles the binding of its control and supports interaction between the List View and the control. Certain List Editors are used for all the List Views. You can change the List Editors used in a default UI, or customize them. This topic explains how to do this, and defines available List Editor types. For information on how to implement your own List Editor, refer to the [](xref:DevExpress.ExpressApp.Editors.ListEditor) class description.

List Editors are abstract UI entities represented by `ListEditor` class descendants. The `ListEditor` class declares members common to all List Editors. These members define the basic List Editor functionality. To create actual controls, each List Editor type overrides the protected `CreateControlCore` method which is called when a List Editor needs to be displayed in a UI. Since different controls are used in ASP.NET Core Blazor and WinForms applications, there are different List Editors implemented for ASP.NET Core Blazor and WinForms UI, respectively. The following tables list the basic List Editors supplied by XAF. 

## List Editors in WinForms Applications

| Name | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) | The default List Editor used in XAF WinForms applications. This is the most common data visualization format in the form of a two-dimensional table. |
| [](xref:DevExpress.ExpressApp.TreeListEditors.Win.CategorizedListEditor) | Implemented in the [TreeList Editors module](xref:112841). Displays data in the form of a two-dimensional table accompanied by the category tree. |
| [](xref:DevExpress.ExpressApp.Chart.Win.ChartListEditor) | Implemented in the [Chart Module](xref:113302). Displays data in the form of a chart. |
| [](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor) | Implemented in the [Pivot Grid Module](xref:113303). Displays data in the form of a pivot table that can be accompanied by a chart. |
| [](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor) | Implemented in the [Scheduler module](xref:112811). Designed to present and manage scheduling information in XAF WinForms applications. |
| [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor) | Implemented in the [TreeList Editors module](xref:112841). Displays data in the form of a tree-like structure. |

[!example[XAF WinForms - How to Use the Gantt Control to Display a List of Tasks](https://github.com/DevExpress-Examples/xaf-win-gantt-control)]

## List Editors in ASP.NET Core Blazor Applications

| Name | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor) | Displays data in the form of a two-dimensional table. To display object collections, the `DxGridListEditor` uses the [DxGrid](xref:DevExpress.Blazor.DxGrid) component. |
| [](xref:DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor) | Displays data in the form of a two-dimensional table with nested rows. To display object collections, the `DxTreeListEditor` uses the [DxTreeList](xref:DevExpress.Blazor.DxTreeList) component. |
| [](xref:DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor) | Implemented in the [Scheduler module](xref:112811). Designed to display and manage scheduling information in XAF ASP.NET Core Blazor applications. |
| [](xref:DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor) | Displays data in the form of a chart. |

## Customize List Editors

This section contains the most common ways to customize List Editors.

* **Change the List Editor for a particular List View**

    In the [Model Editor](xref:112582), navigate to the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node and set the **EditorType** property to the required List Editor's type:
	
    ![ListEditor_EditorTypeProperty](~/images/listeditor_editortypeproperty116354.png)

* **Change the default List Editor for all List Views**

    In the [Model Editor](xref:112830), navigate to the **Views** node and set the **DefaultListEditor** property to the required List Editor's type:
	
    ![ListEditor_DefaultListEditorProperty](~/images/listeditor_defaultlisteditorproperty116353.png)

* **Customize a particular List Editor's control** 
    
    The examples below demonstrate how to customize a List Editor's control:
	
    [](xref:402154)
    
    [How to: Configure Bands in a Grid List Editor (WinForms)](xref:113694)
    
    [How to: Extend the Application Model](xref:112810)


* **Implement a custom List Editor**

    You can use a custom List Editor if XAF's built-in List Editors do not meet your requirements. The following articles describe how to create a List Editor and use it to implement additional functionality:

    [](xref:DevExpress.ExpressApp.Editors.ListEditor)
    
    [How to Access XafApplication and Collection Source from a custom List Editor](xref:DevExpress.ExpressApp.Editors.IComplexListEditor)

    [How to: Implement a Custom WinForms List Editor](xref:112659)

    [How to: Support a Context Menu for a Custom WinForms List Editor](xref:112660)
    
    [How to: Implement an ASP.NET Core Blazor List Editor Using a Custom Control](xref:403258)
