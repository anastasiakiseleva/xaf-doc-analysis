---
uid: DevExpress.Persistent.Validation.RuleSet.ValidateAllTargets(DevExpress.ExpressApp.IObjectSpace,System.Collections.IEnumerable,DevExpress.Persistent.Validation.ContextIdentifiers)
name: ValidateAllTargets(IObjectSpace, IEnumerable, ContextIdentifiers)
type: Method
summary: Silently (without raising the [RuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.RuleSet.ValidationCompleted) event and throwing the [](xref:DevExpress.Persistent.Validation.ValidationException)) validates multiple targets and returns the result.
syntax:
  content: public RuleSetValidationResult ValidateAllTargets(IObjectSpace targetObjectSpace, IEnumerable targets, ContextIdentifiers contextIDs)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used by a validation target.
  - id: targets
    type: System.Collections.IEnumerable
    description: The list of objects to check.
  - id: contextIDs
    type: DevExpress.Persistent.Validation.ContextIdentifiers
    description: The [](xref:DevExpress.Persistent.Validation.ContextIdentifiers) object which is a set of validation contexts, rules for which will be collected. Default contexts are stored in the [](xref:DevExpress.Persistent.Validation.DefaultContexts) enumeration.
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