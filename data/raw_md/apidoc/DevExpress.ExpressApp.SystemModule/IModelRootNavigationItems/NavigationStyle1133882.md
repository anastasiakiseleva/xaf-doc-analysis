---
uid: DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle
name: NavigationStyle
type: Property
summary: Specifies the control to be used as the navigation control.
syntax:
  content: |-
    [DefaultValue(NavigationStyle.NavBar)]
    NavigationStyle NavigationStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.ActionContainers.NavigationStyle
    description: A [](xref:DevExpress.ExpressApp.Templates.ActionContainers.NavigationStyle) enumeration value that specifies which control to use as the navigation control.
seealso: []
---

In the Model Editor, XAF filters the available `NavigationStyle` property's values by platform.

| Platform | Value |
|-|-|
| ASP.NET Core Blazor  | `TreeList`, `Accordion` |
| Windows Forms  | `NavBar`, `TreeList`, `Accordion` |