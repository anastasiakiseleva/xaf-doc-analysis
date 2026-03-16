---
uid: "405280"
title: Calculate a Property Value Based on Values from a Detail Collection in EF Core
owner: Eugeniy Burmistrov
seealso:
  - linkId: "4928"
  - linkId: DevExpress.ExpressApp.DC.PersistentAliasAttribute
  - linkId: '113583'
---

# Calculate a Property Value Based on Values from a Detail Collection in EF Core

This topic describes how to implement a business class, so that one of its properties is calculated based on a property (or properties) of the objects contained in the child object collection.

![CalculatePropertyBasedOnDetailCollection ](~/images/calculatepropertybasedondetailcollection116394.png)

> [!Tip]
> [!include[CodeCentralObjectE305](~/templates/CodeCentralExampleNote.md)] [https://supportcenter.devexpress.com/ticket/details/e305/xaf-how-to-calculate-a-master-property-based-on-values-from-a-detail-collection](https://supportcenter.devexpress.com/ticket/details/e305/xaf-how-to-calculate-a-master-property-based-on-values-from-a-detail-collection).

## Initial Class Implementation

A `Product` class has a collection of `Order` objects. The `Product` and `Order` classes are associated by the [One-to-Many](xref:112654) relationship, which means that a `Product` object may be associated with several `Order` objects. The collection of `Order` objects is aggregated. `Order` objects are created, belonging to one of the `Product` objects. When the master object is removed, all objects in its aggregated collection are removed as well.

The following code snippet illustrates the `Product` class implementation:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...
[DefaultClassOptions]
    public class Product : BaseObject {
    public virtual string Name { get; set; }
    public virtual IList<Order> Orders { get; set; } = new ObservableCollection<Order>();
}
```

***

The following code snippet illustrates the `Order` class implementation:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...
[DefaultClassOptions]
    public class Order : BaseObject {
    public virtual string Description { get; set; }
    public virtual decimal Total { get; set; }
    public virtual Product Product { get; set; }
}
```

***

In the code above, the `Order` class contains the `Total` property and the `Product` class has the `MaximumOrder` and `OrdersTotal` properties. These `Product`'s properties are calculated based on `Total` properties of the aggregated `Orders`. The `OrderCount` property is also added to the `Product` class. This property exposes the number of aggregated `Orders`.

## Implement Non-Persistent Calculated Properties

Use one of the following techniques to implement "lazy" calculated properties that are calculated on demand:

### Calculate Property Values in Code

Omit the property setter to implement a non-persistent property. The following code snippet demonstrates the implementation of three calculated properties: `OrdersCount`, `OrdersTotal`, and `MaximumOrder`.

>[!NOTE]
>
> The calculated property implementation technique demonstrated in this section allows property values to be calculated based on complex business logic that cannot be expressed with the Criteria Operator syntax. In cases when the Criteria Operator syntax is sufficient to calculate the property values, use the technique described in the [Use Criteria Operator Syntax to Calculate Property Values](#use-criteria-operator-syntax-to-calculate-property-values) section.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject {
    // ...
    private int? fOrdersCount = null;
    public int? OrdersCount {
        get {
            return fOrdersCount;
        }
    }
    private decimal? fOrdersTotal = null;
        public decimal? OrdersTotal {
        get {
            return fOrdersTotal;
        }
    }
    private decimal? fMaximumOrder = null;
    public decimal? MaximumOrder {
        get {
        return fMaximumOrder;
        }
    }
}
```
***

Implement an `UpdateCalculatedProperties` method that recalculates the `OrdersCount`, `OrdersTotal`, and `MaximumOrder` calculated properties' values. The method's implementation must contain business logic used to calculate the values of these properties. Call `UpdateCalculatedProperties` from the @DevExpress.Persistent.BaseImpl.EF.BaseObject.OnCreated and @DevExpress.Persistent.BaseImpl.EF.BaseObject.OnLoaded method implementations. 

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject {
    // ...
    public void UpdateCalculatedProperties() {
        decimal tempMaximum = 0m;
        decimal tempTotal = 0m;
        foreach (Order detail in Orders) {
            if (detail.Total > tempMaximum) {
                tempMaximum = detail.Total;
            }
            tempTotal += detail.Total;
        }
        fMaximumOrder = tempMaximum;
        fOrdersTotal = tempTotal;
        fOrdersCount = Orders.Count;
    }
    public override void OnCreated() {
        base.OnCreated();
        UpdateCalculatedProperties();
    }
    public override void OnLoaded() {
        base.OnLoaded();
        UpdateCalculatedProperties();
    }
}

```
***

### Use Criteria Operator Syntax to Calculate Property Values

This technique is optimal when property value calculation logic can be expressed with Criteria Operator syntax. With this technique the calculated property value can be used for data shaping operations (filtering, sorting, grouping, and so on) in server-based [data access modes](xref:113683).

To use Criteria Syntax, decorate properties with the @DevExpress.ExpressApp.DC.PersistentAliasAttribute with a Criteria Syntax expression as a parameter. To calculate the property value based on the specified expression, call the [BaseObject.EvaluateAlias](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject.EvaluateAlias``1(System.String)) method from the property getter.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject, INotifyPropertyChanged {
    // ...
    [PersistentAlias("[Orders].Count()")]
    public int OrdersCount {
        get {
            return EvaluateAlias<int>();
        }
    }
    [PersistentAlias("[Orders].Sum(Total)")]
    public decimal OrdersTotal {
        get {
            return EvaluateAlias<decimal>();
        }
    }
    [PersistentAlias("[Orders].Max(Total)")]
    public decimal MaximumOrder {
        get {
            return EvaluateAlias<decimal>()
        }
    }
}
```
***

>[!TIP]
>
> To immediately update a calculated property's value displayed in the UI as a user changes property editor values, decorate properties used in the expression with the @DevExpress.Persistent.Base.ImmediatePostDataAttribute.

Add an `UpdateCalculatedProperties` method and call it from the @DevExpress.Persistent.BaseImpl.EF.BaseObject.OnCreated and @DevExpress.Persistent.BaseImpl.EF.BaseObject.OnLoaded method implementations. On the next step, you will use this method to update the UI when the `Orders` collection changes.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject {
    // ...
    public void UpdateCalculatedProperties() {

    }
    public override void OnCreated() {
        base.OnCreated();
        UpdateCalculatedProperties();
    }
    public override void OnLoaded() {
        base.OnLoaded();
        UpdateCalculatedProperties();
    }
}

```
***

## Update UI When Calculated Property Values Change

To automatically recalculate the calculated property values when items are added to or removed from the `Orders` collection as well as when `Product` objects are loaded, handle the `Orders` collection's `CollectionChanged` event. In the event handler, call the `UpdateCalculatedProperties` method implemented in the previous step.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject {
    // ...
    public override void OnCreated() {
        base.OnCreated();
        UpdateCalculatedProperties();
        ((ObservableCollection<Order>)this.Orders).CollectionChanged += Product_CollectionChanged;
    }
    public override void OnLoaded() {
        base.OnLoaded();
        UpdateCalculatedProperties();
        ((ObservableCollection<Order>)this.Orders).CollectionChanged += Product_CollectionChanged;
    }
    private void Product_CollectionChanged(object sender, System.Collections.Specialized.NotifyCollectionChangedEventArgs e) {
        UpdateCalculatedProperties();
    }
}

```
***

For the user interface to reflect the changes in the calculated property values, explicitly generate a notification through the [INotifyPropertyChanged](xref:System.ComponentModel.INotifyPropertyChanged) interface. To do this, implement the `INotifyPropertyChanged` interface and modify the `Product` class as shown below:

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Product : BaseObject, INotifyPropertyChanged {
    // ...
    private string name;
    public virtual string Name {
        get { return name; }
        set {
            if (name != value) {
                name = value;
                RaisePropertyChanged(nameof(Name));
            }
        }
    }
    // ...
    public event PropertyChangedEventHandler PropertyChanged;
    public void RaisePropertyChanged(string name) {
        if(PropertyChanged != null) {
            PropertyChanged(this, new PropertyChangedEventArgs(name));
        }
    }
    public void UpdateCalculatedProperties() {
        // ...
        RaisePropertyChanged(nameof(OrdersCount));
        RaisePropertyChanged(nameof(OrdersTotal));
        RaisePropertyChanged(nameof(MaximumOrder));
    }
}
```
***


To automatically recalculate calculated property values when items in the `Orders` collection are modified, handle the `Order` class's `PropertyChanged` event. In the event handler, call the `Product.UpdateCalculatedProperties` method.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Order : BaseObject {
    // ...
    private void Order_PropertyChanged(object sender, PropertyChangedEventArgs e) {
        Product?.UpdateCalculatedProperties();
    }
    public override void OnLoaded() {
        base.OnLoaded();
        ((INotifyPropertyChanged)this).PropertyChanged += Order_PropertyChanged;
    }
    public override void OnCreated() {
        base.OnCreated();
        ((INotifyPropertyChanged)this).PropertyChanged += Order_PropertyChanged;
    }
}
```
***

