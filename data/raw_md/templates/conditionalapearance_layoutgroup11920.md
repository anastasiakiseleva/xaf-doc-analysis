The following code snippet changes the `ProductParameters` layout group caption in Product Detail Views to blue when the product's category is "Seafood":

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
[Appearance("LayoutGroupColoredInDetailView", AppearanceItemType = "LayoutItem",
 TargetItems = "ProductParametersLayoutGroup", Criteria = "Category = 'Seafood'",
 Context = "Product_DetailView", FontColor = "Blue")]
public class Product : BaseObject {
    public virtual string Name { get; set; }
    public virtual decimal Price { get; set; }
    public virtual ProductStatus Status { get; set; }
    public virtual Category Category { get; set; }
}

[DefaultProperty(nameof(Name))]
public class Category : BaseObject {
    public virtual string Name { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
[Appearance("LayoutGroupColoredInDetailView", AppearanceItemType = "LayoutItem",
 TargetItems = "ProductParametersLayoutGroup", Criteria = "Category = 'Seafood'",
 Context = "Product_DetailView", FontColor = "Blue")]
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
[DefaultProperty(nameof(Name))]
public class Category : BaseObject {
    public Category(Session session) : base(session) {}
    public string Name {
        //...
    }
}
```
***
