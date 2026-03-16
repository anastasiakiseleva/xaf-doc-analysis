---
uid: DevExpress.Persistent.Validation.RuleSet.ValidateAll(DevExpress.ExpressApp.IObjectSpace,System.Collections.IEnumerable,DevExpress.Persistent.Validation.ContextIdentifiers,DevExpress.Persistent.Validation.ValidationFailedDelegate,DevExpress.ExpressApp.Frame)
name: ValidateAll(IObjectSpace, IEnumerable, ContextIdentifiers, ValidationFailedDelegate, Frame)
type: Method
summary: Validates multiple objects against **RuleSet**'s rules with the given validation contexts, returns a result and throws a [](xref:DevExpress.Persistent.Validation.ValidationException) if the validation fails.
syntax:
  content: public bool ValidateAll(IObjectSpace targetObjectSpace, IEnumerable targets, ContextIdentifiers contextIDs, ValidationFailedDelegate validationFailedDelegate, Frame sourceFrame = null)
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
  - id: validationFailedDelegate
    type: DevExpress.Persistent.Validation.ValidationFailedDelegate
    description: A method to call if the validation fails.
  - id: sourceFrame
    type: DevExpress.ExpressApp.Frame
    defaultValue: "null"
    description: The [Frame](xref:112608) of the Controller that validates objects. This parameter is [optional](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/named-and-optional-arguments#optional-arguments) and used in WinForms applications only.
  return:
    type: System.Boolean
    description: '**true**, if validation passes; otherwise, **false**.'
seealso: []
---
This method raises the [RuleSet.RuleValidated](xref:DevExpress.Persistent.Validation.RuleSet.RuleValidated) event for each target and the [RuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.RuleSet.ValidationCompleted) event at the end of validation.

The following example demonstrates how to use this method to validate objects when an Action is executed:

# [C#](#tab/tabid-csharp)

```csharp{12}
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
        Validator.RuleSet.ValidateAll(ObjectSpace, ObjectSpace.GetObjectsToSave(false), DefaultContexts.Save, null, Frame);
    }
}
```
***
