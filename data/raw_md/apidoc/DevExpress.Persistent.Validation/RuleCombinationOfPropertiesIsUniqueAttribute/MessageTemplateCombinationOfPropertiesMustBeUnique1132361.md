---
uid: DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute.MessageTemplateCombinationOfPropertiesMustBeUnique
name: MessageTemplateCombinationOfPropertiesMustBeUnique
type: Property
summary: Specifies the text to be written in the Validation Error window when the current rule is broken.
syntax:
  content: public string MessageTemplateCombinationOfPropertiesMustBeUnique { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value representing the text to be written to the Validation Error window when a rule is broken.
seealso: []
---
When defining a **RuleCombinationOfPropertiesIsUnique** rule via the [](xref:DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute) in code or in the [Model Editor](xref:112582), you can specify a custom definition to be displayed in the Vaidation Error window for the broken rule. To do this, set the **CustomMessageTemplate** property. However, the list of the found objects will not be displayed. To display them, specify the **MessageTemplateCombinationOfPropertiesMustBeUnique** property instead of the **CustomMessageTemplate** property. The following code demonstrates this:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.Persistent.Validation;
using System;
using System.Linq;

[RuleCombinationOfPropertiesIsUnique("SampleRule",
    DefaultContexts.Save, "Description, Company",
    MessageTemplateCombinationOfPropertiesMustBeUnique =
    "Objects with the same combinations of the " +
    "'Description' and 'Company' properties must not exist.")]
public class SampleClass : BaseObject {
    //...
    public virtual string Company { get; set; }
    public virtual string Description { get; set; }
    //...
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Persistent.Validation;
using DevExpress.Xpo;

namespace valid5securxpo.Module.BusinessObjects;
[DefaultClassOptions]
[RuleCombinationOfPropertiesIsUnique("SampleRule",
    DefaultContexts.Save, "Description, Company",
    MessageTemplateCombinationOfPropertiesMustBeUnique =
    "Objects with the same combinations of the " +
    "'Description' and 'Company' properties must not exist.")]
public class SampleClass: BaseObject {
  public SampleClass(Session session) : base(session) {    }
    string company;
    string description;
    [Size(SizeAttribute.DefaultStringMappingFieldSize)]
    public string Description {
        get {
            return description;
        }
        set {
            SetPropertyValue(nameof(Description), ref description, value);
        }
    }
    
    [Size(SizeAttribute.DefaultStringMappingFieldSize)]
    public string Company {
        get {
            return company;
        }
        set {
            SetPropertyValue(nameof(Company), ref company, value);
        }
    }
}

```

***

To customize the format that is used to list the found objects in the Validation Error window, use the [RuleCombinationOfPropertiesIsUniqueAttribute.FoundObjectMessageFormat](xref:DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute.FoundObjectMessageFormat) and [RuleCombinationOfPropertiesIsUniqueAttribute.FoundObjectMessagesSeparator](xref:DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute.FoundObjectMessagesSeparator) properties.

There is a set of format items you can use in message templates. For instance, when using the {TargetObject} format item, the validated object will be inserted at runtime. For details, refer to the [RuleBaseAttribute.CustomMessageTemplate](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.CustomMessageTemplate) property description.