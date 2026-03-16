---
uid: DevExpress.Persistent.Validation.IRuleSet.ValidateAllTargets(DevExpress.ExpressApp.IObjectSpace,System.Collections.IEnumerable)
name: ValidateAllTargets(IObjectSpace, IEnumerable)
type: Method
summary: Silently (without raising the [RuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.IRuleSet.ValidationCompleted) event and throwing the [](xref:DevExpress.Persistent.Validation.ValidationException)) validates multiple targets and returns the result.
syntax:
  content: RuleSetValidationResult ValidateAllTargets(IObjectSpace targetObjectSpace, IEnumerable targets)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used by validation targets.
  - id: targets
    type: System.Collections.IEnumerable
    description: The list of objects to check.
  return:
    type: DevExpress.Persistent.Validation.RuleSetValidationResult
    description: The validation result. If all rules are satisfied, the `RuleSetValidationResult.IsValid` property returns `true`; otherwise, it returns `false`
seealso: []
---

The following code snippet demonstrates how to use this method to validate objects when an Action is executed:

# [C#](#tab/tabid-csharp)

```csharp{12-13}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Validation;
// ...
public partial class CustomValidationController : ViewController {
    public CustomValidationController() {
        SimpleAction validationAction = new SimpleAction(this, "ValidateBeforeSave", PredefinedCategory.Edit);
        validationAction.Execute += ValidationAction_Execute;
    }
    private void ValidationAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        RuleSetValidationResult validationResult = Validator.GetService(Application.ServiceProvider)
            .ValidateAllTargets(ObjectSpace, ObjectSpace.GetObjectsToSave(false));
        ValidationResults obj = new ValidationResults(validationResult, base.Application.Model);
        bool flag = validationResult.State != ValidationState.Invalid;
    }
}
```

***
