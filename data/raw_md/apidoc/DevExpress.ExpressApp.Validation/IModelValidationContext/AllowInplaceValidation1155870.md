---
uid: DevExpress.ExpressApp.Validation.IModelValidationContext.AllowInplaceValidation
name: AllowInplaceValidation
type: Property
summary: Specifies whether or not in-place validation is allowed for the current context.
syntax:
  content: |-
    [DefaultValue(false)]
    bool AllowInplaceValidation { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the current context uses in-place validation; otherwise, **false**.'
seealso: []
---
In-place validation occurs immediately for the current [context](xref:113685) after the input focus changes. It is enabled for the **Save** context by default.

The following error message is displayed when the input focus changes.

![InplaceValidation](~/images/inplacevalidation120504.png) ![InplaceValidation_Win](~/images/inplacevalidation_win120505.png)

The in-place validation occurs only if the rule evaluation does not require querying additional data from the server.
Thus, only the following rules can be validated immediately.

* [](xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute)
* [](xref:DevExpress.Persistent.Validation.RuleRegularExpressionAttribute)
* [](xref:DevExpress.Persistent.Validation.RuleStringComparisonAttribute)
* [](xref:DevExpress.Persistent.Validation.RuleValueComparisonAttribute)
* [](xref:DevExpress.Persistent.Validation.RuleRangeAttribute)

As the rule evaluation occurs on the client side, the in-place validation does not occur when:

* the rule's target property is a [collection](xref:113568), [image](xref:113544) or [reference](xref:113572) property (except for **RuleReqiredField** which is supported for reference properties);
* the [](xref:DevExpress.Persistent.Validation.ParametersMode) type parameter passed to the **RuleRange** or the **RuleValueComparison** attribute is set to **Expression**;
* the [RuleBaseAttribute.TargetCriteria](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.TargetCriteria) is specified.

When in-place validation is enabled, the regular validation mechanism is still triggered when an Action associated with the  current context is executed.

> [!NOTE]
> The asterisk (\*) symbol is appended to an editor label when the **RuleRequiredField** is applied.

> [!IMPORTANT]
> The in-place validation engine relies on Controllers provided in the platform-specific [](xref:DevExpress.ExpressApp.Validation.Win.ValidationWindowsFormsModule).