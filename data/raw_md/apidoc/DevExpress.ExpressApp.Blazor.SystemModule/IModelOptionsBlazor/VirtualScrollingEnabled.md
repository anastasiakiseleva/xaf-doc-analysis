---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.VirtualScrollingEnabled
name: VirtualScrollingEnabled
type: Property
summary: Specifies whether [virtual scrolling](xref:DevExpress.Blazor.DxGrid.VirtualScrollingEnabled) is enabled for all List Views that use @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor. When enabled, the List Editors load records as the user scrolls (instead of traditional pagination).
syntax:
  content: |-
    [DefaultValue(false)]
    bool VirtualScrollingEnabled { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if virtual scrolling is enabled for all List Views that use @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor; otherwise, `false`.'
seealso:
- linkId: DevExpress.Blazor.DxGrid.VirtualScrollingEnabled
---

To disable virtual scrolling globally, open Model Editor for your ASP.NET Core Blazor application and specify `false` for the `VirtualScrollingEnabled` property:

![|XAF ASP.NET Core Blazor Virtual Scrolling Global Option, DevExpress](~/images/xaf-virtual-scrolling-global-option-model-editor-devexpress.png)

To disable virtual scrolling for an individual List View, use the [IModelListViewBlazor.VirtualScrollingEnabled](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewBlazor.VirtualScrollingEnabled) property.