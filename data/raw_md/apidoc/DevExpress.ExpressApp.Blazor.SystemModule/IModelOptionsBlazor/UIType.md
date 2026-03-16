---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.UIType
name: UIType
type: Property
summary: Specifies the Show View Strategy in XAF ASP.NET Core Blazor applications.
syntax:
  content: |-
    [DefaultValue(UIType.SingleWindowSDI)]
    UIType UIType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.UIType
    description: A @DevExpress.ExpressApp.UIType enumeration value that specifies the type of the UI used in XAF ASP.NET Core Blazor applications.
seealso: []
---
Use this property to specify the [Show View Strategy](xref:DevExpress.ExpressApp.ShowViewStrategyBase) in your application.  
Open the _MySolution\Blazor.Server\Model.xafml_ file and navigate to the **Options** node to locate the property.


@DevExpress.ExpressApp.UIType.SingleWindowSDI
:   ![|XAF ASP.NET Core Blazor Single Window SDI, DevExpress](~/images/xaf-blazor-singlewindowsdi-devexpress.png)

@DevExpress.ExpressApp.UIType.TabbedMDI
:   ![|XAF ASP.NET Core Blazor Tabbed MDI, DevExpress](~/images/xaf-blazor-tabbedmdi-devexpress.png)