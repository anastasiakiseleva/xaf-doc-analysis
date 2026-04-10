The following code snippet changes the `Category` layout item's caption in Product Detail Views to blue when the product's category is "Seafood":

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
public class Product : BaseObject {
    [Appearance("CategoryColoredInDetailView", AppearanceItemType = "LayoutItem",
         TargetItems = "Category", Criteria = "Category = 'Seafood'", Context = "DetailView",
             FontColor = "Blue")]
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
public class Product : BaseObject {
    public Product(Session session) : base(session) { }
    [Appearance("CategoryColoredInDetailView", AppearanceItemType = "LayoutItem",
         TargetItems = "Category", Criteria = "Category = 'Seafood'", Context = "DetailView",
             FontColor = "Blue")]
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