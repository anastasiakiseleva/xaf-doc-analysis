---
uid: DevExpress.ExpressApp.Validation.ValidationModule.CustomizeApplicationRuntimeRules
name: CustomizeApplicationRuntimeRules
type: Event
summary: Occurs when the [ValidationModule.InitializeRuleSet](xref:DevExpress.ExpressApp.Validation.ValidationModule.InitializeRuleSet) method is invoked.
syntax:
  content: public event EventHandler<CustomizeApplicationRuntimeRulesEventArgs> CustomizeApplicationRuntimeRules
seealso: []
---
Handle this event to create validation rules at run time. Add the required rules to the **Rules** collection. The following code snippet demonstrates how to create a validation rule at run time, ensuring that an end-user will not be able to save a **Contact** object unless its **Anniversary** property is specified.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Validation;
using DevExpress.Persistent.Validation;
//...
public sealed partial class MyModule : ModuleBase {
    ValidationModule validationModule;
    public MyModule() {
        InitializeComponent();
    }
    public override void Setup(ApplicationModulesManager moduleManager) {
        base.Setup(moduleManager);
        validationModule = moduleManager.Modules.FindModule<ValidationModule>();
        validationModule.CustomizeApplicationRuntimeRules += OnCustomizeRules;
    }
    void OnCustomizeRules(object sender, CustomizeApplicationRuntimeRulesEventArgs e) {
        RuleRequiredField myRule =
            new RuleRequiredField("myRule", 
            XafTypesInfo.Instance.FindTypeInfo(typeof(Contact)).FindMember("Anniversary"), 
            ContextIdentifier.Save);
        e.Rules.Add(myRule);
    }
}
```
***
