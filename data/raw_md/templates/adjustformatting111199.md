Note that the value of the business class property associated with the customized Property Editor should be formatted accordingly to display the time part of the `DateTime` value:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Model;
//...
[ModelDefault("DisplayFormat", "{0:MM.dd.yyyy hh:mm:ss}")]
[ModelDefault("EditMask", "MM.dd.yyyy hh:mm:ss")]
public virtual DateTime CreatedOn { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Model;
//...
private DateTime createdOn;
[ModelDefault("DisplayFormat", "{0:MM.dd.yyyy hh:mm:ss}")]
[ModelDefault("EditMask", "MM.dd.yyyy hh:mm:ss")]
public DateTime CreatedOn {
    get { return createdOn; }
    set { SetPropertyValue(nameof(CreatedOn), ref createdOn, value); }
}
```
***

For additional information, refer to the following topic: [](xref:402141).