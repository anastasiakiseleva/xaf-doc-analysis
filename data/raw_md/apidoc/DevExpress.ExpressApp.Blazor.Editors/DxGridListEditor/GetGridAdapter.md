---
uid: DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.GetGridAdapter
name: GetGridAdapter()
type: Method
summary: Provides access to a data grid adapter.
syntax:
  content: public IDxGridAdapter GetGridAdapter()
  return:
    type: DevExpress.ExpressApp.Blazor.Editors.IDxGridAdapter
    description: A data grid adapter.
seealso: []
---

> [!NOTE]
> To access the Editor, use the corresponding Component Model instead. For more information, refer to the following Breaking Change ticket: [Blazor - The ListEditor.Control, PropertyEditor.Control, and ViewItem.Control properties return Component Models instead of Adapters](https://supportcenter.devexpress.com/ticket/details/t1230710/blazor-the-listeditor-control-propertyeditor-control-and-viewitem-control-properties)

The List View editor exposes the `GetGridAdapter` method that returns the [Component Adapter](xref:DevExpress.ExpressApp.Blazor.Editors.IDxGridAdapter).