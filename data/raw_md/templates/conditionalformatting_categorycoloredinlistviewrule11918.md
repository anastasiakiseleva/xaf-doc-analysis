The following code snippet changes the `Category` property in List Views to blue when its value is "Seafood":

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
[Appearance("CategoryColoredInListView", AppearanceItemType = "ViewItem", TargetItems = "Category",
 Criteria = "Category = 'Seafood'", Context = "ListView", FontColor = "Blue", Priority = 1)]
public class Product : BaseObject {
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
[Appearance("CategoryColoredInListView", AppearanceItemType = "ViewItem", TargetItems = "Category",
 Criteria = "Category = 'Seafood'", Context = "ListView", FontColor = "Blue", Priority = 1)]
public class Product : BaseObject {
    public Product(Session session) : base(session) { }
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