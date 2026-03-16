---
uid: DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor.TreeListModel
name: TreeListModel
type: Property
summary: Exposes members of the underlying @DevExpress.Blazor.DxTreeList class.
syntax:
  content: public DxTreeListModel TreeListModel { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Blazor.Editors.Models.DxTreeListModel
    description: A `DevExpress.ExpressApp.Blazor.Editors.Models.DxTreeListModel` object that you can use to access @DevExpress.Blazor.DxTreeList settings.
seealso: []
---
Use the `DxTreeListEditor.TreeListModel` property to access the Tree List component properties.

The following code snippet demonstrates a controller in an XAF ASP.NET Core Blazor project that changes the `ColumnResizeMode` property value:

[!include[dxtreelisteditor-access](~/templates/dxtreelisteditor-access.md)]