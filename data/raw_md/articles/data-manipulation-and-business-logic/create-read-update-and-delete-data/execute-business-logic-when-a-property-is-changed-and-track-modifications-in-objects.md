---
uid: "403621"
title: Execute Business Logic When a Property is Changed
seealso:
  - linkId: "404195"
  - linkId: "113258"
  - linkId: "402990"
  - linkId: "112912"
---
# Execute Business Logic When a Property is Changed

## In a Controller

<!-- 
{|
|-
! Members !! Description
|-
| colspan="2"| **Methods**:
|-
| [IObjectSpace.SetModified](xref:DevExpress.ExpressApp.IObjectSpace.SetModified*) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.SetModified*)]
|-
| colspan="2"| **Properties**:
|-
| [IObjectSpace.ModifiedObjects](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedObjects) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.ModifiedObjects)]
|-
| [IObjectSpace.IsModified](xref:DevExpress.ExpressApp.IObjectSpace.IsModified) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.IsModified)]
|-
| colspan="2"| **Events**:
|-
| [IObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.IObjectSpace.ObjectChanged) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.ObjectChanged)]
|-
| [IObjectSpace.ModifiedChanged](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedChanged) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.ModifiedChanged)]
|} -->

### Update a Calculated Property When Another Property is Changed

To execute your business logic when a business class property is changed, execute it in the [IObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.IObjectSpace.ObjectChanged) event handler. 


[!include[](~/templates/objectchanged_code_snippet.md)]


### Mark a View as Modified

Your business logic can indirectly change a current View object. For example, you can modify a collection property of a business class in code. This won't enable the Save Action in the business class' Detail View to commit changes. Call the [IObjectSpace.SetModified](xref:DevExpress.ExpressApp.IObjectSpace.SetModified*) method and pass the current View object as a parameter.

[!include[](~/templates/setmodified_code_snippet.md)]


### Loop Through Modified Objects

It's possible to traverse through all modified objects in an Object Space to process them in a custom way. The [IObjectSpace.ModifiedObjects](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedObjects) property returns a collection of modified objects.

[!include[<32-33><40-41>](~/templates/os_committing_committed_customcommitchanges_reloaded.md)]

### Track When a View is Changed

If your business logic should be executed after a user starts changing an object or after a user saves changes, handle the [IObjectSpace.ModifiedChanged](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedChanged) event to catch these moments. For example, you can disable an Action if a user changes an object.

[!include[](~/templates/modifiedchanged_code_snippet.md)]

## In a Data Model

A common task in business objects is to create a calculated property which value depends on another persistent property. For example, you have the **Customer** and **Order** business classes that have a one-to-many relationship between them. The **Order** business class implements the **Price** property. In the **Customer** business class, add a calculated property (**Total**) that returns the total price of all customer's orders.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using System.Linq;
using System.Collections.ObjectModel;
using System.ComponentModel.DataAnnotations;
using DevExpress.Persistent.BaseImpl.EF;

namespace MySolution.Module.BusinessObjects {
    public class Customer : BaseObject {
        public decimal Total {
            get {
                return Orders.Sum(c => c.Price);
            }
        }

        public virtual IList<Order> Orders { get; set; } = new ObservableCollection<Order>();
    }

    public class Order : BaseObject { 
        public virtual decimal Price { get; set; }
        public virtual Customer Customer { get; set; }
    }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using System.Linq;

namespace MySolution.Module.BusinessObjects {
    public class Customer : BaseObject {
        public Customer(Session session) : base(session) { }

        public decimal Total {
            get {
                return Orders.Sum(c => c.Price);
            }
        }

        [Association]
        public XPCollection<Order> Orders {
            get {
                return GetCollection<Order>(nameof(Orders));
            }
        }
    }

    public class Order : BaseObject { 
        public Order(Session session) : base(session) { }

        decimal price;
        Customer fCustomer;
        
        public decimal Price {
            get => price;
            set => SetPropertyValue(nameof(Price), ref price, value);
        }

        [Association]
        public Customer Customer {
            get => fCustomer;
            set => SetPropertyValue(nameof(Customer), ref fCustomer, value);
        }
    }
}
```

# [VB.NET (XPO)](#tab/tabid-vb-xpo)

```vb
Imports System.Linq
Imports DevExpress.Persistent.BaseImpl
Imports DevExpress.Xpo

Public Class Customer
    Inherits BaseObject
    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub

    ReadOnly Property Total As Decimal
        Get
            Return Orders.Sum(Function(c) c.Price)
        End Get
    End Property

    <Association>
    Public ReadOnly Property Orders() As XPCollection(Of Order)
        Get
            Return GetCollection(Of Order)(NameOf(Orders))
        End Get
    End Property
End Class

Public Class Order
    Inherits BaseObject
    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub

    Private _customer As Customer
    Private _price As Decimal

    Property Price As Decimal
        Get
            Return _price
        End Get
        Set(ByVal Value As Decimal)
            SetPropertyValue(NameOf(Price), _price, Value)
        End Set
    End Property

    <Association>
    Property Customer() As Customer
        Get
            Return _customer
        End Get
        Set(ByVal Value As Customer)
            SetPropertyValue(NameOf(Customer), _customer, Value)
        End Set
    End Property

End Class
```

***

This code calculates the **Total** property value when a **Customer** object is loaded. To notify bound editors that the **Total** property value changed, subscribe to changes of the **Orders** collection and send notifications about the **Total** property value changes when they occur:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using System.ComponentModel.DataAnnotations;
using System.Collections.ObjectModel;
// ...
public class Customer : BaseObject, INotifyPropertyChanged {
    // ...
    ObservableCollection<Order> orders;
    public virtual IList<Order> Orders { get => orders; }

    public Customer() {
        orders = new ObservableCollection<Order>();
        orders.CollectionChanged += (s, e) => OnPropertyChanged(nameof(Total));
    }

    #region INotifyPropertyChanged implementation

    PropertyChangedEventHandler propertyChanged;
    event PropertyChangedEventHandler INotifyPropertyChanged.PropertyChanged {
        add { propertyChanged += value; }
        remove { propertyChanged -= value; }
    }
    protected void OnPropertyChanged([CallerMemberName] string propertyName = null) {
        propertyChanged.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }

    #endregion
    string customerName;
    public virtual string CustomerName {
        get { return customerName; }
        set {
            customerName = value;
            OnPropertyChanged();
        }
    }    
}

//Note that the Customer class implements the INotifyPropertyChanged interface explicitly. You need to send notifications about changes to all class properties explicitly - UseChangeTrackingProxies does not work in this case.

```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Xpo.Metadata;
// ...
public class Customer : BaseObject {
    // ...
    protected override XPCollection<T> CreateCollection<T>(XPMemberInfo property) {
        XPCollection<T> collection = base.CreateCollection<T>(property);
        if (property.Name == nameof(Orders)) {
            collection.CollectionChanged += Collection_CollectionChanged;
        }
        return collection;
    }

    private void Collection_CollectionChanged(object sender, XPCollectionChangedEventArgs e) {
        OnChanged(nameof(Total));
    }
}
```

# [VB.NET (XPO)](#tab/tabid-vb-xpo)

```vb
Imports DevExpress.Xpo.Metadata
' ...
Public Class Customer
    Inherits BaseObject
    ' ...

    Protected Overrides Function CreateCollection(Of T)([property] As XPMemberInfo) As XPCollection(Of T)
        Dim collection = MyBase.CreateCollection(Of T)([property])
        If [property].Name = NameOf(Orders) Then
            AddHandler collection.CollectionChanged, AddressOf Collection_CollectionChanged
        End If
        Return collection
    End Function
    Private Sub Collection_CollectionChanged(ByVal sender As Object, ByVal e As XPCollectionChangedEventArgs)
        OnChanged(NameOf(Total))
    End Sub
End Class
```

***

You can also notify that the `Total` property value is changed from the `Order` business class. Refer to the following article that describes this: [How to: Calculate a Property Value Based on Values from a Detail Collection](xref:113179).
