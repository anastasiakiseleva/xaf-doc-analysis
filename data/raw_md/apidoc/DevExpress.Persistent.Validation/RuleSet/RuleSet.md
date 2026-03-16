---
uid: DevExpress.Persistent.Validation.RuleSet
name: RuleSet
type: Class
summary: Specifies a set of [Validation Rules](xref:113008) that can be checked against an object.
syntax:
  content: 'public class RuleSet : IRuleSet, IEnumerable<IRule>, IEnumerable'
seealso:
- linkId: DevExpress.Persistent.Validation.RuleSet._members
  altText: RuleSet Members
---

> [!NOTE]
> This is a legacy class. In new applications that target .NET, use @DevExpress.Persistent.Validation.IRuleSet instead. Note that @DevExpress.Persistent.Validation.IRuleSet does not contains validation events. Refer to the following section to learn how to subscribe to RuleSet events in .NET.

[Validation](xref:113684) is based on rules declared in business class code and in the **Validation** node of the [Application Model](xref:112580). These rules are automatically collected in the @DevExpress.Persistent.Validation.RuleSet.RegisteredRules property of the @DevExpress.Persistent.Validation.RuleSet object. The validation module's engine checks rules when saving and deleting objects and when an Action with the corresponding [validation context](xref:113251) is executed. 

You should not create instances of the `RuleSet` class manually, because if you validate a custom `RuleSet`, rules from the default set are ignored and the validation result may be invalid.

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