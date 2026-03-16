---
uid: "402154"
title: "How to: Access the Grid Component in a List View"
owner: Alexey Kazakov
seealso:
  - linkId: "112621"
  - linkId: "113189"
  - linkId: '404610'
    altText: 'How to: Access the Scheduler Control in Code'
  - linkId: '112836'
    altText: 'How to: Access a Control in Tree List Editors'
---
# How to: Access the Grid Component in a List View

This article explains how to access properties of a grid component displayed in a List View. You can use this technique with any [List Editor](xref:113189) control.

## Step-by-Step Instructions

1. In **Solution Explorer**, navigate to:
   * A platform-independent project in your solution (for example, **MySolution.Module**)
   * A platform-specific project in an ASP.NET Core Blazor or Windows Forms application (for example, **MySolution.Blazor.Server** or **MySolution.Win**).
2. Add a View Controller to the _Controllers_ folder.
3. Inherit the controller from the `ObjectViewController<ViewType, ObjectType>` class and override the `OnViewControlsCreated` method as demonstrated in the following code example:

   # [Platform-independent](#tab/tabid-csharp-independent)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Editors;

    namespace MySolution.Module.Controllers {
        public partial class CustomizeGridListEditorColumnController : ObjectViewController<ListView, Paycheck> {
            protected override void OnViewControlsCreated() {
                base.OnViewControlsCreated();                
                if (View.Editor is ColumnsListEditor listEditor) {
                    editor.Model.IsFooterVisible = true;
                    foreach (ColumnWrapper column in listEditor.Columns) {
                        if (column.PropertyName == nameof(Paycheck.NetPay)) {
                            column.AllowSummaryChange = false; }
                    }
                }
            }
        }
    }
    ```
   
   # [ASP.NET Core Blazor](#tab/tabid-csharp-blazor)

    ```csharp	
    using DevExpress.Blazor;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor.Editors;
    using MainDemo.Module.BusinessObjects;
    using MySolution.Module.BusinessObjects;

    namespace MySolution.Blazor.Server.Controllers;

    public class EmployeeListViewController : ObjectViewController<ListView, Employee> {
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            if(View.Editor is DxGridListEditor editor) {
                editor.GridModel.ColumnResizeMode = GridColumnResizeMode.ColumnsContainer;

                foreach(DxGridColumnWrapper column in editor.Columns) {
                    if(column.PropertyName == nameof(Employee.TitleOfCourtesy)) {
                        column.DxGridDataColumnModel.FilterMenuButtonDisplayMode = GridFilterMenuButtonDisplayMode.Never;
                    }
                    column.MinWidth = 50;
                }
            }
        }
    }
    ```
   [`GridModel`]: xref:DevExpress.ExpressApp.Blazor.Editors.Models.DxGridModel
   [`ObjectViewController`]: xref:DevExpress.ExpressApp.ObjectViewController*
   [`DxGridListEditor`]: xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor

   # [Windows Forms](#tab/tabid-csharp-winforms)
   
   ```csharp
   using DevExpress.ExpressApp;
   using DevExpress.ExpressApp.Win.Editors;
   using DevExpress.XtraGrid.Columns;
   using DevExpress.XtraGrid.Views.Grid;
   using MySolution.Module.BusinessObjects;

   namespace MySolution.Win.Controllers;

   public class GridViewController : ObjectViewController<ListView, TargetClassName> {
       protected override void OnViewControlsCreated() {
           base.OnViewControlsCreated();
           // Obtain the List Editor: XAF's abstraction over the UI control.
           if (View.Editor is GridListEditor gridListEditor && gridListEditor.GridView != null) {
               // Access the GridView object (part of the DevExpress WinForms Grid Control architecture). 
               GridView gridView = gridListEditor.GridView;
               // Specify the behavior of the grid's columns.
               // Access grid columns.
               // Use column settings to disable the sorting and grouping functionality. 
               foreach(WinGridColumnWrapper columnWrapper in gridListEditor.Columns) {
                columnWrapper.Column.OptionsColumn.AllowSort = DevExpress.Utils.DefaultBoolean.False;
                columnWrapper.Column.OptionsColumn.AllowGroup = DevExpress.Utils.DefaultBoolean.False;
            }
           }
       }
   }
   ```
   ***

4. (_Blazor only_) The @DevExpress.ExpressApp.Blazor.Editors.Models.DxGridModel object replicates all [parameters](https://learn.microsoft.com/en-us/aspnet/core/blazor/components#component-parameters) of the related @DevExpress.Blazor.DxGrid component. You can use these parameters to configure the underlying component before creation. However, the model does not allow you to access the current component state (for instance, a page index) or call its methods directly.

    Use the @DevExpress.ExpressApp.Blazor.Editors.Models.DxGridModel.ComponentInstance property to access the underlying component instance and its full API.

> [!NOTE]
> For platform-agnostic Grid List and Tree List customization, use `DevExpress.ExpressApp.Editors.ColumnWrapper`. For platform-specific customization, use its descendants:
> - `DevExpress.ExpressApp.Blazor.Editors.DxGridColumnWrapper` (ASP.NET Core Blazor)
> - `DevExpress.ExpressApp.Blazor.Editors.DxTreeListColumnWrapper` (ASP.NET Core Blazor)
> - `DevExpress.ExpressApp.Win.Editors.WinGridColumnWrapper` (Windows Forms)

[!include[platform-specific-events-control-customization](~/templates/platform-specific-events-control-customization.md)]