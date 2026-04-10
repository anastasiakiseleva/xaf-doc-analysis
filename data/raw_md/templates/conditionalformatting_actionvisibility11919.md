The following code snippet disables a Product's **Deactivate** Action when the `Status` property is set to "Inactive" in all Product Views. The Action ID specified in this rule contains the class name ("Product.Deactivate") because the **Deactivate** Action is declared using the [](xref:DevExpress.Persistent.Base.ActionAttribute). If you declare an Action in a Controller, specify its ID without the class name, for example, "Delete" or "Unlink".

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
[Appearance("ActionState", AppearanceItemType = "Action",
    TargetItems = "Product.Deactivate",
        Criteria = "Status = 'Inactive'", Context = "Any", Enabled = false)]
public class Product : BaseObject {
    public virtual ProductStatus Status { get; set; }
    [Action(PredefinedCategory.RecordEdit, Caption = "Deactivate Product...", AutoCommit = true,
     TargetObjectsCriteria = "Status = 'Active'",
      SelectionDependencyType = MethodActionSelectionDependencyType.RequireSingleObject)]
    public void Deactivate() {
        Status = ProductStatus.Inactive;
    }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
//...
[Appearance("ActionState", AppearanceItemType = "Action",
    TargetItems = "Product.Deactivate",
        Criteria = "Status = 'Inactive'", Context = "Any", Enabled = false)]
public class Product : BaseObject {
    public Product(Session session) : base(session) { }
    public ProductStatus Status {
        //...
    }   
    [Action(PredefinedCategory.RecordEdit, Caption = "Deactivate Product...", AutoCommit = true,
     TargetObjectsCriteria = "Status = 'Active'",
      SelectionDependencyType = MethodActionSelectionDependencyType.RequireSingleObject)]
    public void Deactivate() {
        Status = ProductStatus.Inactive;
    }
}
```
***

> [!NOTE]
> When you use a Conditional Appearance Rule (for example, the `Appearance` attribute) to hide an Action, it remains visible in List Views. XAF displays this Action as disabled. This helps avoid complex calculations that could hinder the application's performance.