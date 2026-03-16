---
uid: DevExpress.ExpressApp.Validation.ValidationModule.EnableRuntimeRuleCache
name: EnableRuntimeRuleCache
type: Property
summary: Specifies if the Validation Module caches Rules from custom persistent Rule Sources.
syntax:
  content: |-
    [DefaultValue(false)]
    public bool EnableRuntimeRuleCache { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the Validation Module caches Rules from custom persistent Rule Sources; otherwise, **false**.'
seealso:
- linkId: DevExpress.Persistent.Validation.IRuleSource
---
Built-in Rule Sources query the database each time before validation occurs. You can cache Rules to avoid unnecessary queries. The following code demonstrates how to enable Rule caching for all custom persistent Rule Sources in the platform-agnostic Module:

**File**: _MySolution.Module\Module.cs_.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Validation;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    //...
    public override void Setup(ApplicationModulesManager moduleManager) {
        base.Setup(moduleManager);
        //...
        ValidationModule _validationModule = moduleManager.Modules.FindModule<ValidationModule>();
        _validationModule.EnableRuntimeRuleCache = true;
    }
}
```

***

To enable or disable caching for a specific persistent Rule Source, subscribe to the @DevExpress.ExpressApp.Validation.ValidationModule.CustomizeApplicationRuntimeRules event and specify the `EnableRuleCache` property:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Validation;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    //...
    public override void Setup(ApplicationModulesManager moduleManager) {
        base.Setup(moduleManager);
        //...
        ValidationModule _validationModule = moduleManager.Modules.FindModule<ValidationModule>();
        _validationModule.EnableRuntimeRuleCache = true;
        _validationModule.CustomizeApplicationRuntimeRules += ValidationModule_CustomizeApplicationRuntimeRules;
    }
    private void ValidationModule_CustomizeApplicationRuntimeRules(object sender, CustomizeApplicationRuntimeRulesEventArgs e) {
        foreach(var ruleSource in e.RuleSources) {
            PersistentContainerRuleSource containerRuleSource = ruleSource as PersistentContainerRuleSource;
            if(containerRuleSource != null) {
                if(typeof(MyPersistentRuleSource) == containerRuleSource.ClassType) {
                    containerRuleSource.EnableRuleCache = false;
                }
            }
        }
    }
}
```

***

To clear the Rule cache for all persistent Rule Sources, use the [IRuleSet.DropCachedRules](xref:DevExpress.Persistent.Validation.IRuleSet.DropCachedRules) method. To clear the Rule cache for a specific persistent Rule Source, find a corresponding `PersistentObjectRuleSource` or `PersistentContainerRuleSource` instance in the [IRuleSet.RegisteredSources](xref:DevExpress.Persistent.Validation.IRuleSet.RegisteredSources) collection and call the [IRuleSet.DropCachedRules()](xref:DevExpress.Persistent.Validation.IRuleSet.DropCachedRules) method.
