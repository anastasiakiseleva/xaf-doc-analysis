---
uid: "112660"
seealso: []
title: 'How to: Support a Context Menu for a Custom WinForms List Editor'
owner: Ekaterina Kiseleva
---
# How to: Support a Context Menu for a Custom WinForms List Editor

In XAF applications, [List Views](xref:112611) can have context menus filled with [Actions](xref:112622). For this purpose, the [List Editor](xref:113189) displaying a List View should support the **IRequireContextMenu** and **IRequireDXMenuManager** interfaces. This topic describes how to implement these interfaces in the **WinCustomListEditor** demonstrated in the [How to: Implement a Custom WinForms List Editor](xref:112659) topic.

The following image illustrates the context menu invoked for the **WinCustomListEditor**.

![PopupMenuForWinThumbnailEditor](~/images/popupmenuforwinthumbnaileditor115390.png)
> [!NOTE]
> You can see the code implemented here in the **FeatureCenter** demo installed with **XAF**. This demo is located in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder by default.

To enable the context menu in a custom List Editor, modify its code in the following manner.

# [C#](#tab/tabid-csharp)

```csharp
[ListEditor(typeof(IPictureItem))]
public class WinCustomListEditor : ListEditor, /* ...*/ IRequireContextMenu, IRequireDXMenuManager {
    #region IRequireContextMenu Members
    private void BarManager_QueryShowPopupMenu(object sender, QueryShowPopupMenuEventArgs e) {
        if (e.Control != control) {
            e.Cancel = true;
            e.BreakShowPopupMenu = false;
        }
    }
    public void SetMenu(PopupMenu popupMenu, BarManager barManager) {
        barManager.SetPopupContextMenu(control, popupMenu);
        barManager.QueryShowPopupMenu += BarManager_QueryShowPopupMenu;
    }
        #endregion

        #region IRequireDXMenuManager Members
        public void SetMenuManager(IDXMenuManager menuManager) { }
        #endregion
}
```
***

If you implement a List Editor using a descendant of the [](xref:DevExpress.XtraEditors.Container.EditorContainer) control, initialize the [EditorContainer.MenuManager](xref:DevExpress.XtraEditors.Container.EditorContainer.MenuManager) property in the **SetMenuManager** method.

In the **QueryShowPopupMenu** event handler, you can specify whether or not to cancel showing the context menu for the current region of the control using the **e.Cancel** parameter. For instance, you can use the following logic for the [](xref:DevExpress.XtraGrid.Views.Grid.GridView) control.

# [C#](#tab/tabid-csharp)

```csharp
GridHitTest hitTest = gridView.CalcHitInfo(gridControl.PointToClient(e.Position)).HitTest;
e.Cancel = !(((hitTest == GridHitTest.Row) || 
    (hitTest == GridHitTest.RowCell) || (hitTest == GridHitTest.EmptyRow) || 
    (hitTest == GridHitTest.RowDetail) || (hitTest == GridHitTest.None)));
```
***