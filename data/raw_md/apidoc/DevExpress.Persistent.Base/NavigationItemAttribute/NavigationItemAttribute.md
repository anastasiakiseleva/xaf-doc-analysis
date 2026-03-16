---
uid: DevExpress.Persistent.Base.NavigationItemAttribute
name: NavigationItemAttribute
type: Class
summary: Specifies whether a class will have a corresponding item in the navigation control.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface, Inherited = false)]
    public class NavigationItemAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.NavigationItemAttribute._members
  altText: NavigationItemAttribute Members
- linkId: "112701"
- linkId: "113198"
---
An XAF application usually includes a navigation control in the main window. This control is a part of the [Navigation System](xref:113198). The control implements the **ShowNavigationItem** Action, and the control's items are that Action's items. This Action allows users to switch between Views in the main window:

ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor Navigation Control, DevExpress|](~/images/xaf-blazor-navigation-control-devexpress.png)
Windows Forms
:   ![XAF Windows Forms Navigation Control, DevExpress](~/images/navigationitemattribute115586.png)

The Navigation Action's items are added from the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems) node. This node's items are created either manually via the [Model Editor](xref:112830), or in code via the `NavigationItem` attribute applied to the required business class. The attribute's [NavigationItemAttribute.IsNavigationItem](xref:DevExpress.Persistent.Base.NavigationItemAttribute.IsNavigationItem) property must be set to `true`.

To specify the navigation item within the navigation control, specify the [NavigationItemAttribute.GroupName](xref:DevExpress.Persistent.Base.NavigationItemAttribute.GroupName) attribute. By default, an item is added to the default item specified by the [NavigationItemAttribute.DefaultGroupName](xref:DevExpress.Persistent.Base.NavigationItemAttribute.DefaultGroupName) property.

If the [NavigationItemAttribute.IsNavigationItem](xref:DevExpress.Persistent.Base.NavigationItemAttribute.IsNavigationItem) property is set to `false`, or if this attribute is not applied, the **ShowNavigationItem** Action item list will not have the corresponding item.

In the following code snippet, the `NavigationItem` attribute is applied to the `TestContact` class. As a result, the Test Contact item is added to the specified `MyContacts` navigation item in the navigation control (see the image above).

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[NavigationItem("MyContacts")]
public class TestContact : BaseObject {
    public virtual string Name { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[NavigationItem("MyContacts")]
public class TestContact : BaseObject {
   public TestContact(Session session) : base(session) {}
   private string name;
   public string Name {
      get {
         return name;
      }
      set {
         SetPropertyValue(nameof(Name), ref name, value);
      }
   }
}
```
***

When you need to apply the [](xref:DevExpress.Persistent.Base.CreatableItemAttribute) and [](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute) attributes in addition to the `NavigationItem` attribute, it is easier to apply a single [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) attribute.
