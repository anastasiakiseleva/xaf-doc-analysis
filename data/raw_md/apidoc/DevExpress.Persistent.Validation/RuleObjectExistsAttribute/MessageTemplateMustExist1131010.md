---
uid: DevExpress.Persistent.Validation.RuleObjectExistsAttribute.MessageTemplateMustExist
name: MessageTemplateMustExist
type: Property
summary: Specifies the text to be written in the Validation Error window when the current rule is broken.
syntax:
  content: public string MessageTemplateMustExist { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value representing the text to be written to the Validation Error window when a rule is broken.
seealso: []
---
When defining a **RuleObjectExists** rule via the [](xref:DevExpress.Persistent.Validation.RuleObjectExistsAttribute) in code or in the [Model Editor](xref:112582), you may need to invert it (see [RuleBaseAttribute.InvertResult](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.InvertResult)), so that it is broken when objects that satisfy the specified criteria are found. In this instance, you should write a custom definition to be displayed in the Vaidation Error window for the broken rule. To do this, set the **CustomMessageTemplate** property. However, the list of the found objects will not be displayed. To display them, specify the **MessageTemplateMustExist** property instead of the **CustomMessageTemplate** property. The following code demonstrates this:

# [C#](#tab/tabid-csharp)

```csharp
[RuleObjectExists("ComplexValidationSettingsObject_RuleObjectExists", DefaultContexts.Save,
   "FirstName = '@FirstName' AND LastName = '@LastName'", MessageTemplateMustExist = 
   "Objects with the same combination of the" +
   "'FirstName' and 'LastName' properties must not exist.", 
   InvertResult = true, SkipNullOrEmptyValues = true)]
public class ComplexValidationSettingsObject: BaseObject{
   //...
}
```
***

This code is taken from the FeatureCenter demo that illustrates all the capabilities of the Validation module. This demo is located in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder, by default.

To customize the format that is used to list the found objects in the Validation Error window, use the [RuleObjectExistsAttribute.FoundObjectMessageFormat](xref:DevExpress.Persistent.Validation.RuleObjectExistsAttribute.FoundObjectMessageFormat) and [RuleObjectExistsAttribute.FoundObjectMessagesSeparator](xref:DevExpress.Persistent.Validation.RuleObjectExistsAttribute.FoundObjectMessagesSeparator) properties.

There is a set of format items you can use in message templates. For instance, when using the {TargetObject} format item, the validated object will be inserted at runtime. For details, refer to the [RuleBaseAttribute.CustomMessageTemplate](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.CustomMessageTemplate) property description.