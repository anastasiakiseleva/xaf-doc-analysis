---
uid: "113285"
seealso:
- linkId: "113679"
- linkId: "112611"
- linkId: DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute
title: List View Column Generation
---
# List View Column Generation

XAF automatically generates all List Views according to the [Application Model](xref:112580)'s information. This topic describes the specific rules used to generate a default set of List View columns.


> [!NOTE]
> The column generation logic is declared in the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelListViewColumnsNodesGenerator) class, which is the Node Generator (see [Extend and Customize the Application Model in Code](xref:112810)).

## Simple Property Columns Generation
In this section, simple property columns are generated for the following persistent class:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
public class ObjectA : BaseObject {
    public virtual string PropertyA1 { get; set; }
    public virtual string PropertyA2 { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
public class ObjectA : BaseObject {
    public ObjectA(Session session) : base(session) { }
    private string propertyA1;
    private string propertyA2;
    public string PropertyA1 {
        get { return propertyA1; }
        set { SetPropertyValue(nameof(PropertyA1), ref propertyA1, value); }
     }
    public string PropertyA2 {
        get { return propertyA2; }
        set { SetPropertyValue(nameof(PropertyA2), ref propertyA2, value); }
    }
}
```
***

The **ListView**'s and **LookupListView**'s **Columns** node contains child nodes generated for this class. The following image illustrates this node in the Model Editor:

![ListViewColumns_1](~/images/listviewcolumns_1116685.png)

The column order specified using the [IModelNode.Index](xref:DevExpress.ExpressApp.Model.IModelNode.Index) properties corresponds to their declaration order. These columns are visible when their `Index` values are positive or zero.

The following attributes, applied in code, affect column visibility:

### XafDefaultProperty, DefaultProperty, and FriendlyKeyProperty Attributes
	
If the class has a [default](xref:113525) or friendly key property (see @DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute, [DefaultPropertyAttribute](xref:System.ComponentModel.DefaultPropertyAttribute), and [](xref:DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute)), its Lookup List View contains a single column corresponding to this property. In the general List View, the default property column has an index of zero and is displayed first. The code below demonstrates the `DefaultProperty` attribute in use, and the image illustrates the result.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultProperty(nameof(PropertyA2))]
public class ObjectA : BaseObject {
    // ...
```
***

![ListViewColumns_2](~/images/listviewcolumns_2116686.png)

The `FriendlyKeyProperty` attribute has the same effect.

If the business class property name matches or contains one of the `DevExpress.ExpressApp.DC.TypeInfo.DefaultPropertyNames` values (excluding inherited properties), then it is considered as the default property. The `DefaultPropertyNames` values: Name, Title, Subject, Caption, Description, Benennung, Nombre, Nome. If you want to modify the `DefaultPropertyNames` collection, refer to the following help topic: [Declare a Property with a Specific Name](xref:113525#declare-a-property-with-a-specific-name).

# [C#](#tab/tabid-csharp)

```csharp
public class ObjectA : BaseObject {
    // ...
    public string ObjectName {
        // ...
```
***

![ListViewColumns_3](~/images/listviewcolumns_3116687.png)

The `DefaultProperty` attribute overrides this behavior.

### HideInUI Attribute

The corresponding column is not generated if the property is decorated with `HideInUI.All`, `HideInUI.ListView` or `HideInUI.ListViewColumn`. If it is decorated specifically with `HideInUI.ListViewColumn`, you can then use the **Object Model** dialog to generate the column back (see [](xref:113679)) (available only in Win and Blazor).

### Browsable Attribute
	
The corresponding column is not generated if the property is decorated with the `Browsable` attribute and `false` is passed as the parameter (see [BrowsableAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.browsableattribute)).
### VisibleInListView Attribute
	
The corresponding column is generated but remains invisible if the property is decorated with the [](xref:DevExpress.Persistent.Base.VisibleInListViewAttribute) attribute and `false` is passed as the parameter. The **Columns** node's [IModelNode.Index](xref:DevExpress.ExpressApp.Model.IModelNode.Index) property is set to -1. You can use the Column Chooser or Model Editor to unhide such a column (see [](xref:113679)).
### VisibleInLookupListView Attribute
	
When a class has a default property, XAF generates one column for this property in the Lookup List View. To add a column in code, decorate the required property with the [](xref:DevExpress.Persistent.Base.VisibleInLookupListViewAttribute) and pass `true` as the attribute parameter. 
When the class has no default property, all property columns are generated in the Lookup List View. To hide a column corresponding to a certain property, decorate the property with the `VisibleInLookupListViewAttribute`, and pass `false` as the attribute parameter.

## Reference Property Columns Generation
To demonstrate how the reference property columns are generated, the persistent class demonstrated in the previous section, will be extended with the `PropertyA3` reference property of the `ObjectB` type

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
public class ObjectA : BaseObject {
    public virtual ObjectB PropertyA3 { get; set; }
}

[DefaultProperty(nameof(PropertyB2))]
public class ObjectB : BaseObject {
    public virtual string PropertyB1 { get; set; }
    public virtual string PropertyB2 { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
public class ObjectA : BaseObject {
    // ...
    private ObjectB propertyA3;
    public ObjectB PropertyA3 {
        get { return propertyA3; }
        set { SetPropertyValue(nameof(propertyA3), ref propertyA3, value); }
    }
}
[DefaultProperty(nameof(PropertyB2))]
public class ObjectB : BaseObject {
    public ObjectB(Session session) : base(session) { }
    private string propertyB1;
    public string PropertyB1 {
        get { return propertyB1; }
        set { SetPropertyValue(nameof(propertyB1), ref propertyB1, value); }
    }
    private string propertyB2;
    public string PropertyB2 {
        get { return propertyB2; }
        set { SetPropertyValue(nameof(propertyB2), ref propertyB2, value); }
    }
}
```
***

A column is generated to display the `PropertyA3` property.

![ListViewColumns_4](~/images/listviewcolumns_4116688.png)

In the UI, the `PropertyA3` displays the `PropertyB2`'s value, because  the `PropertyB2` is the `ObjectB` class' default property.

If the `PropertyA3` property is decorated by the [](xref:DevExpress.Persistent.Base.ExpandObjectMembersAttribute) with the  [ExpandObjectMembers.InListView](xref:DevExpress.Persistent.Base.ExpandObjectMembers.InListView) parameter, then the columns for all `ObjectB` class' properties are generated in the `ObjectA` List View. 

# [C#](#tab/tabid-csharp)

```csharp
public class ObjectA : BaseObject {
    // ...
    [ExpandObjectMembers(ExpandObjectMembers.InListView)]
    public ObjectB PropertyA3 {
        // ...
```
***

![ListViewColumns_5](~/images/listviewcolumns_5116689.png)

## Columns, Generated in Inherited Class' List Views
Consider the following `ObjectC` class, derived from the `ObjectA` class:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
public class ObjectC : ObjectA {
    public virtual string PropertyC1 { get; set; }
    public virtual string PropertyC2 { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
public class ObjectC : ObjectA {
    public ObjectC(Session session) : base(session) { }
    private string propertyC1;
    public string PropertyC1 {
         get { return propertyC1; }
        set { SetPropertyValue(nameof(propertyC1), ref propertyC1, value); }
    }
    private string propertyC2;
    public string PropertyC2 {
        get { return propertyC2; }
        set { SetPropertyValue(nameof(propertyC2), ref propertyC2, value); }
    }
}
```
***

Typically, the columns for this class properties are generated as usual (see the description of `ObjectA` List Views column generation above). The columns for derived properties are generated as hidden (with -1 indexes). Note the following specifics:

* **The intended behavior when the derived class has no default property, and its ancestor has a default property**
	
	The ancestor class's default property is used as the default in a derived class' List View. In the general List View, this property's column gets the zero index and is shown first. In the Lookup List View, the default property ancestor class column is the only generated column. The following image illustrates the generated columns when the `PropertyA2` is the `ObjectA` class' default property:
	
	![ListViewColumns_6](~/images/listviewcolumns_6116690.png)
* **The intended behavior, when the derived class has no public fields and properties**
	
	In this case, columns generated for the derived class are the same as the ancestor class' columns, and they all are visible by default. The ancestor class's default property is used as the default in a derived class' List View.

## Default Columns Width
Each column has an [IModelColumn.Width](xref:DevExpress.ExpressApp.Model.IModelColumn.Width) property that specifies its width in ASP.NET Core Blazor and Windows Forms application. The following table shows the default width values:

| Type of Property | Default Width | Default Width in Lookups |
|---|---|---|
| The property is the class' default or friendly key property (see [DefaultPropertyAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.defaultpropertyattribute), [](xref:DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute)). If a property contains "Name" in its name (excluding inherited properties), this property is also considered default. | 400 | 340 |
| A short value type property - `int`, `float`, `double`, `decimal`, `char` or `bool`. | 50 | 50 |
| Other properties (`string` and so on) | 70 | 50 |

> [!NOTE]
> 
> In ASP.NET Core Blazor applications, the default column width is ignored. 

Usually the default property contains the most details in the class, so a wide column is automatically generated for it. Short type values do not take much screen space, and their default columns are narrow.

## Columns Sorting Order
List Views are sorted by the default property values in ascending order (if the default property type is `System.IComparable`). The default column's [IModelColumn.SortIndex](xref:DevExpress.ExpressApp.Model.IModelColumn.SortIndex) is set to 0, and [IModelColumn.SortOrder](xref:DevExpress.ExpressApp.Model.IModelColumn.SortOrder) is set to `ColumnSortOrder.Ascending`. Other columns have the default `SortIndex` and `SortOrder` (-1 and `ColumnSortOrder.None`, respectively) values.
