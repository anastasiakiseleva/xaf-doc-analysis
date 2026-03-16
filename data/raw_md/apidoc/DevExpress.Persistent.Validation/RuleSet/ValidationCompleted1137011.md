---
uid: DevExpress.Persistent.Validation.RuleSet.ValidationCompleted
name: ValidationCompleted
type: Event
summary: Occurs after validation of an entire [](xref:DevExpress.Persistent.Validation.RuleSet) is complete.
syntax:
  content: public event EventHandler<ValidationCompletedEventArgs> ValidationCompleted
seealso: []
---
Handle this event to change or remove the [ValidationCompletedEventArgs.Exception](xref:DevExpress.Persistent.Validation.ValidationCompletedEventArgs.Exception).

The following example demonstrates how to hide the @DevExpress.Persistent.Validation.ValidationException.ObjectHeaderFormat part of the validation message:

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.Persistent.Validation;

namespace MySolution.Module.Controllers {
    public class CustomizeValidationMessageController : WindowController {
        public CustomizeValidationMessageController() {
            TargetWindowType = WindowType.Main;
        }
        protected override void OnActivated() {
            base.OnActivated();
            Validator.RuleSet.ValidationCompleted += new EventHandler<ValidationCompletedEventArgs>(RuleSet_ValidationCompleted);
        }
        void RuleSet_ValidationCompleted(object sender, ValidationCompletedEventArgs e) {
            if (e.Exception != null) {
                e.Exception.ObjectHeaderFormat = "";
            }
        }
        protected override void OnDeactivated() {
            base.OnDeactivated();
            Validator.RuleSet.ValidationCompleted -= new EventHandler<ValidationCompletedEventArgs>(RuleSet_ValidationCompleted);
        }
    }
}
```
***

If the validation was performed by the [RuleSet.ValidateTarget](xref:DevExpress.Persistent.Validation.RuleSet.ValidateTarget(DevExpress.ExpressApp.IObjectSpace,System.Object,DevExpress.Persistent.Validation.ContextIdentifiers)) or [RuleSet.ValidateAllTargets](xref:DevExpress.Persistent.Validation.RuleSet.ValidateAllTargets*) method, the **ValidationCompleted** event is not raised.

[!include[](~/templates/validation-rule-set-event-note.md)]
