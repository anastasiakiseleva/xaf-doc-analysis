The following example demonstrates how to declare a persistent class:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
// ...
[DefaultClassOptions]
public class Contact : BaseObject {
    public virtual string FirstName { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
// ...
[DefaultClassOptions]
public class Contact : BaseObject {
    // BaseObject contains an auto-generated Guid key, you cannot add a custom key
    public Contact(Session session) : base(session) { }
    string fFirstName;
    public string FirstName {
        get { return fFirstName; }
        set { SetPropertyValue(nameof(FirstName), ref fFirstName, value); }
    }
}
```
***

[`DefaultClassOptions`]: xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute
[`/(BaseObject).[^c]/`]: xref:DevExpress.Persistent.BaseImpl.BaseObject
[`Session`]: xref:DevExpress.Xpo.Session

The following help topic lists base classes that you can use in XPO-based applications: [Base Persistent Classes](xref:113146).