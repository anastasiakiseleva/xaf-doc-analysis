---
uid: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor
name: WinColumnsListEditor
type: Class
summary: The base class for built-in grid-like WinForms [List Editors](xref:113189).
syntax:
  content: |-
    [Browsable(false)]
    public abstract class WinColumnsListEditor : ColumnsListEditor, IControlOrderProvider, IOrderProvider, IDXPopupMenuHolder, IComplexListEditor, IHtmlFormattingSupport, IFocusedElementCaptionProvider, ISupportAppearanceCustomization, ISupportEnabledCustomization, IExportable, ISupportFilter, ISupportUpdate, IGridViewOptions, IDataAwareExportableCsv, IDataAwareExportable, IDataAwareExportableXls, IDataAwareExportableXlsx, IObjectRecordSupport, IInstantFeedbackRecordSupport
seealso:
- linkId: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor._members
  altText: WinColumnsListEditor Members
---
The **WinColumnsListEditor** serves as the base class for WinForms List Editors that visualize object collections in the form of a grid. In such grids, a row represents a particular object and columns represent the object properties.

The **WinColumnsListEditor**'s members are not intended to be used in your code and are used internally by XAF. To customize the columns displayed by a List Editor for a particular [List View](xref:112611), use the [Application Model](xref:112580)'s corresponding [!include[Node_Views_ListView_Columns](~/templates/node_views_listview_columns111387.md)] node. To learn how to customize the Application Model in code, refer to the [Access the Application Model in Code](xref:112810).