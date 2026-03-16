---
uid: DevExpress.Persistent.Base.DataSourceCriteriaAttribute
name: DataSourceCriteriaAttribute
type: Class
summary: Specifies the [criteria expression](xref:4928) used to filter source data for a [reference](xref:113572), [collection](xref:113568), or [enumeration](xref:113552) property.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property, Inherited = true, AllowMultiple = false)]
    public sealed class DataSourceCriteriaAttribute : ModelExportedValueAttribute
seealso:
- linkId: DevExpress.Persistent.Base.DataSourceCriteriaAttribute._members
  altText: DataSourceCriteriaAttribute Members
- linkId: "112681"
  altText: 'How to: Implement Cascading Filtering for Lookup List Views'
- linkId: "112993"
- linkId: DevExpress.Persistent.Base.DataSourcePropertyAttribute
- linkId: DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute
- linkId: "112998"
- linkId: "113052"
- linkId: "113307"
- linkId: "112612"
---
You can apply a `DataSourceCriteriaAttribute` to a [reference](xref:113572), [collection](xref:113568), or [enumeration](xref:113552) property of a business class.
    * For **reference** and **collection** properties, the attribute specifies the [criteria expression](xref:4928) that filters the [lookup list view](xref:400501) or a list view invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) action. 
    * For **enumeration** properties, the attribute specifies the [criteria expression](xref:4928) that filters values displayed in the combo box.

Use [DataSourceCriteriaAttribute.DataSourceCriteria](xref:DevExpress.Persistent.Base.DataSourceCriteriaAttribute.DataSourceCriteria) to specify filter criteria. You can use [function criteria operators](xref:113307) and the [current object parameter](xref:113204). Refer to the following help topic for more information about building criteria: <xref:113052>.
# [C# (EF Core)](#tab/tabid-csharp)
```csharp
using DevExpress.Data.Filtering;
//...
EnumProcessingHelper.RegisterEnum<OrderStatus>();
```
***

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp{6,10}
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
    public class Order : BaseObject {
        [DataSourceCriteria("IsGlobal = true")]
        public virtual Accessory Accessory { get; set; }

        //For enum property
        [DataSourceCriteria("Status = ##Enum#MyNamespace.OrderStatus,Pending# or Status = ##Enum#MyNamespace.OrderStatus,Confirmed# or Status = ##Enum#MyNamespace.OrderStatus,Processing#")]
        public virtual OrderStatus Status { get; set; }
    }

    public class Accessory : BaseObject {
        public virtual bool IsGlobal { get; set; }
    }

    public enum OrderStatus {
        Pending,
        Confirmed,
        Processing,
        Shipped,
        Delivered,
        Canceled,
        Returned
    }
    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp{8,19}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
[DefaultClassOptions]
public class Order : BaseObject {
    // ...
    private Accessory fAccessory;
    [DataSourceCriteria("IsGlobal = true")]
    public Accessory Accessory {
        get {
            return fAccessory;
        }
        set {
            SetPropertyValue(nameof(Accessory), ref fAccessory, value);
        }
    }
    //For enum property
    private OrderStatus fStatus;
    [DataSourceCriteria("Status = ##Enum#MyNamespace.OrderStatus,Pending# or Status = ##Enum#MyNamespace.OrderStatus,Confirmed# or Status = ##Enum#MyNamespace.OrderStatus,Processing#")]
    public OrderStatus Status {
        get {
            return fStatus;
        }
        set {
            SetPropertyValue(nameof(Status), ref fStatus, value);
        }
    }
}
public class Accessory : BaseObject {
    // ...
    private bool fIsGlobal;
    public bool IsGlobal {
        get { return fIsGlobal; }
        set {
            SetPropertyValue(nameof(IsGlobal), ref fIsGlobal, value);
        }
    }
}
public enum OrderStatus {
    Pending,
    Confirmed,
    Processing,
    Shipped,
    Delivered,
    Canceled,
    Returned
}
```

***

### Application Model

@DevExpress.Persistent.Base.DataSourceCriteriaAttribute.DataSourceCriteria property value is assigned to the [IModelCommonMemberViewItem.DataSourceCriteria](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DataSourceCriteria) property of the [Application Model](xref:112580). You can specify property value directly in the [Model Editor](xref:112582) at the following path: **BOModel | _\<Class\>_ | OwnMembers | _\<Member\>_**.

### Important Notes
* The criteria specified by the `DataSourceCriteria` attribute in a base business class remains applied in descendants.
* `DataSourceProperty` and `DataSourceCriteria` attributes do not affect visibility of objects added to a lookup via the **New** action.
* [!include[DataSourceCriteria_This](~/templates/datasourcecriteria_this111276.md)]
* @DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute overrides `DataSourceCriteriaAttribute` when both attributes are applied to the same property.
* When applying `DataSourceCriteriaAttribute` to an enumeration property, the left part of the criteria string must match the property name.
