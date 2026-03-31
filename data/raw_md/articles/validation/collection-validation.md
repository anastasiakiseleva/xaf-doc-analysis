---
uid: "113217"
seealso:
- linkId: "113008"
- linkId: "113251"
title: Collection Validation
---
# Collection Validation

When defining a Validation Rule, you can use it to validate a collection property. This topic describes collection validation specifics. For general information on the contextual validation concept, refer to the [Validation Rules](xref:113008) topic.

## Collection Property Validation
Built-in validation rules can be applied to a collection property involved in a relationship (marked with the **Association** attribute). In this instance, a validation rule is evaluated for all the collection elements rather than for the master object, ensuring that each collection element is valid. So, when specifying parameters of a rule applied to a collection property, you need to specify them in the context of a collection element. For instance, the rule's [RuleBaseAttribute.TargetCriteria](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.TargetCriteria) should not contain references to the master object's properties and should only include properties of the collection element. Additionally, you will need to specify a collection element's property that must be checked via the **TargetPropertyName** named parameter. In the following code snippet, **RuleUniqueValue** is applied to the **Collection** property, to ensure that all the collection elements' **StringProperty** property values are unique:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using System.Collections.ObjectModel;
// ...

[DefaultClassOptions]
public class CollectionOwner : BaseObject {
    [RuleUniqueValue("RuleCollectionValidation", DefaultContexts.Save, 
        TargetPropertyName = nameof(CollectionElement.StringProperty))]
    public virtual IList<CollectionElement> Collection { get; set; } = new ObservableCollection<CollectionElement>();
}

public class CollectionElement : BaseObject {
    public virtual string StringProperty { get; set; }
    public virtual CollectionOwner Owner { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions]
public class CollectionOwner : BaseObject {

    public CollectionOwner(Session session) : base(session) { }

    [RuleUniqueValue("RuleCollectionValidation", DefaultContexts.Save, 
        TargetPropertyName = nameof(CollectionElement.StringProperty))]
    [Association("CollectionOwner-CollectionElements"), Aggregated]
    public XPCollection<CollectionElement> Collection {
        get { return GetCollection<CollectionElement>(nameof(Collection)); }
    }
}

public class CollectionElement : BaseObject {
    private CollectionOwner owner;
    private string stringProperty;

    public CollectionElement(Session session) : base(session) { }

    public string StringProperty {
        get { return stringProperty; }
        set { stringProperty = value; }
    }

    [Association("CollectionOwner-CollectionElements")]
    public CollectionOwner Owner {
        get { return owner; }
        set { owner = value; }
    }
}
```
***

## Aggregate Functions
When applied to collection properties, certain validation rules, such as the **RuleRange** and **RuleValueComparison** rules, can use aggregate functions. The attributes corresponding to these rules expose the **TargetCollectionAggregate** property that specifies the aggregate function. When a value is assigned to this property (by setting the corresponding named parameter or via the [Application Model](xref:112580)), the validation rule does not check the collection property's elements. Instead, it checks the specified aggregate function. For example, the following code snippet illustrates the **RuleValueComparison** rule applied to the **Collection** property. In this example, the rule ensures that the sum of the collection elements' **IntegerProperty** property values does not equal zero:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Data.Filtering;
using System.Collections.ObjectModel;
//...

[DefaultClassOptions]
public class AggregateFunction : BaseObject {
    [RuleValueComparison("RuleWithAggregateFunction", DefaultContexts.Save,
        ValueComparisonType.NotEquals, 0, TargetPropertyName = nameof(AggregateFunctionCollectionElement.IntegerProperty),
        TargetCollectionAggregate = Aggregate.Sum)]
    public virtual IList<AggregateFunctionCollectionElement> Collection { get; set; } = new ObservableCollection<AggregateFunctionCollectionElement>();
}

public class AggregateFunctionCollectionElement : BaseObject {
    public virtual int IntegerProperty { get; set; }
    public virtual AggregateFunction Owner { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.

```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Data.Filtering;

//...

[DefaultClassOptions]
public class AggregateFunction : BaseObject {

    public AggregateFunction(Session session) : base(session) { }
    
    [RuleValueComparison("RuleWithAggregateFunction", DefaultContexts.Save,
        ValueComparisonType.NotEquals, 0, TargetPropertyName = nameof(AggregateFunctionCollectionElement.IntegerProperty),
        TargetCollectionAggregate = Aggregate.Sum)]
    [Association("AggregateFunction-AggregateFunctionCollectionElements"), Aggregated]
    public XPCollection<AggregateFunctionCollectionElement> Collection {
        get { return GetCollection<AggregateFunctionCollectionElement>(nameof(Collection)); }
    }
}

public class AggregateFunctionCollectionElement : BaseObject {
    private AggregateFunction owner;
    private int integerProperty;

    public AggregateFunctionCollectionElement(Session session) : base(session) { }

    public int IntegerProperty {
        get { return integerProperty; }
        set { integerProperty = value; }
    }

    [Association("AggregateFunction-AggregateFunctionCollectionElements")]
    public AggregateFunction Owner {
        get { return owner; }
        set { owner = value; }
    }
}
```
***

If the [RuleBaseAttribute.TargetCriteria](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.TargetCriteria) property has been specified, then the demonstrated rule would calculate the sum over the suitable elements only.

The following aggregate functions are available:

| Aggregate Function | Description |
|---|---|
| **Avg** | Evaluates the average of the collection elements' property values. Requires the **TargetPropertyName** to be specified. |
| **Count** | Evaluates the number of elements contained in the collection. Does not require the **TargetPropertyName** to be specified. |
| **Exists** | Evaluates whether a collection element exists, which has a valid **TargetPropertyName** property's value (the validity is defined by the actual validation rule). |
| **Max** | Evaluates the maximum of the collection elements' property values. Requires the **TargetPropertyName** to be specified. |
| **Min** | Evaluates the minimum of the collection elements' property values. Requires the **TargetPropertyName** to be specified. |
| **Sum** | Evaluates the sum of the collection elements' property values. Requires the **TargetPropertyName** to be specified. |

> [!NOTE]
> [!include[RuleValueComparison_CollectionNote](~/templates/rulevaluecomparison_collectionnote111284.md)]

## Aggregate Function Values in Custom Message Templates
When customizing validation message templates, you can include the aggregate function value in the template. For this purpose, use the **{AggregatedTargetValue}** parameter. The following code snippet illustrates this:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Data.Filtering;
using System.Collections.ObjectModel;
//...

[DefaultClassOptions]
public class MessageTemplate : BaseObject {
    [RuleRange("RuleWithCustomMessageTemplate", DefaultContexts.Save, 0, 50,
        TargetPropertyName = nameof(MessageTemplateCollectionElement.DecimalProperty), TargetCollectionAggregate = Aggregate.Sum,
        CustomMessageTemplate = "The sum of the {TargetPropertyName} values must be " +
        "within {MinimumValue} and {MaximumValue} range. The current value is" +
        " {AggregatedTargetValue}")]
    public virtual IList<MessageTemplateCollectionElement> Collection { get; set; } = new ObservableCollection<MessageTemplateCollectionElement>();
}

public class MessageTemplateCollectionElement : BaseObject {
    public virtual decimal DecimalProperty { get; set; }
    public virtual MessageTemplate Owner { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Data.Filtering;

//...

[DefaultClassOptions]
public class MessageTemplate : BaseObject {

    public MessageTemplate(Session session) : base(session) { }

    [RuleRange("RuleWithCustomMessageTemplate", DefaultContexts.Save, 0, 50,
        TargetPropertyName = nameof(MessageTemplateCollectionElement.DecimalProperty), TargetCollectionAggregate = Aggregate.Sum,
        CustomMessageTemplate = "The sum of the {TargetPropertyName} values must be " +
        "within {MinimumValue} and {MaximumValue} range. The current value is" +
        " {AggregatedTargetValue}")]
    [Association("MessageTemplate-MessageTemplateCollectionElements"), Aggregated]
    public XPCollection<MessageTemplateCollectionElement> Collection {
        get { return GetCollection<MessageTemplateCollectionElement>(nameof(Collection)); }
    }
}

public class MessageTemplateCollectionElement : BaseObject {
    private decimal decimalProperty;
    private MessageTemplate owner;

    public MessageTemplateCollectionElement(Session session) : base(session) { }

    public decimal DecimalProperty {
        get { return decimalProperty; }
        set { decimalProperty = value; }
    }

    [Association("MessageTemplate-MessageTemplateCollectionElements")]
    public MessageTemplate Owner {
        get { return owner; }
        set { SetPropertyValue(nameof(Owner), ref owner, value); }
    }
}
```
***