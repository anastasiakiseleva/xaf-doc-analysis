---
uid: "113010"
title: Trigger Validation Programmatically and Customize Default Rule Behavior
seealso:
- linkId: 113051
- linkId: 113008
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-highlight-invalid-properties-when-a-view-is-activated
  altText: How to Highlight Invalid Properties Immediately in an Invoked View
- linkId:  DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode
  altText: ModificationsController.ModificationsHandlingMode
---
# Trigger Validation Programmatically and Customize Default Rule Behavior

The XAF validation module allows you to configure validation parameters, trigger validation in code, and change the validation logic at runtime.

## Trigger Validation Programmatically

The @DevExpress.Persistent.Validation.IRuleSet interface declares the following validation methods you can call in a custom place in your code to trigger validation.

@DevExpress.Persistent.Validation.IRuleSet.ValidateTarget*
:   Checks whether the specified object satisfies all rules associated with specified contexts.
@DevExpress.Persistent.Validation.IRuleSet.ValidateAllTargets*
:   Checks whether specified objects satisfy all rules associated with specified contexts.
@DevExpress.Persistent.Validation.IRuleSet.Validate*
:   Checks whether the specified object satisfies all rules associated with specified contexts. If validation fails, the method raises an exception.
@DevExpress.Persistent.Validation.IRuleSet.ValidateAll*
:   Checks whether specified objects satisfy all rules associated with specified contexts. If validation fails, the method raises an exception.

These methods should be used from Controllers and Object Space events, and not within the persistent class scope that takes the Object Space instance as a parameter. 

You can use this methods to validate rules in predefined or custom [validation contexts](xref:113685). Call the @DevExpress.Persistent.Validation.Validator.GetService(System.IServiceProvider) method to access the @DevExpress.Persistent.Validation.IRuleSet object.


```csharp{21,22}
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Validation;
using YourApplicationName.Module.BusinessObjects;

namespace YourApplicationName.Blazor.Server.Controllers;

public class CustomBlazorController : ViewController {
    public CustomBlazorController() {
        var myBlazorAction = new SimpleAction(this, "MyBlazorAction", PredefinedCategory.Edit);
        myBlazorAction.Execute += (s, e) => {
            var os = Application.CreateObjectSpace(typeof(DemoTask));
            var tsk = os.FirstOrDefault<DemoTask>(t => t.Subject == "Task1");

            var employee = os.CreateObject<Employee>();
            employee.FirstName = "James";
            tsk.AssignedTo = employee;

            IRuleSet ruleSet = Validator.GetService(Application.ServiceProvider);
            ruleSet.Validate(os, employee, DefaultContexts.Save);
            os.CommitChanges();
        };
    }
}
```

## Customize Default Rule Behavior

The XAF validation module implements a set of validation-related events that allow you to change the predefined validation logic at runtime.

# [](#platform/net8)
Use the `ValidationOptions` class to handle validation events in XAF applications. The `ValidationOptions.Events` property 
exposes the following delegate properties:

* `OnCustomIsEmptyValue`
* `OnCustomIsEmptyValueType`
* `OnCustomNeedToValidateRule` 
* `OnCustomValidateRule`
* `OnRuleValidated`
* `OnValidationCompleted`

You can assign event handlers to their properties in two ways: use the XAF Application Builder or get a `ValidationOptions` instance as an [IOptionsSnapshot](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.ioptionssnapshot-1).

### Use the XAF Application Builder

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

### Get a ValidationOptions Instance as IOptionsSnapshot

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

# [](#platform/netframework46)

The following events are implemented in the @DevExpress.Persistent.Validation.RuleSet class:

: @DevExpress.Persistent.Validation.RuleSet.CustomIsEmptyValue
: @DevExpress.Persistent.Validation.RuleSet.CustomIsEmptyValueType
: @DevExpress.Persistent.Validation.RuleSet.CustomNeedToValidateRule 
: @DevExpress.Persistent.Validation.RuleSet.CustomValidateRule
: @DevExpress.Persistent.Validation.RuleSet.RuleValidated
: @DevExpress.Persistent.Validation.RuleSet.ValidationCompleted

***