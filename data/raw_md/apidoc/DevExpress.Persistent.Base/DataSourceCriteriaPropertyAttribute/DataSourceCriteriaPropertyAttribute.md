---
uid: DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute
name: DataSourceCriteriaPropertyAttribute
type: Class
summary: Specifies the @DevExpress.Data.Filtering.CriteriaOperator used to filter source data for a [reference](xref:113572), [collection](xref:113568), or [enumeration](xref:113552) property.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property, Inherited = true, AllowMultiple = false)]
    public sealed class DataSourceCriteriaPropertyAttribute : ModelExportedValueAttribute
seealso:
- linkId: DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute._members
  altText: DataSourceCriteriaPropertyAttribute Members
- linkId: DevExpress.Persistent.Base.DataSourceCriteriaAttribute
- linkId: DevExpress.Persistent.Base.DataSourcePropertyAttribute
- linkId: "112998"
- linkId: "113052"
- linkId: "113307"
---
You can apply a `DataSourceCriteriaPropertyAttribute` to a [reference](xref:113572), [collection](xref:113568), or [enumeration](xref:113552) property of a business class.
    * For **reference** and **collection** properties, the attribute specifies the @DevExpress.Data.Filtering.CriteriaOperator that filters the [lookup list view](xref:400501) and the list view invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) action. 
    * For **enumeration** properties, the attribute specifies the @DevExpress.Data.Filtering.CriteriaOperator that filters enumeration values in the combo box.

Use [DataSourceCriteriaPropertyAttribute.DataSourceCriteriaProperty](xref:DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute.DataSourceCriteriaProperty) to specify the name of a property that contains the @DevExpress.Data.Filtering.CriteriaOperator.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp{7,9-11,13,16,17}
using DevExpress.Data.Filtering;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...
[DefaultClassOptions]
public class Order : BaseObject {
    [DataSourceCriteriaProperty(nameof(AccessoryCriteria))]
    public virtual Accessory Accessory { get; set; }
    public CriteriaOperator AccessoryCriteria {
        get { return CriteriaOperator.FromLambda<Accessory>(a => a.IsGlobal == true); }
    }
    //For enum properties
    [DataSourceCriteriaProperty(nameof(PendingConfirmedAndProcessingCriteria))]
    public virtual OrderStatus Status { get; set; }

    public CriteriaOperator PendingConfirmedAndProcessingCriteria
        => CriteriaOperator.FromLambda(o => o.Status==OrderStatus.Pending || o.Status==OrderStatus.Confirmed|| o.Status==OrderStatus.Processing);
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

```csharp{8,15-17,20,27-28}
using DevExpress.Data.Filtering;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
[DefaultClassOptions]
public class Order : BaseObject {
    private Accessory fAccessory;
    [DataSourceCriteriaProperty(nameof(AccessoryCriteria))]
    public Accessory Accessory {
        get { return fAccessory; }
        set {
            SetPropertyValue(nameof(Accessory), ref fAccessory, value);
        }
    }
    public CriteriaOperator AccessoryCriteria {
        get { return CriteriaOperator.FromLambda<Accessory>(a => a.IsGlobal == true); }
    }
    //For enum properties
    private OrderStatus fStatus;
    [DataSourceCriteriaProperty(nameof(PendingConfirmedAndProcessingCriteria))]
    public OrderStatus Status {
        get { return fStatus; }
        set {
            SetPropertyValue(nameof(Status), ref fStatus, value);
        }
    }
    public CriteriaOperator PendingConfirmedAndProcessingCriteria
        => CriteriaOperator.FromLambda(o => o.Status==OrderStatus.Pending || o.Status==OrderStatus.Confirmed|| o.Status==OrderStatus.Processing);
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

`DataSourceCriteriaPropertyAttribute` overrides @DevExpress.Persistent.Base.DataSourceCriteriaAttribute when both attributes are applied to the same property.

### Application Model

`DataSourceCriteriaProperty` property value is assigned to the corresponding property of the [Application Model](xref:112580). You can specify the property value directly in the [Model Editor](xref:112582) at the following path: **BOModel | _\<Class\>_ | OwnMembers | _\<Member\>_**.
