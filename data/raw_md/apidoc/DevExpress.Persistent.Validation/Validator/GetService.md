---
uid: DevExpress.Persistent.Validation.Validator.GetService(System.IServiceProvider)
name: GetService(IServiceProvider)
type: Method
summary: Takes an `IServiceProvider` instance as a parameter and returns an instance of @DevExpress.Persistent.Validation.IRuleSet.
syntax:
  content: public static IRuleSet GetService(IServiceProvider serviceProvider)
  parameters:
  - id: serviceProvider
    type: System.IServiceProvider
    description: An object that implements the `IServiceProvider` interface.
  return:
    type: DevExpress.Persistent.Validation.IRuleSet
    description: An object that implements the `IRuleSet` interface.
seealso: []
---

Use this method to access an object that implements the `IRuleSet` interface. Refer to the [](xref:DevExpress.Persistent.Validation.IRuleSet) topic for more information.

## Example

The following code snippet demonstrates how to use the `Validator.GetService` method to access an `IRuleSet` instance and use it to trigger validation against a specific object and context, and then handle the result:

**File:** _MySolution.Module.Controllers.MyController.cs_

# [C#](#tab/tabid-csharp)

```csharp{8-12}
using DevExpress.Persistent.Validation;
// ...
namespace MySolution.Module.Controllers;
public partial class MyController : ViewController {
    // ...
    protected override void OnActivated() {
        base.OnActivated();
        RuleSetValidationResult result = Validator.GetService(Application.ServiceProvider).ValidateTarget(
            View.ObjectSpace, 
            View.CurrentObject, 
            "MyContext"
        );
        if (result.ValidationOutcome > ValidationOutcome.Information)
            ((Contact)View.CurrentObject).Notes += "[Validation Error] " + result.Results[0].ErrorMessage;
    }
}
```

***