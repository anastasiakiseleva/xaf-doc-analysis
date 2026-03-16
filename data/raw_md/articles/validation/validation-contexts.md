---
uid: "113685"
title: Validation Contexts
seealso: []
---
# Validation Contexts

When you create a [validation rule](xref:113008), you define the conditions under which the rule is checked — this is called the **validation context**.

You can use the [RuleBaseAttribute.TargetContextIDs](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.TargetContextIDs) property to specify one or several validation contexts for a rule. This value is assigned to the `TargetContextIDs` property of the @DevExpress.ExpressApp.Validation.IModelRuleBase node. You can also customize the context identifier list directly in the [Model Editor](xref:112580).

## Predefined Contexts

The XAF validation module implements the following predefined validation contexts:

@DevExpress.Persistent.Validation.DefaultContexts.Save
:   The validation rule is checked each time the object or its properties is saved to a database.  
	Note that in-place validation is initially enabled for this context (the @DevExpress.ExpressApp.Validation.IModelValidationContext.AllowInplaceValidation  property is set to `true`), so the rule is also checked after the input focus leaves the validated value until you disable the in-place validation.
@DevExpress.Persistent.Validation.DefaultContexts.Delete
:   The validation rule is checked before the object is deleted. 

Assign [DefaultContexts.Save](xref:DevExpress.Persistent.Validation.DefaultContexts.Save) or [DefaultContexts.Delete](xref:DevExpress.Persistent.Validation.DefaultContexts.Delete) value to the [RuleBaseAttribute.TargetContextIDs](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.TargetContextIDs) property to validate the rule in the predefined context.

```csharp
[RuleRequiredField("RuleRequiredField for Position.Title", DefaultContexts.Save, "A title must be specified.")]
public virtual string Title { get; set; }
```

In the Model Editor, select **Validation | Rules | \<ApplicationName>.Module.BusinessObjects | \<ClassName> | \<Rule Name>** and specify a value for the `TargetContextIDs` property.

![TargetContextIDs property in model editor](~/images/TargetContextIDs-in-model-editor.png)

## Custom Contexts

If predefined contexts do not satisfy your requirements and you need to perform validation outside of save and delete actions, you can create a custom validation context. 

Assign a custom context identifier to a rule and then trigger validation in this context. Note that there are no objects that store contexts, only a context identifier. The validation module's engine automatically collects all rules associated with this context and checks that the specified object(s) comply with the rules.

Specify the [RuleBaseAttribute.TargetContextIDs](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.TargetContextIDs) property to assign a custom context to a rule.

```csharp
[RuleRegularExpression("PasswordComplexity", "ChangePasswordContext", @"^(?=.*[a-zA-Z])(?=.*\d).{6,}$")]
public virtual String NewPassword { get; set; }
```

In the Model Editor, select **Validation | Rules | \<ApplicationName>.Module.BusinessObjects | \<ClassName> | \<Rule Name>** and specify a value for the `TargetContextIDs` property.

![Custom Context Id in Model Editor](~/images/TargetContextIDs-in-model-editor-custom.png)

### Trigger Validation in a Custom Context

You can trigger rule validation in a custom context as follows:

Trigger validation when an action is executed
:   Associate a context identifier with a particular [Action](xref:112622) to check all rules associated with this context when the action is executed.  
	In the Model Editor, select [!include[Node_Action](~/templates/node_action111373.md)] and specify a value for the @DevExpress.ExpressApp.Validation.IModelActionValidationContexts.ValidationContexts property. You can associate any number of context identifiers separated by a semicolon.

	![ValidationContexts property in Model Editor](~/images/ValidationContexts-in-model-editor-custom.png)

Trigger validation programmatically
:   Call a `IRuleSet.Validate*` method in any place in your code and specify the custom context identifier as a parameter to trigger validation of all rules associated with this context.

	```csharp{3-5}
	private void MyApplicationController_Activated(object sender, EventArgs e) {
		IRuleSet ruleSet = Validator.GetService(Application.ServiceProvider);
		RuleSetValidationResult result = ruleSet.ValidateTarget(
			View.ObjectSpace, View.CurrentObject, "ChangePasswordContext"
		);
		if (result.ValidationOutcome > ValidationOutcome.Information)
			((Contact)View.CurrentObject).Notes += "[Validation Error] " + result.Results[0].ErrorMessage;
	}
	```
	Refer to the following topic for more information: <xref:113010>.

## Validate Objects in Custom Object Spaces

The validation module's engine works automatically only for [object spaces](xref:113707) assigned to [views](xref:112611). If you manually instantiate a @DevExpress.ExpressApp.BaseObjectSpace and perform object modifications through this object space, these modifications are not validated. 

To validate such modifications, trigger validation manually. Refer to the following topic for more information: <xref:113010>.

## Target Criteria 

You can specify additional contextual criteria for a validation rule. Specify the @DevExpress.Persistent.Validation.RuleBaseAttribute.TargetCriteria property to trigger validation only if the specified criteria is satisfied.

```csharp
public class Contact : BaseObject {
    // The SpouseName value is required only when the IsMarried property is set to true
    [RuleRequiredField("SpouseNameIsRequiredWhenMarried", DefaultContexts.Save,
        SkipNullOrEmptyValues = false, TargetCriteria = "[IsMarried] == True")]
    public virtual String SpouseName { get; set; }
    public virtual bool IsMarried { get; set; }
    // ...
}
```