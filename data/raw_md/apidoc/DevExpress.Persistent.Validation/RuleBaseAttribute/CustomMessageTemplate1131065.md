---
uid: DevExpress.Persistent.Validation.RuleBaseAttribute.CustomMessageTemplate
name: CustomMessageTemplate
type: Property
summary: Specifies informational text that is to be added to the exception message when the current [Validation Rule](xref:113008) is broken.
syntax:
  content: public string CustomMessageTemplate { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that contains information on the current rule.
seealso: []
---
When a validation rule is broken, an XAF application invokes the error window that displays the information on this broken rule. Each rule has its default message template. The [Model Editor](xref:112582) **IModelValidationDefaultErrorMessageTemplates** node lists these default templates: 

![The IModelValidationDefaultErrorMessageTemplates node in the Model Editor](~/images/IModelValidationDefaultErrorMessageTemplates.png)

You can use format items to include property values in the message. A format item is a property path wrapped in curly braces. The property path is resolved from the current rule object. You can use properties of the [RuleBase](xref:DevExpress.Persistent.Validation.RuleBase) and [RuleBaseProperties](xref:DevExpress.Persistent.Validation.RuleBaseProperties) descendant classes. For example, use the following format items:

{TargetObject}
:   The [display member](xref:113525) of the validated object or its key property value if the display member is not declared.

{TargetObject.\<The Object's Property Name>}
:   The value of the specified validated object property.

{TargetValue}
:   The value of the validated property.

{TargetPropertyName}
:   The localized caption of the validated property.

{RightOperand}
:   The value to be compared to the target property value. You can only use this format item in `CustomMessageTemplate` with rules that have the `RightOperand` property. For example, you can use this item with the following attribute: [RuleValueComparison](xref:DevExpress.Persistent.Validation.RuleValueComparisonAttribute).

### How to Customize the Message Template
#### In the Model Editor
You can customize default messages in the **IModelValidationDefaultErrorMessageTemplates** child nodes globally for all rules in the application. 

To specify a custom message template for a rule, navigate to the **Validation** | **Rules** | **Rule** node and modify its **CustomMessageTemplate** or **MessageTemplate…** property: 

![The MessageTemplateMustNotBeEmpty property](~/images/IModelValidationRules_MessageTemplate.png)

#### In Code
To set a custom message for a particular rule in code, specify the **CustomMessageTemplate** parameter of a rule attribute. The following example demonstrates how to use a format item to include the [RightOperand](xref:DevExpress.Persistent.Validation.RuleValueComparisonProperties.RightOperand) value in the validation message:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Validation;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
//...
public class Account : BaseObject {
   [RuleValueComparison("RuleRequiredField for Account .Amount", DefaultContexts.Save,
      ValueComparisonType.LessThan, 100,
      CustomMessageTemplate = "The Amount must not be less than {RightOperand}.")]
   public virtual double Amount { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Validation;
using System.ComponentModel;
//...
public class Account : BaseObject {
   //...
   private double amount;
   [RuleValueComparison("RuleRequiredField for Account .Amount", DefaultContexts.Save,
      ValueComparisonType.LessThan, 100,
      CustomMessageTemplate = "The Amount must not be less than {RightOperand}.")]
   public double Amount { 
      get { 
         return amount; 
      }
      set { 
         SetPropertyValue(nameof(Amount), ref amount, value);
      }
   }
}
```
***

The **CustomMessageTemplate** property of the corresponding [](xref:DevExpress.ExpressApp.Validation.IModelRuleBase) node stores the message template specified for the validation rule attribute in code. 

> [!NOTE]
> Note that **CustomMessageTemplate** does not include the list of found objects when you specify this property for the @DevExpress.Persistent.Validation.RuleUniqueValueAttribute or inverted @DevExpress.Persistent.Validation.RuleIsReferencedAttribute / @DevExpress.Persistent.Validation.RuleObjectExistsAttribute. To display this list, specify the  **MessageTemplateMustBeUnique** property instead of **CustomMessageTemplate** in the corresponding Model Editor nodes.
