---
uid: DevExpress.Persistent.Base.VisibleInReportsAttribute
name: VisibleInReportsAttribute
type: Class
summary: When applied to [business classes](xref:113664), specifies whether end-users can create reports on objects of the required class. When applied to a business class property, specifies if the target property is visible in the Report Designer.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Property | AttributeTargets.Interface, Inherited = false)]
    public class VisibleInReportsAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.VisibleInReportsAttribute._members
  altText: VisibleInReportsAttribute Members
- linkId: "112701"
---
Decorate the class with this attribute and set the [VisibleInReportsAttribute.IsVisible](xref:DevExpress.Persistent.Base.VisibleInReportsAttribute.IsVisible) property to **true** to show an item for the decorated class in the following **Data Type** drop-down lists: 

* in the [Report Wizard](xref:4254)

  ![VisibleInReportsAttribute](~/images/visibleinreportsattribute115587.png)

* in a Detail View of a [Mail Merge Template](xref:400006)
  
  ![VisibleInReportsAttribute_Office](~/images/visibleinreportsattribute_office.png)

The value passed as the **VisibleInReports** attribute's parameter is set for the [IModelClassReportsVisibility.IsVisibleInReports](xref:DevExpress.ExpressApp.Model.IModelClassReportsVisibility.IsVisibleInReports) property of the corresponding **BOModel** | **_\<Class\>_** node.

The attribute parameter's default value is **true**. You can apply the **VisibleInReports** attribute to a class without this parameter to allow users to create reports and analysis on specified type objects and use this class as the document's data source for the [Mail Merge](xref:400006) operation. 

The following example shows how to apply the **VisibleInReports** attribute to the **TestContact** class:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[VisibleInReports]
public class TestContact : BaseObject {
    public virtual string Name { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[VisibleInReports]
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

When you need to apply the [](xref:DevExpress.Persistent.Base.CreatableItemAttribute) and [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) attributes in addition to the **VisibleInReports** attribute, it is easier to apply a single [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) attribute.

Apply the **VisibleInReports** attribute with the **false** parameter value to a business class property to hide this property from the Report Designer.