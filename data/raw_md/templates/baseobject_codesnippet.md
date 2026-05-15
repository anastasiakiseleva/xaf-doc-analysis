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

# [VB.NET (XPO)](#tab/tabid-vb-xpo)

```vb
Imports DevExpress.Persistent.Base
Imports DevExpress.Persistent.BaseImpl
Imports DevExpress.Xpo
' ...
<DefaultClassOptions()>
Public Class Contact
    Inherits BaseObject 
    ' BaseObject contains an auto-generated Guid key, you cannot add a custom key
    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub
    Private fFirstName As String
    Public Property FirstName() As String
        Get
            Return fFirstName
        End Get
        Set(ByVal value as String)
            SetPropertyValue(NameOf(FirstName), fFirstName, value)
        End Set
    End Property
End Class
```

***

[`DefaultClassOptions`]: xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute
[`/(BaseObject).[^c]/`]: xref:DevExpress.Persistent.BaseImpl.BaseObject
[`Session`]: xref:DevExpress.Xpo.Session

The following help topic lists base classes that you can use in XPO-based applications: [Base Persistent Classes](xref:113146).