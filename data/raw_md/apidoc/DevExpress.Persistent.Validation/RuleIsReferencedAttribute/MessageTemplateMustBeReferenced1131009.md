---
uid: DevExpress.Persistent.Validation.RuleIsReferencedAttribute.MessageTemplateMustBeReferenced
name: MessageTemplateMustBeReferenced
type: Property
summary: Specifies the text to be written in the Validation Error window when the current rule is broken.
syntax:
  content: public string MessageTemplateMustBeReferenced { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value representing the text to be written to the Validation Error window when a rule is broken.
seealso: []
---
When defining a RuleIsReferenced via the [](xref:DevExpress.Persistent.Validation.RuleIsReferencedAttribute) in code or in the [Model Editor](xref:112582), you may need to invert it (see [RuleBaseAttribute.InvertResult](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.InvertResult)), so that it is broken when objects that reference the current object are found. In this instance, you should write a custom definition to be displayed in the Vaidation Error window for the broken rule. To do this, set the **CustomMessageTemplate** property. However, the list of found objects will not be displayed. To display them, specify the **MessageTemplateMustBeReferenced** property instead of the **CustomMessageTemplate** property. The following code demonstrates this:

# [C#](#tab/tabid-csharp)

```csharp
[RuleIsReferenced("ComplexValidationSettingsObject_RuleIsReferenced", 
   DefaultContexts.Delete, typeof(ComplexValidationSettingsObject), 
   "ReferencedObject", MessageTemplateMustBeReferenced = 
   "To delete the '{TargetObject}' object, you must be sure that it is not referenced anywhere.", 
   InvertResult = true)]
public class ComplexValidationSettingsObject : BaseObject {
   //...
}
```
***

[!include[<`MessageTemplateMustBeReferenced` property>](~/templates/main-demo-tip.md)]

To customize the format that is used to list the found objects in the Validation Error window, use the [RuleIsReferencedAttribute.FoundObjectMessageFormat](xref:DevExpress.Persistent.Validation.RuleIsReferencedAttribute.FoundObjectMessageFormat) and [RuleIsReferencedAttribute.FoundObjectMessagesSeparator](xref:DevExpress.Persistent.Validation.RuleIsReferencedAttribute.FoundObjectMessagesSeparator) properties.

As you can see in the code above, the {TargetObject} format item is used in the message template. At runtime, this item will be replaced with the validated object. There is set of format items you can use in message templates. For details, refer to the [RuleBaseAttribute.CustomMessageTemplate](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.CustomMessageTemplate) property description.