---
uid: DevExpress.Persistent.Validation.IRuleSet
name: IRuleSet
type: Interface
summary: Specifies a set of [Validation Rules](xref:113008) that can be checked against an object.
syntax:
  content: public interface IRuleSet
seealso:
- linkId: DevExpress.Persistent.Validation.IRuleSet._members
  altText: IRuleSet Members
- linkId: DevExpress.Persistent.Validation.IValidator
---

[Validation](xref:113684) is based on rules declared in business class code and in the **Validation** node of the [Application Model](xref:112580). Internally, these rules are automatically collected in the [RegisteredRules](xref:DevExpress.Persistent.Validation.IRuleSet.RegisteredRules) property of an @DevExpress.Persistent.Validation.IRuleSet object. The rules are checked automatically when objects are saved or deleted and when an Action with the appropriate [validation context](xref:113251) is executed.

If you need to modify the default behavior, you can use one of the following techniques to access an object that implements the `IRuleSet` interface (both examples demonstrate how to trigger validation against a specific object and context, and then handle the result):

* Use [Dependency Injection](xref:404364) to access the @DevExpress.Persistent.Validation.IValidator service. Use the injected service's `RuleSet` property to access an `IRuleSet`:
  
  **File:** _MySolution.Module.Controllers.MyController.cs_
  
  # [C#](#tab/tabid-csharp)

  ```csharp
  using DevExpress.Persistent.Validation;
  using Microsoft.Extensions.DependencyInjection;
  // ...
  namespace MySolution.Module.Controllers;
  public partial class MyController : ViewController {
      IServiceProvider serviceProvider;

      public MyController() { }

      [ActivatorUtilitiesConstructor]
      public MyController(IServiceProvider serviceProvider) : this() {
          InitializeComponent();
          this.serviceProvider = serviceProvider;
      }

      protected override void OnActivated() {
          base.OnActivated();
          RuleSetValidationResult result = serviceProvider.GetRequiredService<IValidator>()
              .RuleSet.ValidateTarget(View.ObjectSpace, View.CurrentObject, "MyContext");
          if (result.ValidationOutcome > ValidationOutcome.Information)
              ((Contact)View.CurrentObject).Notes += "[Validation Error] " + result.Results[0].ErrorMessage;
      }
  }
  ```

  ***

* Call the static [Validator.GetService](xref:DevExpress.Persistent.Validation.Validator.GetService(System.IServiceProvider)) method. This method takes an `IServiceProvider` instance as a parameter. In a context where @DevExpress.ExpressApp.XafApplication is available (for example, in a View Controller), you can use this method as follows:

  **File:** _MySolution.Module.Controllers.MyController.cs_

  # [C#](#tab/tabid-csharp)

  ```csharp
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

### How to Subscribe to Validation Events

You can use the `ValidationOptions` class to handle validation events. The `ValidationOptions.Events` property 
exposes the following delegate properties:

* `OnCustomIsEmptyValue`
* `OnCustomIsEmptyValueType`
* `OnCustomNeedToValidateRule` 
* `OnCustomValidateRule`
* `OnRuleValidated`
* `OnValidationCompleted`

You can assign event handlers to their properties in two ways: use the XAF Application Builder or get a `ValidationOptions` instance as [IOptionsSnapshot](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.ioptionssnapshot-1).

#### Use the XAF Application Builder

The following code sample subscribes to the `OnCustomNeedToValidateRule` event in the XAF Application Builder:

```csharp{5,6}
services.AddXaf(Configuration, builder => {
    //...
    builder.Modules
        //...
        .AddValidation(options => {
            options.Events.OnCustomNeedToValidateRule += (context) => {
                //...
            };
        });
    //...
};
```

#### Get a ValidationOptions instance as IOptionsSnapshot

The following code sample uses dependency injection and [IOptionsSnapshot](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.ioptionssnapshot-1) to subscribe to the `OnCustomNeedToValidateRule` event in an XAF controller:

```csharp{13,19,23}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Validation;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Options;

public class CustomValidationCheckController : WindowController {
    IOptionsSnapshot<ValidationOptions> options;

    [ActivatorUtilitiesConstructor]
    public CustomValidationCheckController(IServiceProvider serviceProvider) : this() {
        this.TargetWindowType = WindowType.Main;
        options = serviceProvider.GetRequiredService<IOptionsSnapshot<ValidationOptions>>();
    }
    public CustomValidationCheckController() { }

    protected override void OnActivated() {
        base.OnActivated();
        options.Value.Events.OnCustomNeedToValidateRule += CustomNeedToValidateRule;
    }

    protected override void OnDeactivated() {
        options.Value.Events.OnCustomNeedToValidateRule -= CustomNeedToValidateRule;
        base.OnDeactivated();
    }

    private void CustomNeedToValidateRule(CustomNeedToValidateRuleContext context) {
        //...
    }
}
```