---
uid: DevExpress.Persistent.Base.NavigationItemAttribute.GroupName
name: GroupName
type: Property
summary: Specifies the name of the first-level navigation item to which an item corresponding to the required business class is added.
syntax:
  content: public string GroupName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value which represents the name of the group within the navigation control.
seealso: []
---
If the group specified by this property does not currently exist, it is created, and an item is added to it.

If this property is not specified, the default first-level navigation item name is used. This name is specified by the [NavigationItemAttribute.DefaultGroupName](xref:DevExpress.Persistent.Base.NavigationItemAttribute.DefaultGroupName) property.

Since the structure of navigation items is initially generated in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems) node, you can change the required group name via the [Model Editor](xref:112830).