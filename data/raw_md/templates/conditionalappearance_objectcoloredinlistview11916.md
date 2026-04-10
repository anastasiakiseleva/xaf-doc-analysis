The following code snippet changes the `Product` objects to maroon on a red background in List Views when the product's price exceeds 50:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
[Appearance("RedPriceObject", AppearanceItemType = "ViewItem", TargetItems = "*",
    Criteria = "Price>50", Context = "ListView", BackColor = "Red",
        FontColor = "Maroon", Priority = 2)]
public class Product : BaseObject {
    public virtual string Name { get; set; }
    public virtual decimal Price { get; set; }
    public virtual ProductStatus Status { get; set; }
    public virtual Category Category { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
[Appearance("RedPriceObject", AppearanceItemType = "ViewItem", TargetItems = "*",
    Criteria = "Price>50", Context = "ListView", BackColor = "Red",
        FontColor = "Maroon", Priority = 2)]
public class Product : BaseObject {
    public Product(Session session) : base(session) { }
    public string Name {
        //...
    }
    public decimal Price {
        //...
    }
    public ProductStatus Status {
        //...
    }
    public Category Category {
        //...
    }
}
```
***