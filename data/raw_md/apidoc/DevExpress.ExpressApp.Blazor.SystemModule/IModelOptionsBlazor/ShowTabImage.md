---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.ShowTabImage
name: ShowTabImage
type: Property
summary: Specifies whether XAF displays tabs with icons in ASP.NET Core Blazor applications that use the `TabbedMDI` @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.UIType.
syntax:
  content: |-
    [DefaultValue(true)]
    [ModelBrowsable(typeof(TabbedMdiOptionModelVisibilityCalculator))]
    bool ShowTabImage { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if XAF displays tabs with icons in ASP.NET Core Blazor applications that use the `TabbedMDI` @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.UIType; otherwise, `false`.'
seealso: []
---
Use this property to specify whether you want to display tabs with icons in your application in Tabbed MDI mode. Use the @DevExpress.ExpressApp.Model.IModelClass.ImageName property to specify icons for your business classes.  
Open the _MySolution\Blazor.Server\Model.xafml_ file and navigate to the **Options** node to locate the property.


`true`
:   ![|XAF ASP.NET Core Blazor Tabs with Icons, DevExpress](~/images/xaf-blazor-tabbedmdi-showtabimagetrue-devexpress.png)

`false`
:   ![|XAF ASP.NET Core Blazor Tabs without Icons, DevExpress](~/images/xaf-blazor-tabbedmdi-showtabimagefalse-devexpress.png)