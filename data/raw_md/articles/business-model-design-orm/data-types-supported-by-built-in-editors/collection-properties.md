---
uid: "113568"
seealso:
- linkId: "402188"
title: Collection Properties
owner: Ekaterina Kiseleva
---
# Collection Properties

XAF applications display collection properties as nested List Views or as Tag Box editors.

Refer to the following topics for information on relationships between entities in code and UI:

* [Relationships Between Persistent Objects in Code and UI (XPO)](xref:112654)
* [](xref:402958)

> [!NOTE]
> Refer to the **Property Editors** | **Collection Properties** section in the **Feature Center** demo installed with XAF to see Collection Property Editors in action. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)]

## Examples
* [Collection Properties in XPO](xref:113569)
* [Collection Properties in EF Core](xref:113570)
* [XAF - How to display a collection property as a checked list box](https://github.com/DevExpress-Examples/xaf-how-to-display-a-collection-property-as-a-checked-list-box)

## ListPropertyEditor

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor ListPropertyEditor, DevExpress](~/images/xaf-blazor-collection-properties-devexpress.gif)
Windows Forms
:   ![XAF Windows Forms ListPropertyEditor, DevExpress](~/images/xaf-winforms-collection-properties-devexpress.gif)

The platform-agnostic **ListPropertyEditor** creates a [Template](xref:112609) and [Frame](xref:112608) that contain a [List View](xref:112611). This List View uses the [ListView.CollectionSource](xref:DevExpress.ExpressApp.ListView.CollectionSource) of the [](xref:DevExpress.ExpressApp.PropertyCollectionSource) type.

For more information on Templates, Frames, and Views, refer to the [UI Element Overview](xref:112607) topic.

In the [Model Editor](xref:112582), set the [IModelMemberViewItem.View](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.View) property to a custom List View to use this View instead of the default one.

You can hide **New**, **Delete**, **Link**, or **Unlink** Actions associated with the Property Editor. In the Model Editor, set the List View's [AllowNew](xref:DevExpress.ExpressApp.Model.IModelView.AllowNew), [AllowDelete](xref:DevExpress.ExpressApp.Model.IModelView.AllowDelete), [AllowLink](xref:DevExpress.ExpressApp.Model.IModelListView.AllowLink), or [AllowUnlink](xref:DevExpress.ExpressApp.Model.IModelListView.AllowUnlink) property to `false` to hide these Actions.

## TagBoxListPropertyEditor

### ASP.NET Core Blazor

![|XAF ASP.NET Core Blazor TagBoxListPropertyEditor, DevExpress](~/images/xaf-blazor-tagboxpropertyeditor-devexpress.png)

Component Model:
* `DevExpress.ExpressApp.Blazor.Components.Models.DxButtonModel`
* `DevExpress.ExpressApp.Blazor.Editors.DxTagBoxListModel`
	
Component: `DevExpress.ExpressApp.Blazor.Components.TagBoxListComponent` -- a wrapper that contains the @DevExpress.Blazor.DxTagBox`2 editor and @DevExpress.Blazor.DxButton control shipped with the DevExpress ASP.NET Core Blazor Library.
	
[!include[](~/templates/tagboxpropertyeditor-description.md)]

To edit an item in a pop-up window, users can double-click the tag in the editor. In [TabbedMDI](xref:DevExpress.ExpressApp.UIType#tabbedmdi---blazor) mode, users can hold <kbd>Alt</kbd> and double-click on the tag to edit it in a new window.

To access and customize a `TagBoxListPropertyEditor` in XAF applications, create a @DevExpress.ExpressApp.ViewController that accesses a `TagBoxListPropertyEditor` object and modifies the underlying @DevExpress.Blazor.DxTagBox`2 control. For more information about Property Editor customization in Detail Views, refer to the following topic: [](xref:402153).

### Windows Forms

![|XAF Windows Forms TagBoxListPropertyEditor, DevExpress](~/images/xaf-win-tagboxpropertyeditor-devexpress.png)

Control: `TagBoxListEdit` -- a descendant of the [](xref:DevExpress.XtraEditors.BaseEdit) editor shipped with the XtraEditors Library.
	
Repository Item: `RepositoryItemTokenEdit` -- a descendant of the XtraEditors Library's @DevExpress.XtraEditors.Repository.RepositoryItemTokenEdit.

[!include[](~/templates/tagboxpropertyeditor-description.md)]

To edit an item in a pop-up window, users can double-click the tag in the editor. In [TabbedMDI](xref:DevExpress.ExpressApp.UIType#tabbedmdi---winforms) mode, users can hold <kbd>Ctrl</kbd> + <kbd>Shift</kbd> and double-click on the tag to edit it in a new window.

Users can click the **New** button to create a new collection item. To clear the editor (remove all selected tags), users can press the <kbd>Ctrl</kbd>+<kbd>Delete</kbd> key combination. To delete selected tags or delete the last added tag, users can press <kbd>Backspace</kbd>. For more information about the available shortcuts, refer to the following topic: [](xref:17088#end-user-capabilities).

## ComboBoxListPropertyEditor

### ASP.NET Core Blazor

![|XAF ASP.NET Core Blazor ComboBoxListPropertyEditor, DevExpress](~/images/xaf-blazor-comboboxlistpropertyeditor-devexpress.gif)

[!include[](~/templates/comboboxlistpropertyeditor-description.md)]

To edit an item in a pop-up window, users can click an item in the editor.

Users can press the **New** button or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd> to create a new collection item. When the checkbox column is focused, <kbd>Enter</kbd> inverts the current selection. <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Enter</kbd> saves the selection and closes the pop-up window.

To access and customize a `ComboBoxListPropertyEditor` in XAF applications, create a @DevExpress.ExpressApp.ViewController that accesses a `ComboBoxListPropertyEditor` object. For more information about Property Editor customization in Detail Views, refer to the following topic: [](xref:402153).

The following code snippet specifies a value list separator in the `ComboBoxListPropertyEditor` in a Detail View:

# [MySolution.Blazor.Server\Controllers\ComboBoxListPropertyEditorController.cs](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

namespace MySolution.Blazor.Server.Controllers;

public partial class ComboBoxListPropertyEditorController : ViewController<DetailView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<ComboBoxListPropertyEditor>(this, e => {
            e.Separator = ',';
        });
    }
}
```
***

### Windows Forms

![|XAF Windows Forms ComboBoxListPropertyEditor, DevExpress](~/images/xaf-win-comboboxlistpropertyeditor-devexpress.gif)

Control: `ComboBoxLookupEdit` -- a descendant of [](xref:DevExpress.XtraEditors.BaseEdit) from the DevExpress WinForms Data Editors library.
	
Repository Item: `ComboBoxRepositoryItemLookupEdit`.

[!include[](~/templates/comboboxlistpropertyeditor-description.md)]

To edit an item in a pop-up window, users can double-click an item in the editor. 

Users can use the **New** button or <kbd>Ctrl</kbd>+<kbd>N</kbd> to create a new collection item. <kbd>Shift</kbd>+<kbd>Enter</kbd> selects or deselects the current focused item.