---
uid: "113179"
seealso:
- linkId: '403711'
- linkId: "4928"
- linkId: DevExpress.Xpo.PersistentAttribute
- linkId: DevExpress.Xpo.PersistentAliasAttribute
- linkId: "2875"
- linkId: "113258"
- linkId: "113583"
title: 'Calculate a Property Value Based on Values from a Detail Collection'
---
# Calculate a Property Value Based on Values from a Detail Collection

This topic describes how to implement a business class, so that one of its properties is calculated based on a property(ies) of the objects contained in the child object collection.

![CalculatePropertyBasedOnDetailCollection ](~/images/calculatepropertybasedondetailcollection116394.png)

> [!Tip]
> A sample project for this task is available on our GitHub: [How to calculate a master property based on values from a detail collection](https://github.com/DevExpress-Examples/XAF_how-to-calculate-a-master-property-based-on-values-from-a-detail-collection/).

## Initial Class Implementation
A **Product** class has a collection of **Order** objects. The **Product** and **Order** classes are associated by the [One-to-Many](xref:112654) relationship, which means that a **Product** object may be associated with several **Order** objects. The collection of **Order** objects is aggregated. **Order** objects are created, belonging to one of the **Product** objects. When the master object is removed, all the objects in its aggregated collection are removed as well.

The following snippet illustrates the **Product** class implementation.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject {
    public Product(Session session) : base(session) { }
    private string fName;
    public string Name {
        get { return fName; }
        set { SetPropertyValue(nameof(Name), ref fName, value); }
    }
    [Association("Product-Orders"), Aggregated]
    public XPCollection<Order> Orders {
        get { return GetCollection<Order>(nameof(Orders)); }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
<DefaultClassOptions> _
Public Class Product
    Inherits BaseObject
    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub
    Private fName As String
    Public Property Name() As String
        Get
            Return fName
        End Get
        Set(ByVal value As String)
            SetPropertyValue(NameOf(Name), fName, value)
        End Set
    End Property
    <Association("Product-Orders"), Aggregated> _
    Public ReadOnly Property Orders() As XPCollection(Of Order)
        Get
            Return GetCollection(Of Order)(NameOf(Orders))
        End Get
    End Property
End Class
```

***

The following snippet illustrates the **Order** class implementation.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Order : BaseObject {
    public Order(Session session) : base(session) { }
    private string fDescription;
    public string Description {
         get { return fDescription; }
         set { SetPropertyValue(nameof(Description), ref fDescription, value); }
    }
    private decimal fTotal;
    public decimal Total {
        get { return fTotal; }
        set { SetPropertyValue(nameof(Total), ref fTotal, value); }
    }
    private Product fProduct;
    [Association("Product-Orders")]
    public Product Product {
        get { return fProduct; }
        set { SetPropertyValue(nameof(Product), ref fProduct, value); }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
<DefaultClassOptions> _
Public Class Order
    Inherits BaseObject
    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub
    Private fDescription As String
    Public Property Description() As String
         Get
             Return fDescription
         End Get
         Set(ByVal value As String)
             SetPropertyValue(NameOf(Description), fDescription, value)
         End Set
    End Property
    Private fTotal As Decimal
    Public Property Total() As Decimal
        Get
            Return fTotal
        End Get
        Set(ByVal value As Decimal)
            SetPropertyValue(NameOf(Total), fTotal, value)
        End Set
    End Property
    Private fProduct As Product
    <Association("Product-Orders")> _
    Public Property Product() As Product
        Get
            Return fProduct
        End Get
        Set(ByVal value As Product)
            SetPropertyValue(NameOf(Product), fProduct, value)
        End Set
    End Property
End Class
```
***

> [!NOTE]
> You can modify an object from the child collection in a separate Detail View and save it. In this scenario, the parent object may also be marked as modified in a separate object space. If the collection property is not decorated with the [](xref:DevExpress.Xpo.AggregatedAttribute), you need to refresh the parent object before saving changes. To avoid this, disable the [XpoDefault.IsObjectModifiedOnNonPersistentPropertyChange](xref:DevExpress.Xpo.XpoDefault.IsObjectModifiedOnNonPersistentPropertyChange) option before starting the application.

## Implement Non-Persistent Calculated Properties
An implementation of "lazy" calculated (calculated on demand) properties is described in this section.

Omit the property setter to implement a non-persistent property. The following code snippet demonstrates the implementation of three calculated properties - the **OrdersCount**, **OrdersTotal** and **MaximumOrder**.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject {
    // ...
    private int? fOrdersCount = null;
    public int? OrdersCount {
        get {
            if(!IsLoading && !IsSaving && fOrdersCount == null)
                UpdateOrdersCount(false);
            return fOrdersCount;
        }
    }
    private decimal? fOrdersTotal = null;
    public decimal? OrdersTotal {
        get {
           if(!IsLoading && !IsSaving && fOrdersTotal == null)
                UpdateOrdersTotal(false);
            return fOrdersTotal;
        }
    }
    private decimal? fMaximumOrder = null;
    public decimal? MaximumOrder {
        get {
            if(!IsLoading && !IsSaving && fMaximumOrder == null)
                UpdateMaximumOrder(false);
            return fMaximumOrder;
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
<DefaultClassOptions> _
Public Class Product
    Inherits BaseObject
    ' ...
    Private fOrdersCount As Nullable(Of Integer) = Nothing
    Public ReadOnly Property OrdersCount() As Nullable(Of Integer)
        Get
            If (Not IsLoading) AndAlso (Not IsSaving) AndAlso Not fOrdersCount.HasValue Then
                UpdateOrdersCount(False)
            End If
            Return fOrdersCount
        End Get
    End Property
    Private fOrdersTotal As Nullable(Of Decimal) = Nothing
    Public ReadOnly Property OrdersTotal() As Nullable(Of Decimal)
        Get
           If (Not IsLoading) AndAlso (Not IsSaving) AndAlso Not fOrdersTotal.HasValue Then
                UpdateOrdersTotal(False)
           End If
            Return fOrdersTotal
        End Get
    End Property
    Private fMaximumOrder As Nullable(Of Decimal) = Nothing
    Public ReadOnly Property MaximumOrder() As Nullable(Of Decimal)
        Get
            If (Not IsLoading) AndAlso (Not IsSaving) AndAlso Not fMaximumOrder.HasValue Then
                UpdateMaximumOrder(False)
            End If
            Return fMaximumOrder
        End Get
    End Property
End Class
```

***

In the code above, the **Order** class contains the **Total** property and the **Product** class has the **MaximumOrder** and **OrdersTotal** properties. These **Product**'s properties are calculated based on **Total** properties of the aggregated **Orders**. The **OrderCount** property is also added to the **Product** class. This property exposes the number of aggregated **Orders**.

The properties' business logic is contained into three separate methods - **UpdateOrdersCount**, **UpdateOrdersTotal** and **UpdateMaximumOrder**. These methods are invoked in the property getters. Having the business logic in separate methods allows you to update a property's value by calling the corresponding method, when required. The **OrdersCount** is a simple calculated non-persistent property. This property is calculated using **XPO** criteria language. The **OrdersTotal** and **MaximumOrder** are complex calculated non-persistent properties, not expressed using the criteria language. So, traverse the **Orders** collection to calculate these properties.

> [!NOTE]
> In this topic, the **OrdersTotal** and **MaximumOrder** properties are considered to be complex to illustrate how such properties are calculated. Actually, their values can be easily calculated using **XPO** criteria language. For instance, you can use the **Avg**, **Count**, **Exists**, **Max** and **Min** functions to perform aggregate operations on collections. Refer to the [Criteria Language Syntax](xref:4928) topic for details.

The following snippet illustrates the **UpdateOrdersCount**, **UpdateOrdersTotal** and **UpdateMaximumOrder** methods definitions.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject {
    // ...
    public void UpdateOrdersCount(bool forceChangeEvents) {
        int? oldOrdersCount = fOrdersCount;
        fOrdersCount = Convert.ToInt32(Evaluate(CriteriaOperator.Parse("Orders.Count")));
        if (forceChangeEvents)
          OnChanged(nameof(OrdersCount), oldOrdersCount, fOrdersCount);
    }
    public void UpdateOrdersTotal(bool forceChangeEvents) {
        decimal? oldOrdersTotal = fOrdersTotal;
        decimal tempTotal = 0m;
        foreach (Order detail in Orders)
            tempTotal += detail.Total;
        fOrdersTotal = tempTotal;
        if (forceChangeEvents)
            OnChanged(nameof(OrdersTotal), oldOrdersTotal, fOrdersTotal);
    }
    public void UpdateMaximumOrder(bool forceChangeEvents) {
        decimal? oldMaximumOrder = fMaximumOrder;
        decimal tempMaximum = 0m;
        foreach (Order detail in Orders)
            if (detail.Total > tempMaximum)
                tempMaximum = detail.Total;
        fMaximumOrder = tempMaximum;
        if (forceChangeEvents)
            OnChanged(nameof(MaximumOrder), oldMaximumOrder, fMaximumOrder);
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
<DefaultClassOptions> _
Public Class Product
    Inherits BaseObject
    ' ...
    Public Sub UpdateOrdersCount(ByVal forceChangeEvents As Boolean)
        Dim oldOrdersCount As Nullable(Of Integer) = fOrdersCount
        fOrdersCount = Convert.ToInt32(Evaluate(CriteriaOperator.Parse("Orders.Count")))
        If forceChangeEvents Then
          OnChanged(NameOf(OrdersCount), oldOrdersCount, fOrdersCount)
        End If
    End Sub
    Public Sub UpdateOrdersTotal(ByVal forceChangeEvents As Boolean)
        Dim oldOrdersTotal As Nullable(Of Decimal) = fOrdersTotal
        Dim tempTotal As Decimal = 0D
        For Each detail As Order In Orders
            tempTotal += detail.Total
        Next detail
        fOrdersTotal = tempTotal
        If forceChangeEvents Then
            OnChanged(NameOf(OrdersTotal), oldOrdersTotal, fOrdersTotal)
        End If
    End Sub
    Public Sub UpdateMaximumOrder(ByVal forceChangeEvents As Boolean)
        Dim oldMaximumOrder As Nullable(Of Decimal) = fMaximumOrder
        Dim tempMaximum As Decimal = 0D
        For Each detail As Order In Orders
            If detail.Total > tempMaximum Then
                tempMaximum = detail.Total
            End If
        Next detail
        fMaximumOrder = tempMaximum
        If forceChangeEvents Then
            OnChanged(NameOf(MaximumOrder), oldMaximumOrder, fMaximumOrder)
        End If
    End Sub
End Class
```

***

Note that the **fOrdersCount** is evaluated on the client side using the objects loaded from an internal **XPO** cache in the **UpdateOrdersCount** method. You can use the following code to evaluate the **fOrdersCount** on the server side, so the uncommitted objects are not taken into account.

# [C#](#tab/tabid-csharp)

```csharp
fOrdersCount = Convert.ToInt32(Session.Evaluate<Product>(CriteriaOperator.Parse("Orders.Count"), 
    CriteriaOperator.Parse("Oid=?", Oid)));
```

# [VB.NET](#tab/tabid-vb)

```vb
fOrdersCount = Convert.ToInt32(Session.Evaluate(Of Product)( _
CriteriaOperator.Parse("Orders.Count"), CriteriaOperator.Parse("Oid=?", Oid)))
```

***

In the **Order** class' **Total** and **Product** property setters, a UI is updated when an **Order** object's property values change and an object is not currently being initialized:

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Order : BaseObject {
    // ...
    private decimal fTotal;
    public decimal Total {
        get { return fTotal; }
        set {
            bool modified = SetPropertyValue(nameof(Total), ref fTotal, value);
            if(!IsLoading && !IsSaving && Product != null && modified) {
                Product.UpdateOrdersTotal(true);
                Product.UpdateMaximumOrder(true);
            }
        }
    }
    private Product fProduct;
    [Association("Product-Orders")]
    public Product Product {
        get { return fProduct; }
        set {
            Product oldProduct = fProduct;
            bool modified = SetPropertyValue(nameof(Product), ref fProduct, value);
            if(!IsLoading && !IsSaving && oldProduct != fProduct && modified) {
                oldProduct = oldProduct ?? fProduct;
                oldProduct.UpdateOrdersCount(true);
                oldProduct.UpdateOrdersTotal(true);
                oldProduct.UpdateMaximumOrder(true);
            }
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
<DefaultClassOptions> _
Public Class Order
    Inherits BaseObject
    ' ...
    Private fTotal As Decimal
    Public Property Total() As Decimal
        Get
            Return fTotal
        End Get
        Set(ByVal value As Decimal)
            Dim modified As Boolean = SetPropertyValue(NameOf(Total), fTotal, value)
            If (Not IsLoading) AndAlso (Not IsSaving) AndAlso Product IsNot Nothing AndAlso modified Then
                Product.UpdateOrdersTotal(True)
                Product.UpdateMaximumOrder(True)
            End If
        End Set
    End Property
    Private fProduct As Product
    <Association("Product-Orders")> _
    Public Property Product() As Product
        Get
            Return fProduct
        End Get
        Set(ByVal value As Product)
            Dim oldProduct As Product = fProduct
            Dim modified As Boolean = SetPropertyValue(NameOf(Product), fProduct, value)
            If (Not IsLoading) AndAlso (Not IsSaving) AndAlso oldProduct IsNot fProduct AndAlso modified Then
                oldProduct = If((oldProduct <> Nothing), oldProduct, fProduct)
                oldProduct.UpdateOrdersCount(True)
                oldProduct.UpdateOrdersTotal(True)
                oldProduct.UpdateMaximumOrder(True)
            End If
        End Set
    End Property
End Class
```

***

In the **Product** class, the **OnLoaded** method is overridden, as it is necessary to reset cached values when using "lazy" calculations.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject {
    // ...
    protected override void OnLoaded() {
        Reset();
        base.OnLoaded();
    }
    private void Reset() {
        fOrdersCount = null;
        fOrdersTotal = null;
        fMaximumOrder = null;
    }
    // ...
```

# [VB.NET](#tab/tabid-vb)

```vb
<DefaultClassOptions> _
Public Class Product
    Inherits BaseObject
    ' ...
    Protected Overrides Sub OnLoaded()
        Reset()
        MyBase.OnLoaded()
    End Sub
    Private Sub Reset()
        fOrdersCount = Nothing
        fOrdersTotal = Nothing
        fMaximumOrder = Nothing
    End Sub
    ' ...
```

***