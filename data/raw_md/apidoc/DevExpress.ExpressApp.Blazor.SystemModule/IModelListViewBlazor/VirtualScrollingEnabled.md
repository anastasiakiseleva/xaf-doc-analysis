---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewBlazor.VirtualScrollingEnabled
name: VirtualScrollingEnabled
type: Property
summary: Specifies whether [virtual scrolling](xref:DevExpress.Blazor.DxGrid.VirtualScrollingEnabled) is enabled in @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor. When enabled, the List Editor loads records as the user scrolls (instead of traditional pagination).
syntax:
  content: |-
    [ModelBrowsable(typeof(IModelListViewBlazorVirtualScrollingVisibilityCalculator))]
    bool VirtualScrollingEnabled { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if virtual scrolling is enabled in @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor; otherwise, `false`.'
seealso:
- linkId: DevExpress.Blazor.DxGrid.VirtualScrollingEnabled
---

To disable virtual scrolling in an individual List View, open Model Editor for your ASP.NET Core Blazor application, navigate to the List View, and specify `false` for the `VirtualScrollingEnabled` property:

![|XAF ASP.NET Core Blazor Virtual Scrolling in Individual List Views, DevExpress](~/images/xaf-virtual-scrolling-individual-listview-model-editor-devexpress.png)

To disable virtual scrolling globally, use the [IModelOptionsBlazor.VirtualScrollingEnabled](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.VirtualScrollingEnabled) property.