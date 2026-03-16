---
uid: DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.DefaultChildItemsDisplayStyle
name: DefaultChildItemsDisplayStyle
type: Property
summary: Specifies the default navbar group style when the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property is set to [NavigationStyle.NavBar](xref:DevExpress.ExpressApp.Templates.ActionContainers.NavigationStyle.NavBar).
syntax:
  content: |-
    [DefaultValue(ItemsDisplayStyle.LargeIcons)]
    [ModelBrowsable(typeof(ChildItemsDisplayStyleOptionModelVisibilityCalculator))]
    ItemsDisplayStyle DefaultChildItemsDisplayStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.ActionContainers.ItemsDisplayStyle
    description: An [](xref:DevExpress.ExpressApp.Templates.ActionContainers.ItemsDisplayStyle) enumeration value that specifies the default navbar group style.
seealso: []
---
This setting has no effect in XAF Blazor applications. For more information, refer to the following help topic: [Navigation System](xref:113198).
