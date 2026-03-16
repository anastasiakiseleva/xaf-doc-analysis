---
uid: DevExpress.ExpressApp.Win.Editors.GridListEditor
name: GridListEditor
type: Class
summary: Represents the [List Editor](xref:113189) used by default in XAF Windows Forms applications, to display [List Views](xref:112611) in a UI.
syntax:
  content: 'public class GridListEditor : WinColumnsListEditor, ISupportNewItemRowPosition, ISupportFooter, ILookupListEditor, IGridListEditorTestable, ILookupEditProvider, IRequireContextMenu, IRequireDXMenuManager, IConfigurableLookupListEditor, ISupportBorderStyle, ISupportFilterEditor'
seealso:
- linkId: DevExpress.ExpressApp.Win.Editors.GridListEditor._members
  altText: GridListEditor Members
- linkId: DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor
- linkId: "113189"
- linkId: "113694"
---
List Editors are used by List Views to display object collections in a UI. The `GridListEditor` provides the most common data representation in the form of a two-dimensional table:

![WinGridListEditor](~/images/wingridlisteditor116271.png)

To display object collections, the `GridListEditor` uses an instance of the [](xref:DevExpress.XtraGrid.GridControl) class as the underlying control.

The `GridListEditor` supports a wide range of features out of the box:

* Implements the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface - can be exported via the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) and printed via the [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController):
    
    ![Export_GridListEditor](~/images/export_gridlisteditor116967.png)
    
    ![Tutorial_EM_Lesson3_1_0](~/images/tutorial_em_lesson3_1_0115583.png)
* Implements the [](xref:DevExpress.ExpressApp.SystemModule.IDataAwareExportable) interface - the [data-aware](xref:17733) export type ([](xref:DevExpress.Export.ExportType)) is used by default when exporting to Excel formats.
* Implements the `ISupportAppearanceCustomization` interface - supports [conditional appearance](xref:113286):
    
    ![ConditionalAppearance_Win](~/images/conditionalappearance_win115674.png)
* Implements the [](xref:DevExpress.ExpressApp.Win.SystemModule.IHtmlFormattingSupport) interface - supports [HTML formatting](xref:113130) of column captions:
    
    ![HTML_Formatting3](~/images/html_formatting3116156.png)
* Implements the `IDXPopupMenuHolder` interface, and provides an `ActionDX` pop-up menu:
    
    ![ContextMenuTemplate](~/images/contextmenutemplate116134.png)
* Implements the `IControlOrderProvider` interface - supports the  [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s **PreviousObject** and **NextObject** [Actions](xref:112622):
    
    ![RecordsNavigationController_Actions_Win](~/images/recordsnavigationcontroller_actions_win115934.png)
* Implements the [](xref:DevExpress.ExpressApp.ISupportNewItemRowPosition) interface - has a new item row. It allows end-users to create a new object directly in a List View:
    
    ![GridListEditorNewItemRow](~/images/gridlisteditornewitemrow116274.png)
    
    The new item row option is available when a List View is displayed in edit mode. To set the row's location, use the `DefaultListViewOptions` attribute in code. Alternatively, use the [IModelListViewNewItemRow.NewItemRowPosition](xref:DevExpress.ExpressApp.SystemModule.IModelListViewNewItemRow.NewItemRowPosition) property of the appropriate **Views** | **List View** node. By default, the row is not displayed.
* Supports the preview section. It is a non-editable region in data rows that displays a particular column's content across all the List Editor's columns:
    
    ![Tutorial_EF_Lesson9_1](~/images/tutorial_ef_lesson9_1115472.png)
    
    The column whose content is displayed in the preview section is specified by the [IModelListViewPreviewColumn.PreviewColumnName](xref:DevExpress.ExpressApp.SystemModule.IModelListViewPreviewColumn.PreviewColumnName) property of the Application Model's [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node.
* Supports [Banded Grid Views](xref:114637).
    
    ![Bands_WinAdv](~/images/bands_winadv117594.png)
    
    For details, refer to the [List View Bands Layout](xref:113695) and [](xref:113694) topics.
* Supports the in-place editing feature. It allows the `GridListEditor` to represent its cells via various [Property Editors](xref:113097):
    
    ![InplaceEditing](~/images/inplaceediting116272.png)
* Supports the filter panel. It allows you to quickly filter the grid:
    
    ![GridListEditor_FilterPane](~/images/gridlisteditor_filterpane116331.png)
    
    The filter panel can be activated via the [IModelListViewShowAutoFilterRow.ShowAutoFilterRow](xref:DevExpress.ExpressApp.SystemModule.IModelListViewShowAutoFilterRow.ShowAutoFilterRow) property of the Application Model's [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node.
* Supports filtering, sorting and grouping:
    
    ![GridListEditorGrouping](~/images/gridlisteditorgrouping116273.png)
    
    You can specify a group interval, so that groups are not created for each unique value, but for specific value ranges. To do this, use the [IModelColumn.GroupInterval](xref:DevExpress.ExpressApp.Model.IModelColumn.GroupInterval) property of the Application Model's [!include[Node_Views_ListView_Columns](~/templates/node_views_listview_columns111387.md)] |  **Column**  node.
* Supports all [List View data access modes](xref:113683). These modes can be activated via the [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) property of the appropriate **Views** | **List View** node.

The `GridListEditor` is used by default in XAF Windows Forms applications. So generally, there is no need to instantiate it in your code. However, the `GridListEditor` exposes a range of useful public members that are not defined in the base [](xref:DevExpress.ExpressApp.Editors.ListEditor) class. These members can be accessed, for example, from a custom [Controller](xref:112621) or [Action](xref:112622). The following table lists them.

| Property Name | Member Type | Description |
|---|---|---|
| [WinColumnsListEditor.ColumnCreated](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.ColumnCreated) | Event | Occurs after a column has been created in the `GridListEditor`'s `GridView`. Handle this event to be notified after a column has been created or recreated in the `GridListEditor`'s `GridView`. |
| [WinColumnsListEditor.Grid](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.Grid) | Property | Provides access to the `GridListEditor`'s `GridControl` control. |
| [GridListEditor.GridView](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor.GridView) | Property | Provides access to the `GridControl`'s View that is used to represent data in two-dimensional grid form. |
| [GridListEditor.ProcessSelectedItemBySingleClick](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor.ProcessSelectedItemBySingleClick) | Property | Specifies whether a List View's record must be processed after a click or a double-click. |
| [GridListEditor.TrackMousePosition](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor.TrackMousePosition) | Property | When this property is set to `true`, moving the mouse within the `GridListEditor`'s region changes the focus to the row that is under the mouse pointer. |

To see examples on how to access the `GridListEditor` from a View Controller, refer to the following topics:

* [](xref:402154)
* [How to: Filter Large List Views using the Auto Filter Row](xref:112919)
* [How to: Filter List Views on the UI Specific Level](xref:112652)