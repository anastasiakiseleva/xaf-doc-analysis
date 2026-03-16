---
uid: DevExpress.ExpressApp.SystemModule.IModelClassNavigation.NavigationGroupName
name: NavigationGroupName
type: Property
summary: Indicates the navigation control group to which the current class belongs, according to code.
syntax:
  content: string NavigationGroupName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the navigation control group to which the current class belongs, according to code.
seealso:
- linkId: "113198"
---
If the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) is applied to the class declaration, the value of its GroupName parameter is assigned to the value of this property. Otherwise, the **Default** value is assigned.