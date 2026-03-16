---
uid: DevExpress.Persistent.Base.CreatableItemAttribute
name: CreatableItemAttribute
type: Class
summary: Specifies whether a class will have a corresponding item in the **New** Action's item list.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface, Inherited = false)]
    public class CreatableItemAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.CreatableItemAttribute._members
  altText: CreatableItemAttribute Members
- linkId: "112701"
---
Each application built via the **XAF** has the **New** Action by default. This Action allows end-users to create objects of one of the types listed in the drop-down menu:

![CreatableItemAttribute](~/images/creatableitemattribute115585.png)

Note that the first item in this list is the type of objects currently listed in a View. This item is added automatically. So, this item cannot be disabled by applying the **CreatableItem(false)** attribute to the corresponding business class. The remaining items are added from the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems) node. This node's items are created either manually via the [Model Editor](xref:112830) or in code via the **CreatableItem** attribute applied to the required business class. The attribute's [CreatableItemAttribute.IsCreatableItem](xref:DevExpress.Persistent.Base.CreatableItemAttribute.IsCreatableItem) property must be set to **true**.

If the [CreatableItemAttribute.IsCreatableItem](xref:DevExpress.Persistent.Base.CreatableItemAttribute.IsCreatableItem) property is set to **false**, or if this attribute is not applied, the **New** Action item list will not have the corresponding item. However, if a user has the permissions required to create objects of a particular type and the currently active [View](xref:112611) is of this type, the **New** Action will still have the automatically added item. In this case, the user will still be able to create objects of this type via the **New** Action. You can, however, set the [Application Model](xref:112580)'s  [IModelView.AllowNew](xref:DevExpress.ExpressApp.Model.IModelView.AllowNew) property for the required [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] or **DetailView** node to **false**. In this instance, the **New** Action will not be available.

In the example below, the **CreatableItem** attribute, with its **IsCreatableItem** property set to **true**, by default, is applied to the TestContact class. As a result, the Test Contact item is added to the **New** Action's list (see the image above). This allows end-users to create TestContact objects, no matter what View is currently displayed.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[CreatableItem]
public class TestContact : BaseObject {
   public virtual string Name { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[CreatableItem]
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

When you need to apply the [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) and [](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute) attributes, in addition to the **CreatableItem** attribute, it is easier to apply a single [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) attribute.
