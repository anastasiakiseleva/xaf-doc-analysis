---
uid: "112652"
seealso:
- linkId: "112998"
title: 'Filter Data at Grid Control Level'
---
# Filter Data at Grid Control Level

You can filter a List View by means of the grid that displays it: XAF supports the following platform-specific grid controls:

ASP.NET Core Blazor
:   [](xref:DevExpress.Blazor.DxGrid)
Windows Forms
:   [](xref:DevExpress.XtraGrid.GridControl)

> [!TIP]
> For information on how to customize a grid component displayed in a List View, refer to the following topic: [](xref:402154)

## Column Header Filters

This functionality is available in the following platform-specific controls:

* @DevExpress.Blazor.DxGrid in ASP.NET Core Blazor
* [](xref:DevExpress.XtraGrid.GridControl) in Windows Forms

ASP.NET Core Blazor
:   ![|ASP.NET Core Blazor XAF ListView Filter, DevExpress|](~/images/xaf-blazor-ui-listview-filter-devexpress.png)
Windows Forms
:   ![Windows Forms XAF ListView Filter, DevExpress](~/images/listview_filter_win118835.png)

> [!TIP]
> If you use column header filters, XAF saves changes in the [Application Model](xref:112579). Changes persist even if you close the View. You can access these filter settings from the [IModelListView.Filter](xref:DevExpress.ExpressApp.Model.IModelListView.Filter) property in the [Model Editor](xref:112582).

## Filter Builder

This functionality is available for the following [List Editors](xref:113189):

ASP.NET Core Blazor
:   @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor, @DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor
Windows Forms
:   @DevExpress.ExpressApp.Win.Editors.GridListEditor

ASP.NET Core Blazor
:   ![|Filter Builder in XAF ASP.NET Core Blazor Application, DevExpress|](~/images/xaf-filter-builder-listview-blazor-devexpress.gif)
Windows Forms
:   ![Filter Builder in XAF Windows Forms Application, DevExpress](~/images/xaf-filter-builder-listview-winforms-devexpress.png)

> [!TIP]
> If you use the Filter Builder, XAF saves changes in the [Application Model](xref:112579). Changes persist even if you close the View. You can access these filter settings from the [IModelListView.Filter](xref:DevExpress.ExpressApp.Model.IModelListView.Filter) property in the [Model Editor](xref:112582).

The Filter Builder is available for properties that store filter criteria in ASP.NET Core Blazor and Windows Forms XAF applications. For more information about platform-specific UI controls that implement the Filter Builder, refer to the following topic: [](xref:113564).

### Useful Links

#### Filter Builder in ASP.NET Core Blazor

* [FilterPropertyEditor.](xref:113564#filterpropertyeditor)
* [FilterEditorController.](xref:113141#filtereditorcontroller)
* [Control Property Visibility in Filter Editors.](xref:113564#property-visibility-customization-in-filter-editors)

#### Filter Builder in Windows Forms

* [Control which properties are available in a Filter Builder.](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.FilterColumnsMode)
* Handle the @DevExpress.ExpressApp.Win.Editors.GridListEditor.FilterEditorCreated event to access the currently used Filter Control.   
* Handle the @DevExpress.ExpressApp.Win.Editors.GridListEditor.CreateCustomFilterEditorRepositoryItem event to create a custom [repository item](xref:DevExpress.XtraEditors.Repository.RepositoryItem) in the Filter Builder.  
* Handle the @DevExpress.ExpressApp.Win.Editors.GridListEditor.CustomizeFilterTreeNodeModelPropertyCaption event to customize a property caption when it appears in the Filter Builder.

## Auto Filter Row

The Auto Filter Row functionality is available for the following [List Editors](xref:113189):

ASP.NET Core Blazor
:   @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor
Windows Forms
:   @DevExpress.ExpressApp.Win.Editors.GridListEditor

![Auto Filter Row in XAF ASP.NET Core Blazor Application, DevExpress](~/images/blazor-grid-autofilterrow.png)

> [!TIP]
> If you use the Auto Filter Row, XAF saves changes in the [Application Model](xref:112579). Changes persist even if you close the View. You can access these filter settings via the [IModelListView.Filter](xref:DevExpress.ExpressApp.Model.IModelListView.Filter) property in the [Model Editor](xref:112582).

### Useful Links

* Use the @DevExpress.ExpressApp.SystemModule.IModelListViewShowAutoFilterRow.ShowAutoFilterRow property to toggle Auto Filter Row visibility in the grid that displays the current List View.

* Use the @DevExpress.ExpressApp.SystemModule.IModelClassShowAutoFilterRow.DefaultListViewShowAutoFilterRow property to toggle Auto Filter Row visibility in the default List View.

* [Filter Large List Views With Auto Filter Row.](xref:112919)

## Find Panel or Search Panel

A search component that a List Editor displays at runtime. The following List Editors support this functionality:

ASP.NET Core Blazor
:   @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor
Windows Forms
:   @DevExpress.ExpressApp.Win.Editors.GridListEditor

> [!TIP]
> The filters applied in the search component are not saved in the [Application Model](xref:112579).

### Useful Links

* Use the @DevExpress.ExpressApp.SystemModule.IModelListViewShowFindPanel.ShowFindPanel property to control whether the List Editor displays a search component at runtime.

* Use the @DevExpress.ExpressApp.SystemModule.IModelClassShowFindPanel.DefaultListViewShowFindPanel property to specify the @DevExpress.ExpressApp.SystemModule.IModelListViewShowFindPanel.ShowFindPanel property's default value.

* Use @DevExpress.ExpressApp.ListViewFindPanelAttribute in a business class declaration to control whether a List View of this type displays a search component.
