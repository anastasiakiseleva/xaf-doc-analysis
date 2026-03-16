---
uid: DevExpress.Persistent.Validation.RuleSet.CustomNeedToValidateRule
name: CustomNeedToValidateRule
type: Event
summary: Occurs when the validation system determines whether or not a rule should be validated.
syntax:
  content: public static event EventHandler<CustomNeedToValidateRuleEventArgs> CustomNeedToValidateRule
seealso: []
---
The validation system validates a rule when it corresponds to the current context. Handle this event to change this behavior. The [NeedToValidateObjectEventArgs.NeedToValidate](xref:DevExpress.ExpressApp.Validation.NeedToValidateObjectEventArgs.NeedToValidate) parameter allows you to cancel or enable the rule validation. Set the **Handled** parameter to **true** to cancel the default logic that determines whether a rule should be validated. 

The following Controller unconditionally enables the rule with [Id](xref:DevExpress.Persistent.Validation.IRule.Id) = "MyRule" for the **Employee** Detail View:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.Persistent.Validation;
// ...
namespace MySolution.Module.Controllers {
    public class ValidateMyRuleAlwaysController : ObjectViewController<DetailView, Employee> {
        protected override void OnActivated() {
            base.OnActivated();
            RuleSet.CustomNeedToValidateRule += RuleSet_CustomNeedToValidateRule;
        }
        void RuleSet_CustomNeedToValidateRule(object sender, CustomNeedToValidateRuleEventArgs e) {
            if (!e.Handled && e.Rule.Id == "MyRule") {
                e.NeedToValidateRule = true;
                e.Handled = true;
            }
        }
        protected override void OnDeactivated() {
            RuleSet.CustomNeedToValidateRule -= RuleSet_CustomNeedToValidateRule;
            base.OnDeactivated();
        }
    }
}
```
***

If you want to enable this rule for all Views in the application, subscribe to this event in the [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup(DevExpress.ExpressApp.XafApplication)) method.

[!include[](~/templates/validation-rule-set-event-note.md)]
