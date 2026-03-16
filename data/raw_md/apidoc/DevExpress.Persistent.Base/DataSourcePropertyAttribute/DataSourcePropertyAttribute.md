---
uid: DevExpress.Persistent.Base.DataSourcePropertyAttribute
name: DataSourcePropertyAttribute
type: Class
summary: Specifies the data source for a [reference](xref:113572), [collection](xref:113568), or [enumeration](xref:113552) property.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property, Inherited = true, AllowMultiple = false)]
    public class DataSourcePropertyAttribute : ModelExportedValuesAttribute
seealso:
- linkId: DevExpress.Persistent.Base.DataSourcePropertyAttribute._members
  altText: DataSourcePropertyAttribute Members
- linkId: DevExpress.Persistent.Base.DataSourceCriteriaAttribute
- linkId: DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute
- linkId: "112993"
- linkId: "112998"
- linkId: "113052"
- linkId: "113307"
---
You can apply a `DataSourcePropertyAttribute` to a [reference](xref:113572), [collection](xref:113568), or [enumeration](xref:113552) property of a business class.
    * For **reference** and **collection** properties, the attribute specifies the data source for the [lookup list view](xref:400501) and the list view invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) action. 
    * For **enumeration** properties, the attribute specifies the data source with enumeration values. These values are displayed in the combo box.

Use [DataSourcePropertyAttribute.DataSourceProperty](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourceProperty) to specify the name of a collection property used as the data source. The collection must contain objects of the target property's type or its descendants. The collection property must provide information about the element type. It can be an associated collection, a generic collection, or an untyped collection decorated with the `CollectionAttribute`.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp{10,16-24,27,31-33}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel;
using System.Collections.ObjectModel;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class Order : BaseObject {
    // Specify the AvailableAccessories collection as a data source for the Accessory property
    [DataSourceProperty(nameof(AvailableAccessories))]
    public virtual Accessory Accessory { get; set; }

    private IList<Accessory> fAvailableAccessories;

    [NotMapped, Browsable(false)] // Prohibits showing the AvailableAccessories collection separately
    public IList<Accessory> AvailableAccessories {
        get {
            if(fAvailableAccessories == null) {
                // Retrieve all Accessory objects
                fAvailableAccessories = ObjectSpace.GetObjects<Accessory>();
            }
            return fAvailableAccessories;
        }
    }

    //For Enumeration Properties
    [DataSourceProperty(nameof(PendingConfirmedAndProcessing))]
    public virtual OrderStatus Status { get; set; }
    
    [NotMapped, Browsable(false)] // Prohibits showing the PendingConfirmedAndProcessing collection separately
    public IList<OrderStatus> PendingConfirmedAndProcessing
        => new List<OrderStatus>() { OrderStatus.Pending,OrderStatus.Confirmed,OrderStatus.Processing};
    }

    public class Accessory : BaseObject {
        public virtual string Name { get; set; }
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

# [C# (XPO)](#tab/tabid-csharp)

```csharp{11,20-28,32,40-41}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations.Schema;
// ...
[DefaultClassOptions]
public class Order : BaseObject {
    private Accessory fAccessory;
    // Set the AvailableAccessories collection as a data source for the Accessory property
    [DataSourceProperty(nameof(AvailableAccessories))]
    public Accessory Accessory {
        get { return fAccessory; }
        set {
            SetPropertyValue(nameof(Accessory), ref fAccessory, value);
        }
    }
    private XPCollection<Accessory> fAvailableAccessories;
    [Browsable(false)] // Prohibits showing the AvailableAccessories collection separately
    public XPCollection<Accessory> AvailableAccessories {
        get {
            if(fAvailableAccessories == null) {
                // Retrieve all Accessory objects
                fAvailableAccessories = new XPCollection<Accessory>(Session);
            }
            return fAvailableAccessories;
        }
    }

    //For Enumeration Properties
    private OrderStatus fStatus;
    [DataSourceProperty(nameof(PendingConfirmedAndProcessing))]
    public OrderStatus Status {
        get { return fStatus; }
        set {
            SetPropertyValue(nameof(Status), ref fStatus, value);
        }
    }
    [NotMapped, Browsable(false)] // Prohibits showing the PendingConfirmedAndProcessing collection separately
    public IList<OrderStatus> PendingConfirmedAndProcessing
        => new List<OrderStatus>() { OrderStatus.Pending, OrderStatus.Confirmed, OrderStatus.Processing };
}

public class Accessory : BaseObject {
    // ...
    private string fName;
    public string Name {
        get { return fName; }
        set {
            SetPropertyValue(nameof(Name), ref fName, value);
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

For more information, refer to the following help topic: [How to: Implement Cascading Filtering for Lookup List Views](xref:112681).

### Default Collection

Use the @DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourcePropertyIsNullMode property to specify the default collection displayed by the lookup list view if @DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourceProperty returns `null`.

If you set the @DevExpress.Persistent.Base.DataSourcePropertyIsNullMode property to `CustomCriteria`, use the @DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourcePropertyIsNullCriteria property to specify the filter criteria. In the criteria, you can use [function criteria operators](xref:113307) and the [current object parameter](xref:113204).

> [!NOTE]
> * The criteria specified by the `DataSourceProperty` attribute in a base business class remains applied in descendants.
> * `DataSourceProperty` and `DataSourceCriteria` attributes do not affect visibility of objects added to a lookup via the **New** action.

### Application Model

`DataSourcePropertyAttribute` property value is assigned to the corresponding property of the [Application Model](xref:112580). You can specify the property value directly in the [Model Editor](xref:112582) at the following path: **BOModel | _\<Class\>_ | OwnMembers | _\<Member\>_**.

### Limitation

[!include[](~/templates/datasourcepropertyvsservermode_note11161.md)]
