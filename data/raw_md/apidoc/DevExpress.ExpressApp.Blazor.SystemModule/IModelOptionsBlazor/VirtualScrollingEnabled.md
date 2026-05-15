---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.VirtualScrollingEnabled
name: VirtualScrollingEnabled
type: Property
summary: Specifies whether virtual scrolling is enabled for all List Views in the Blazor application. When enabled, the List Editors load records as the user scrolls (instead of traditional pagination).
syntax:
  content: |-
    [DefaultValue(false)]
    bool VirtualScrollingEnabled { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if virtual scrolling is enabled; otherwise, `false`.'
seealso:
- linkId: DevExpress.Blazor.DxGrid.VirtualScrollingEnabled
---
To enable or disable virtual scrolling globally, do the following:

1. Open the [Model Editor](xref:112582) for the _SolutionName.Blazor.Server\Model.xafml_ file.
2. Navigate to the required List View node: **SolutionName** | **Options**.
3. Specify the `VirtualScrollingEnabled` property.

![|XAF ASP.NET Core Blazor Virtual Scrolling Global Option, DevExpress](~/images/xaf-virtual-scrolling-global-option-model-editor-devexpress.png)

To control virtual scrolling availability for individual List Views, use the [IModelListViewBlazor.VirtualScrollingEnabled](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewBlazor.VirtualScrollingEnabled) property.