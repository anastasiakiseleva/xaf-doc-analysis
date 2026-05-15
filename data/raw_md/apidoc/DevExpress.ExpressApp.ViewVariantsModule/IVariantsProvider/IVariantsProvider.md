---
uid: DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider
name: IVariantsProvider
type: Interface
summary: Implemented by objects that provide a list of view variants available for the specific View, and stores the variant selected by the user.
syntax:
  content: public interface IVariantsProvider
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider._members
  altText: IVariantsProvider Members
---
The default implementation of the **IVariantsProvider** interface used by the [View Variants Module](xref:113011) is [](xref:DevExpress.ExpressApp.ViewVariantsModule.ModelVariantsProvider), that stores view variants in the Application Model. You can create a custom **IVariantsProvider** implementation and pass it to the [ViewVariantsModule.VariantsProvider](xref:DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule.VariantsProvider) property.

The following snippet illustrates how to implement an **IVariantsProvider** that stores View Variants in the database.

# [C#](#tab/tabid-csharp)

```csharp
public class DatabaseViewVariantsProvider : IVariantsProvider {
    XafApplication application;
    public DatabaseViewVariantsProvider(XafApplication application) {
        Guard.ArgumentNotNull(application, nameof(application));
        this.application = application;
    }
    public VariantsInfo GetVariants(string rootVariantViewId) {
        VariantsInfo result = null;
        if(application.Security.IsAuthenticated) {
            using(IObjectSpace os = application.CreateObjectSpace(typeof(ViewVariantsObject))) {
                ViewVariantsObject variants = os.FirstOrDefault<ViewVariantsObject>(obj => obj.RootViewId == rootVariantViewId);
                if(variants != null && (variants.Items.Count >= 2)) {
                    List<VariantInfo> items = new List<VariantInfo>();
                    foreach(ViewVariantObject variant in variants.Items) {
                        items.Add(new VariantInfo(variant.ID.ToString(), variant.ViewId, variant.Caption));
                    }
                    string currentVariantId;
                    if(variants.CurrentVariant != null) {
                        currentVariantId = variants.CurrentVariant.ID.ToString();
                    }
                    else {
                        currentVariantId = variants.Items[0].ID.ToString();
                    }
                    result = new VariantsInfo(variants.RootViewId, currentVariantId, items);
                }
            }
        }
        return result;
    }
    public void SaveCurrentVariantId(string rootViewId, string currentVariantId) {
        using(IObjectSpace os = application.CreateObjectSpace(typeof(ViewVariantsObject))) {
            ViewVariantObject variant = os.GetObjectByKey<ViewVariantObject>(Guid.Parse(currentVariantId));
            if((variant == null) || (variant.Owner == null)) {
                throw new InvalidOperationException();
            }
            variant.Owner.CurrentVariant = variant;
            os.CommitChanges();
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Public Class DatabaseViewVariantsProvider
    Implements IVariantsProvider
    Private application As XafApplication
    Public Sub New(ByVal application As XafApplication)
        Guard.ArgumentNotNull(application, NameOf(application))
        Me.application = application
    End Sub
    Public Function GetVariants(ByVal rootVariantViewId As String) As VariantsInfo
        Dim result As VariantsInfo = Nothing
        If application.Security.IsAuthenticated Then
            Using os As IObjectSpace = application.CreateObjectSpace(GetType(ViewVariantsObject))
                Dim variants As ViewVariantsObject = os.FirstOrDefault(Function(obj as ViewVariantsObject) obj.RootViewId = rootVariantViewId)
                If variants IsNot Nothing AndAlso (variants.Items.Count >= 2) Then
                    Dim items As New List(Of VariantInfo)()
                    For Each [variant] As ViewVariantObject In variants.Items
                        items.Add(New VariantInfo([variant].Oid.ToString(), [variant].ViewId, [variant].Caption))
                    Next [variant]
                    Dim currentVariantId As String
                    If variants.CurrentVariant IsNot Nothing Then
                        currentVariantId = variants.CurrentVariant.Oid.ToString()
                    Else
                        currentVariantId = variants.Items(0).Oid.ToString()
                    End If
                    result = New VariantsInfo(variants.RootViewId, currentVariantId, items)
                End If
            End Using
        End If
        Return result
    End Function
    Public Sub SaveCurrentVariantId(ByVal rootViewId As String, ByVal currentVariantId As String)
        Using os As IObjectSpace = application.ObjectSpaceProvider.CreateObjectSpace()
            Dim [variant] As ViewVariantObject = os.GetObjectByKey(Of ViewVariantObject)(Guid.Parse(currentVariantId))
            If ([variant] Is Nothing) OrElse ([variant].Owner Is Nothing) Then
                Throw New InvalidOperationException()
            End If
            [variant].Owner.CurrentVariant = [variant]
            os.CommitChanges()
        End Using
    End Sub
End Class
```

***

The following code illustrates persistent objects used by **DatabaseViewVariantsProvider** to store View Variants:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[Index(nameof(RootViewId), IsUnique = true)]
[DefaultClassOptions,XafDefaultProperty(nameof(RootViewId))]
public class ViewVariantsObject : BaseObject {
    [RuleUniqueValue]
    public virtual string RootViewId { get; set; }
    public virtual ViewVariantObject CurrentVariant { get; set; }
    public virtual IList<ViewVariantObject> Items { get; set; } = new ObservableCollection<ViewVariantObject>();
}

[XafDefaultProperty(nameof(Caption))]
public class ViewVariantObject : BaseObject {
    [InverseProperty(nameof(ViewVariantsObject.Items))]
    public virtual ViewVariantsObject Owner { get; set; }
    public virtual string ViewId { get; set; }
    public virtual string Caption { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions, XafDefaultProperty(nameof(RootViewId))]
public class ViewVariantsObject : BaseObject {
    public ViewVariantsObject(Session session) : base(session) { }
    [Indexed(Unique = true), RuleUniqueValue]
    public string RootViewId { 
        get { return GetPropertyValue<string>(nameof(RootViewId)); } 
        set { SetPropertyValue<string>(nameof(RootViewId), value); }
    }
    public ViewVariantObject CurrentVariant { 
        get { return GetPropertyValue<ViewVariantObject>(nameof(CurrentVariant)); } 
        set { SetPropertyValue<ViewVariantObject>(nameof(CurrentVariant), value); }
    }
    [Association]
    public XPCollection<ViewVariantObject> Items { 
        get { return GetCollection<ViewVariantObject>(nameof(Items)); }
    }
}
[XafDefaultProperty(nameof(Caption))]
public class ViewVariantObject : BaseObject {
    public ViewVariantObject(Session session) : base(session) { }
    [Association]
    public ViewVariantsObject Owner { 
        get { return GetPropertyValue<ViewVariantsObject>(nameof(Owner)); } 
        set { SetPropertyValue<ViewVariantsObject>(nameof(Owner), value); }
    }
    public string ViewId { 
        get { return GetPropertyValue<string>(nameof(ViewId)); }
        set { SetPropertyValue<string>(nameof(ViewId), value); } 
    }
    public string Caption { 
        get { return GetPropertyValue<string>(nameof(Caption)); } 
        set { SetPropertyValue<string>(nameof(Caption), value); } 
    }
}
```

# [VB.NET (XPO)](#tab/tabid-vb-xpo)

```vb
<DefaultClassOptions, XafDefaultProperty(NameOf(RootViewId))>
Public Class ViewVariantsObject
    Inherits BaseObject

    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub
    <Indexed(Unique := True), RuleUniqueValue>
    Public Property RootViewId() As String
        Get
            Return GetPropertyValue(Of String)(NameOf(RootViewId))
        End Get
        Set(ByVal value As String)
            SetPropertyValue(Of String)(NameOf(RootViewId), value)
        End Set
    End Property
    Public Property CurrentVariant() As ViewVariantObject
        Get
            Return GetPropertyValue(Of ViewVariantObject)(NameOf(CurrentVariant))
        End Get
        Set(ByVal value As ViewVariantObject)
            SetPropertyValue(Of ViewVariantObject)(NameOf(CurrentVariant), value)
        End Set
    End Property
    <Association>
    Public ReadOnly Property Items() As XPCollection(Of ViewVariantObject)
        Get
            Return GetCollection(Of ViewVariantObject)(NameOf(Items))
        End Get
    End Property
End Class
<XafDefaultProperty(NameOf(Caption))>
Public Class ViewVariantObject
    Inherits BaseObject

    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub
    <Association>
    Public Property Owner() As ViewVariantsObject
        Get
            Return GetPropertyValue(Of ViewVariantsObject)(NameOf(Owner))
        End Get
        Set(ByVal value As ViewVariantsObject)
            SetPropertyValue(Of ViewVariantsObject)(NameOf(Owner), value)
        End Set
    End Property
    Public Property ViewId() As String
        Get
            Return GetPropertyValue(Of String)(NameOf(ViewId))
        End Get
        Set(ByVal value As String)
            SetPropertyValue(Of String)(NameOf(ViewId), value)
        End Set
    End Property
    Public Property Caption() As String
        Get
            Return GetPropertyValue(Of String)(NameOf(Caption))
        End Get
        Set(ByVal value As String)
            SetPropertyValue(Of String)(NameOf(Caption), value)
        End Set
    End Property
End Class
```

***