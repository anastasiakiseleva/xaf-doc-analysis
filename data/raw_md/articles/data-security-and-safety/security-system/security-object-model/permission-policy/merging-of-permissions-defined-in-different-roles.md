---
uid: "400290"
seealso: []
title: Merging of Permissions Defined in Different Roles
---
# Merging of Permissions Defined in Different Roles

You can configure a role's permissions and assign it to a user. This topic describes how the [Security System](xref:113366) processes permissions when a user has several roles.

## General Information

One role's permissions do not affect the permissions of another role. When the user has several roles, the Security System consistently checks permissions of each role. The Security System merges these checks' results depending on the [SecurityStrategy.RolesMergingMode](xref:DevExpress.ExpressApp.Security.SecurityStrategy.RolesMergingMode) property value. The following table lists the available modes:

| RolesMergingMode | Description |
|---|---|
| **Granted&#65279;In&#65279;Any&#65279;Role** | A user can execute an operation when at least one of the user's roles allows this operation. This is the default mode. |
| **Granted&#65279;In&#65279;All&#65279;Roles** | A user can execute an operation when all roles assigned to the user allows this operation. |

For example, your application includes the **Customer** and **Order** business objects. A user has the **CustomersManager** and **OrdersManager** roles with the **DenyAllByDefault** [Permission Policy](xref:116172). Role **CustomerManager** has a permission that allows reading the **Customer** objects. Role **OrdersManager** has a permission that allows reading the **Order** objects. The Security System processes these permissions according to the **RolesMergingMode** property value: 

* The **GrantedInAnyRole** mode 

  The user can read both types. Remove the _read_ permissions for **Customer** type in the **CustomersManager** role to deny reading this type's objects.

* The **GrantedInAllRoles** mode 

  The user can not read both types. Add the _read_ permission for the **Customer** type in the **OrdersManager** role to allow reading this type's objects.

## Permission Merging for Associations

This section describes how the Security System merges permissions for associated objects when a user has several assigned roles.

> [!Note]
> Security System grants rights for associated properties in each role independently. To allow an associated property, you should set allow permissions for [both sides of an association](xref:116170) within one role.

For example, the **Order** and **Customer** business objects have a [one-to-many relationship](xref:112654#one-to-many-non-aggregated). The **Customer** object implements the **Orders** collection property and the **Order** object implements the **Customer** reference property.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
public class Customer : BaseObject {
    public virtual IList<Order> Orders { get; set; } = new ObservableCollection<Order>();
}

public class Order : BaseObject {
    public virtual Customer Customer { get; set; }

}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)
	
```csharp
public class Customer : BaseObject {
    // ...
    [Association]
    public XPCollection<Order> Orders { 
        get { return GetCollection<Order>(nameof(Orders)); }
    }
}

public class Order : BaseObject {
    // ...
    [Association]
    public Customer Customer {
        get { return fCustomer; }
        set { SetPropertyValue(nameof(Customer), ref fCustomer, value); }
    }
    Customer fCustomer;

}
```
***

A user has the 'A' and 'B' roles and the [SecurityStrategy.RolesMergingMode](xref:DevExpress.ExpressApp.Security.SecurityStrategy.RolesMergingMode) property is set to **GrantedInAnyRole**. To allow accessing the **Order.Customer** property and deny the **Customer.Orders** collection, follow the steps below:

1. Give the role 'A' a permission that allows a user to read/write the **Order.Customer** property.
2. Give the role 'B' a permission that denies a user to read/write the **Customer.Orders** collection. 

The user can read/write the "Orders-Customer" association because the role 'A' allows these operations according to the rules described in the [Permissions for Associated Objects](xref:116170) article. Note that the role 'B' denies the association but the [Security System](xref:113366) does not take it into account when the **RolesMergingMode** property is set to **GrantedInAnyRole**.

If you give permissions that allow the user to read/write the **Order.Customer** property and deny the **Customer.Orders** collection in one role, the user cannot read/write the "Orders-Customer" association because the association is denied on the **Customer** side.

## Permissions Merging for Reference Properties

This section describes how the Security System merges permissions for reference properties when a user has several assigned roles.

> [!Note]
> You should set [the reference property and referenced type](xref:116170#permissions-for-reference-objects) within one role.

For example, the **Order** business object has the **Customer** type **Customer** reference property. 

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
public class Order : BaseObject {
    // ...
    public virtual Customer Customer { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)
	
```csharp
public class Order : BaseObject {
    // ...   
    public Customer Customer {
        get { return fCustomer; }
        set { SetPropertyValue(nameof(Customer), ref fCustomer, value); }
    }
    Customer fCustomer;

}
```
***

The user cannot read the **Order.Customer** property when:
* the role 'A' has a permission that allows the user to read the **Order.Customer** property
* the role 'B' has a permission that allows the user to read the **Customer** type

These permissions are in different roles and do not affect each other. Add the _read_ permission for the **Order.Customer** property and **Customer** type within one role to allow the user to read this property.