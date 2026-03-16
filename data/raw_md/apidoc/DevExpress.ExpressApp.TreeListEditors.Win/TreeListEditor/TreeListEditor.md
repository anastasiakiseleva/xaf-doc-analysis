---
uid: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor
name: TreeListEditor
type: Class
summary: Represents a Windows Forms [List Editor](xref:113189) that displays data in the form of a tree-like structure.
syntax:
  content: 'public class TreeListEditor : ColumnsListEditor, IDXPopupMenuHolder, IComplexListEditor, IControlOrderProvider, IOrderProvider, ILookupListEditor, IFocusedElementCaptionProvider, INodeObjectAdapterProvider, ISupportFooter, IExportable, ISupportUpdate, IRequireContextMenu, IRequireDXMenuManager, ISupportBorderStyle, ISupportFilterEditor'
seealso:
- linkId: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor._members
  altText: TreeListEditor Members
- linkId: "113189"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-win-enable-inplace-editing-in-tree-list-view
  altText: 'GitHub Example: XAF WinForms - How to enable in-place editing in the tree List View (TreeListEditor)'
---
[List Views](xref:112611) use List Editors to display object collections in a UI. `TreeListEditor` ships with the [TreeList Editors module](xref:112841), and displays data in the form of a tree:

![XAF Windows Forms Tree List Editor, DevExpress](~/images/treelisteditor2116347.png)

To display object collections, `TreeListEditor` uses an instance of the `ObjectTreeList` as the underlying control. `ObjectTreeList` is a descendant of the [](xref:DevExpress.XtraTreeList.TreeList) class.

`TreeListEditor` supports a range of features out of the box:

* Implements the `ISupportAppearanceCustomization` interface to support [conditional appearance](xref:113286):
    
    ![TreeListEditor_ConditionalAppearance](~/images/treelisteditor_conditionalappearnce116374.png)

* Implements the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface to enable export through the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) and printing through the [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController):
    
    ![Export_TreeListEditor](~/images/export_treelisteditor116969.png)
    
    ![TreeListEditor_PrintPreview](~/images/treelisteditor_printpreview116341.png)

* Implements the `IDXPopupMenuHolder` interface and provides the **ActionDX** pop-up menu:
    
    ![TreeListEditor_PopupMenu](~/images/treelisteditor_popupmenu116342.png)

* Implements the `IControlOrderProvider` interface to support the  [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController)'s **PreviousObject** and **NextObject** [Actions](xref:112622):
    
    ![RecordsNavigationController_Actions_Win](~/images/recordsnavigationcontroller_actions_win115934.png)

Since it is not possible to display an arbitrary object collection in the form of a tree, the objects that `TreeListEditor` displays must implement the [](xref:DevExpress.Persistent.Base.General.ITreeNode) interface. To learn how to implement this interface, refer to the following topic: [Display a Tree List using the ITreeNode Interface](xref:112837).

For additional information on `TreeListEditor` and an overview of the TreeList Editors module, refer to the following topic: [](xref:112836).

> [!NOTE]
> `TreeListEditor` supports only [Client](xref:118449) mode ([CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode)).