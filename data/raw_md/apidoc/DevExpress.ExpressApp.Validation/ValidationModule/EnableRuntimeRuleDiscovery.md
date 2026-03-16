---
uid: DevExpress.ExpressApp.Validation.ValidationModule.EnableRuntimeRuleDiscovery
name: EnableRuntimeRuleDiscovery
type: Property
summary: Specifies if the Validation Module generates Rules from custom persistent Sources at runtime.
syntax:
  content: |-
    [DefaultValue(true)]
    public bool EnableRuntimeRuleDiscovery { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the Validation Module generates Rules from custom persistent Sources at runtime; otherwise, **false**.'
seealso:
- linkId: DevExpress.Persistent.Validation.IRuleSource
---
The Validation Module automatically collects persistent Validation Rule Sources and Rules when you start an application. Persistent Validation Rule Sources and Rules are persistent classes that implement the @DevExpress.Persistent.Validation.IRuleSource and @DevExpress.Persistent.Validation.IRule interfaces. You can disable automatic collection of persistent Rules and Rule Sources and add custom proxy Rule Sources with different behavior. The following code demonstrates how to do this in the platform-agnostic _MySolution.Module_ project:

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
        _validationModule.EnableRuntimeRuleDiscovery = false;
        _validationModule.CustomizeApplicationRuntimeRules += ValidationModule_CustomizeApplicationRuntimeRules;
    }
    private void ValidationModule_CustomizeApplicationRuntimeRules(object sender, CustomizeApplicationRuntimeRulesEventArgs e) {
        IRuleSource myRuleSource = new MyRuleSource();
        e.RuleSources.Add(myRuleSource);
    }
}
```
***
[`/validationModule.(CustomizeApplicationRuntimeRules)/`]: xref:DevExpress.ExpressApp.Validation.ValidationModule.CustomizeApplicationRuntimeRules
