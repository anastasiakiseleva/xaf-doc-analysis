---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.RestoreTabbedMdiLayout
name: RestoreTabbedMdiLayout
type: Property
summary: Specifies whether XAF should restore open tabs when you start an ASP.NET Core Blazor application that uses the `TabbedMDI` @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.UIType.
syntax:
  content: |-
    [DefaultValue(false)]
    [ModelBrowsable(typeof(TabbedMdiOptionModelVisibilityCalculator))]
    bool RestoreTabbedMdiLayout { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if XAF should restore open tabs on next app startup; otherwise, `false`.'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy.MaxTabLimit
- linkId: DevExpress.ExpressApp.Blazor.BlazorMdiShowViewStrategy.TabOverflowStrategy
---
When an XAF ASP.NET Core Blazor application uses the `TabbedMDI` @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.UIType, you can control whether you want to save the tabs arrangement upon closing the browser window and restore it when you start the application again.  
Open the _MySolution\Blazor.Server\Model.xafml_ file and navigate to the **Options** node to locate the property.