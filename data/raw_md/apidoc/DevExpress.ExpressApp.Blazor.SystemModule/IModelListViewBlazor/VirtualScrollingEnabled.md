---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewBlazor.VirtualScrollingEnabled
name: VirtualScrollingEnabled
type: Property
summary: Specifies whether virtual scrolling is enabled in the List Editor. When enabled, the editor loads records as the user scrolls the page (instead of traditional pagination).
syntax:
  content: |-
    [ModelBrowsable(typeof(IModelListViewBlazorVirtualScrollingVisibilityCalculator))]
    bool VirtualScrollingEnabled { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if virtual scrolling is enabled; otherwise, `false`.'
seealso:
- linkId: DevExpress.Blazor.DxGrid.VirtualScrollingEnabled
---
To enable or disable virtual scrolling in an individual List View, do the following:

1. Open the [Model Editor](xref:112582) for the _SolutionName.Blazor.Server\Model.xafml_ file.
2. Navigate to the required List View node: **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView**.
3. Specify the `VirtualScrollingEnabled` property.


![|XAF ASP.NET Core Blazor Virtual Scrolling in Individual List Views, DevExpress](~/images/xaf-virtual-scrolling-individual-listview-model-editor-devexpress.png)

To control virtual scrolling globally, use the [IModelOptionsBlazor.VirtualScrollingEnabled](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.VirtualScrollingEnabled) property.