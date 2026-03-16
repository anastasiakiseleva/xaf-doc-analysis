---
uid: DevExpress.ExpressApp.Model.IModelChoiceActionItemChildItemsDisplayStyle.ChildItemsDisplayStyle
name: ChildItemsDisplayStyle
type: Property
summary: Specifies the navbar group style when the [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property is set to [NavigationStyle.NavBar](xref:DevExpress.ExpressApp.Templates.ActionContainers.NavigationStyle.NavBar). Has effect in WinForms applications only.
syntax:
  content: |-
    [ModelBrowsable(typeof(ChildItemsDisplayStyleOptionModelVisibilityCalculator))]
    ItemsDisplayStyle ChildItemsDisplayStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.ActionContainers.ItemsDisplayStyle
    description: An [](xref:DevExpress.ExpressApp.Templates.ActionContainers.ItemsDisplayStyle) enumeration value specifying the navbar group style.
seealso: []
---
The images below illustrate how the **ChildItemsDisplayStyle** property value influences the navbar group appearance.

[comment]: <> (<\!--<%ObjectImage$117207#Tutorial_UIC_Navigation_02%>-->)

![ChildItemsDisplayStyle_LargeIcons](~/images/childitemsdisplaystyle_largeicons128845.png)

![ChildItemsDisplayStyle_List](~/images/childitemsdisplaystyle_list128846.png)

For details, refer to the [Navigation System](xref:113198) help topic.