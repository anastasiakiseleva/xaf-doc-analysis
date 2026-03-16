---
uid: DevExpress.Persistent.Validation.RuleSet.ValidateAllTargets(DevExpress.ExpressApp.IObjectSpace,System.Collections.IEnumerable)
name: ValidateAllTargets(IObjectSpace, IEnumerable)
type: Method
summary: Silently (without raising the [RuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.RuleSet.ValidationCompleted) event and throwing the [](xref:DevExpress.Persistent.Validation.ValidationException)) validates multiple targets and returns the result.
syntax:
  content: public RuleSetValidationResult ValidateAllTargets(IObjectSpace targetObjectSpace, IEnumerable targets)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used by a validation targets.
  - id: targets
    type: System.Collections.IEnumerable
    description: The list of objects to check.
  return:
    type: DevExpress.Persistent.Validation.RuleSetValidationResult
    description: The result of the [](xref:DevExpress.Persistent.Validation.RuleSet) validation.
seealso: []
---
Below is the example of using the **ValidateAllTargets** method and handling its result.

# [C#](#tab/tabid-csharp)

```csharp
RuleSetValidationResult validationResult = Validator.RuleSet.ValidateAllTargets(
    ObjectSpace, ObjectSpace.GetObjectsToSave(false), ContextIdentifier.Save);
ValidationResults obj = new ValidationResults(validationResult, base.Application.Model);
bool flag = validationResult.State != ValidationState.Invalid;
```
***
This method raises the [RuleSet.RuleValidated](xref:DevExpress.Persistent.Validation.RuleSet.RuleValidated) event for each target.