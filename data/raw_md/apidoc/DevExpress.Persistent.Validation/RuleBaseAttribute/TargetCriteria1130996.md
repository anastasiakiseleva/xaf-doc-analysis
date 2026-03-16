---
uid: DevExpress.Persistent.Validation.RuleBaseAttribute.TargetCriteria
name: TargetCriteria
type: Property
summary: Specifies a criterion that must be satisfied by the validated object or property to check rules.
syntax:
  content: public string TargetCriteria { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that represents a criterion that must be satisfied to check validation rules.
seealso: []
---
When defining a rule for a business class or property, you should specify a context for checking this rule. In some scenarios, you may need to check whether a criterion is satisfied by the object or property before checking the rule. For instance, the **RuleRequiredField** rule can be checked for the **SpouseName** property, if the **IsMarried** property is set to **true**. The following code sample demonstrates how to define this rule.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
public class Contact : BaseObject {
    // ...
    [RuleRequiredField("SpouseNameIsRequiredWhenMarried", DefaultContexts.Save,
       SkipNullOrEmptyValues = false, TargetCriteria = "[IsMarried] == True")]
    public virtual String SpouseName { get; set; }
    public virtual bool IsMarried { get; set; }
    // ...
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.BaseImpl;
using DevExpress.Persistent.Validation;
using DevExpress.Xpo;

namespace valid5securxpo.Module.BusinessObjects;
public class Contact : BaseObject {
    // ...
    bool isMarried;
    string spouseName;
    [RuleRequiredField("SpouseNameIsRequiredWhenMarried", DefaultContexts.Save,
   SkipNullOrEmptyValues = false, TargetCriteria = "[IsMarried] == True")]
    [Size(SizeAttribute.DefaultStringMappingFieldSize)]
    public string SpouseName {
        get { return spouseName; }
        set {
            SetPropertyValue(nameof(SpouseName), ref spouseName, value);
        }
    }

    public bool IsMarried {
        get { return isMarried; }
        set {
            SetPropertyValue(nameof(IsMarried), ref isMarried, value);
        }
    }
    // ...
}
```

***

> [!NOTE]
> You can use [Function Criteria Operators](xref:113307) when passing a criteria as the **TargetCriteria** parameter. For details on how to write a criteria, refer to the [Ways to Build Criteria](xref:113052) topic.