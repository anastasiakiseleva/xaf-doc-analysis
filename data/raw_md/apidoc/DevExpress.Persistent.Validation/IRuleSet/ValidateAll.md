---
uid: DevExpress.Persistent.Validation.IRuleSet.ValidateAll(DevExpress.ExpressApp.IObjectSpace,System.Collections.IEnumerable,DevExpress.Persistent.Validation.ContextIdentifiers,DevExpress.Persistent.Validation.ValidationFailedDelegate,DevExpress.ExpressApp.Frame)
name: ValidateAll(IObjectSpace, IEnumerable, ContextIdentifiers, ValidationFailedDelegate, Frame)
type: Method
summary: Validates multiple objects against `RuleSet` rules with the given validation contexts. If validation fails, the [](xref:DevExpress.Persistent.Validation.ValidationException) is thrown and the method passed as the `validationFailedDelegate` parameter is called.
syntax:
  content: bool ValidateAll(IObjectSpace targetObjectSpace, IEnumerable targets, ContextIdentifiers contextIDs, ValidationFailedDelegate validationFailedDelegate, Frame sourceFrame = null)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used by a validation target.
  - id: targets
    type: System.Collections.IEnumerable
    description: The list of objects to check.
  - id: contextIDs
    type: DevExpress.Persistent.Validation.ContextIdentifiers
    description: The [](xref:DevExpress.Persistent.Validation.ContextIdentifiers) object, which is a set of validation contexts for which rules will be collected. Default contexts are stored in the [](xref:DevExpress.Persistent.Validation.DefaultContexts) enumeration.
  - id: validationFailedDelegate
    type: DevExpress.Persistent.Validation.ValidationFailedDelegate
    description: A method to call if the validation fails.
  - id: sourceFrame
    type: DevExpress.ExpressApp.Frame
    defaultValue: "null"
    description: The [Frame](xref:112608) of the Controller that validates objects. This parameter is [optional](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/named-and-optional-arguments#optional-arguments) and used in WinForms applications only.
  return:
    type: System.Boolean
    description: '`true` if validation passes; otherwise, `false`.'
seealso: []
---

This method raises the [IRuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.IRuleSet.ValidationCompleted) event at the end of validation.

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
        Validator.GetService(Application.ServiceProvider)
            .ValidateAll(ObjectSpace, ObjectSpace.GetObjectsToSave(false), DefaultContexts.Save, null, Frame);
    }
}
```

***
