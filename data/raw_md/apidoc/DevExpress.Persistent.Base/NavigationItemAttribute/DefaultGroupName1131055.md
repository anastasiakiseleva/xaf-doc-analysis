---
uid: DevExpress.Persistent.Base.NavigationItemAttribute.DefaultGroupName
name: DefaultGroupName
type: Property
summary: Specifies the name of the default first-level navigation item in the navigation control to which the required item is added.
syntax:
  content: public static string DefaultGroupName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value representing the default first-level navigation item name.
seealso: []
---
This property value is used when the [NavigationItemAttribute.GroupName](xref:DevExpress.Persistent.Base.NavigationItemAttribute.GroupName) property is not specified.

By default, this property is set to the "Default" value.

Since the structure of navigation items is initially generated in the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems) node, you can change the default name via the [Model Editor](xref:112830).