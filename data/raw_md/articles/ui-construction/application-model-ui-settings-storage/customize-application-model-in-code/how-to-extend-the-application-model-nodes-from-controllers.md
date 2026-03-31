---
uid: "112785"
seealso:
- linkId: "112810"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-implement-a-custom-attribute-to-customize-the-application-model
  altText: How to implement a custom attribute to customize the Application Model
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF-how-to-add-an-unbound-column-to-gridlisteditor-to-execute-a-custom-action-for-a-record
  altText: XAF - Add an Unbound Column to GridListEditor to Execute a Custom Action for a Record
title: 'How to: Extend and Access the Application Model Nodes from Controllers'
---
# How to: Extend and Access the Application Model Nodes from Controllers

Follow the instructions below to extend the [Application Model](xref:112580) in the following two ways: 

- Add the `IsGroupFooterVisible` property to [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] nodes. If set to `true`, the corresponding List View displays a Group Footer. 
- Add the `GroupFooterSummaryType` property  to column nodes (**ListView** | **Columns** | **Column**). This property specifies group summary type for the corresponding column.
 
For more information on how to extend the Application Model, refer to the following topic: [Extend and Customize the Application Model in Code](xref:112810).

[!example[How to Extend the Application Model](https://github.com/DevExpress-Examples/xaf-how-to-extend-the-application-model)]

## Common Steps

Implement interfaces that expose the `IsGroupFooterVisible` and `GroupFooterSummaryType` properties:
	
```csharp
using DevExpress.Data;
using System.ComponentModel;

namespace ExtendModel.Module {
    public interface IModelListViewExtender {
        bool IsGroupFooterVisible { get; set; }
    }
    public interface IModelColumnExtender {
        [DefaultValue(SummaryItemType.None)]
        SummaryItemType GroupFooterSummaryType { get; set; }
    }
}
```

Override the [ModuleBase.ExtendModelInterfaces](xref:DevExpress.ExpressApp.ModuleBase.ExtendModelInterfaces(DevExpress.ExpressApp.Model.ModelInterfaceExtenders)) method of your base Module to extend the Application Model with declared interfaces:
	
```csharp
using DevExpress.ExpressApp.Model;
// ...
namespace ExtendModel.Module;

public sealed partial class ExtendModelModule : ModuleBase {
	// ...
	public override void ExtendModelInterfaces(ModelInterfaceExtenders extenders) {
	    base.ExtendModelInterfaces(extenders);
	    extenders.Add<IModelListView, IModelListViewExtender>();
	    extenders.Add<IModelColumn, IModelColumnExtender>();
	}
}
```

## WinForms-Specific Steps

Inherit a [WinGroupFooterViewController](xref:DevExpress.ExpressApp.ViewController) from the `ViewController<ListView>` type in the Windows Forms Module. This base class choice ensures the Controller activates in List Views only.

Override the protected `OnViewControlsCreated` method. If the `IsGroupFooterVisible` property is set to `true` for the current List View, display the group footer. 

Note that users can change column summary types in the UI. Handle the [View.ModelSaved](xref:DevExpress.ExpressApp.View.ModelSaved) event to save these changes to the Application Model when users close the current List View.
	
```csharp
using DevExpress.Data;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
using DevExpress.XtraGrid.Views.Grid;
using ExtendModel.Module;

namespace ExtendModel.Win.Controllers {
    public class WinGroupFooterViewController : ViewController<DevExpress.ExpressApp.ListView> {
        private void View_ModelSaved(object sender, EventArgs e) {
            if (View.Model is IModelListViewExtender modelListView && modelListView.IsGroupFooterVisible) {
                if (View.Editor is GridListEditor gridListEditor) {
                    GridView gridView = gridListEditor.GridView;
                    for (int i = 0; i < gridView.GroupSummary.Count; i++) {
                        if (View.Model.Columns[
                            gridView.GroupSummary[i].FieldName] is IModelColumnExtender modelColumn) {
                            modelColumn.GroupFooterSummaryType = gridView.GroupSummary[i].SummaryType;
                        }
                    }
                }
            }
        }
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            if (View.Model is IModelListViewExtender modelListView && modelListView.IsGroupFooterVisible) {
                if (View.Editor is GridListEditor gridListEditor) {
                    GridView gridView = gridListEditor.GridView;
                    gridView.OptionsView.GroupFooterShowMode = GroupFooterShowMode.VisibleAlways;
                    foreach (var column in gridListEditor.Columns) {
                        if (column.ModelColumn is IModelColumnExtender modelColumnExtender && modelColumnExtender.GroupFooterSummaryType != SummaryItemType.None) {
                            gridView.GroupSummary.Add(modelColumnExtender.GroupFooterSummaryType, column.Id, column.Column);
                        }
                    }
                }
            }
        }
        protected override void OnActivated() {
            base.OnActivated();
            View.ModelSaved += View_ModelSaved;
        }
        protected override void OnDeactivated() {
            View.ModelSaved -= View_ModelSaved;
            base.OnDeactivated();
        }
    }
}
```

## ASP.NET Core Blazor-Specific Steps

Inherit a [BlazorGroupFooterViewController](xref:DevExpress.ExpressApp.ViewController) from the `ViewController<ListView>` type in the ASP.NET Core Blazor Module. This base class choice ensures that the controller is activated only in List Views.

Override the protected `OnViewControlsCreated` method. If the `IsGroupFooterVisible` property is set to `true` for the current List View, display the group footer. 

Users cannot customize summary settings in ASP.NET Core Blazor UI. You do not need to handle the `ModelSaved` event.

# [C#](#tab/tabid-csharp1)
```csharp
using DevExpress.Data;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using ExtendModel.Module;

namespace ExtendModel.Blazor.Server.Controllers {
    public class BlazorGroupFooterViewController : ViewController<ListView> {
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            if (View.Model is IModelListViewExtender modelListView && modelListView.IsGroupFooterVisible && View.Editor is DxGridListEditor gridListEditor) {
                gridListEditor.GridModel.GroupFooterDisplayMode = DevExpress.Blazor.GridGroupFooterDisplayMode.Always;
                foreach (var column in gridListEditor.Columns) {
                    if (column.ModelColumn is IModelColumnExtender modelColumnExtender && modelColumnExtender.GroupFooterSummaryType != SummaryItemType.None) {
                        var summaryItem = (DxGridSummaryItemWrapper)gridListEditor.GridSummary.CreateItem(column.Id, modelColumnExtender.GroupFooterSummaryType);
                        summaryItem.SummaryItemModel.FooterColumnName = column.Id;
                        gridListEditor.GridSummary.GroupSummary.Add(summaryItem);
                    }
                }
            }
        }
    }
}
```
***

## Run the Application

Rebuild your solution. Invoke the **Model Editor** for the base Module and navigate to a **ListView** node. Change the following settings: 

- Set the `IsGroupPanelVisible` property to `true` to allow users to group data. 
- Set the new `IsGroupFooterVisible` property to `true` to enable group footers. 
- Specify summary types for **Column** nodes. Use the new `GroupFooterSummaryType` property.

Run the application. Open a List View with a group panel and group the List View by a column. You can see the footer with the specified summary types.

![Extend the app model](~/images/howtoexdendapplicationmodel116031_withBlazor.png)
