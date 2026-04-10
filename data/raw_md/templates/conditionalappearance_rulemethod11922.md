The following code snippet changes the `Product` objects in List Views to black on a green background when the `RuleMethod` returns `true`:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
public class Product : BaseObject {
    public virtual decimal Price { get; set; }
    public virtual ProductStatus Status { get; set; }
    [Appearance("RuleMethod", AppearanceItemType = "ViewItem", TargetItems = "*", Context = "ListView",
     BackColor = "Green", FontColor = "Black")]
    public bool RuleMethod() {
        if (Price < 10 && Status == ProductStatus.Active) {
            return true;
        }
        else {
            return false;
        }
    }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
public class Product : BaseObject {
    public Product(Session session) : base(session) { }
    public decimal Price {
        //...
    }
    public ProductStatus Status {
        //...
    }
    [Appearance("RuleMethod", AppearanceItemType = "ViewItem", TargetItems = "*", Context = "ListView",
     BackColor = "Green", FontColor = "Black")]
    public bool RuleMethod() {
        if (Price < 10 && Status == ProductStatus.Active) {
            return true;
        }
        else {
            return false;
        }
    }
}
```
***