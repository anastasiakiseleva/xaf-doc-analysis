---
uid: DevExpress.Persistent.Validation.IRuleBaseProperties.MessageTemplateTargetDoesNotSatisfyTargetCriteria
name: MessageTemplateTargetDoesNotSatisfyTargetCriteria
type: Property
summary: Specifies the template for the message displayed when the [Validation Rule](xref:113008) was not checked because the criteria specified by the [RuleBaseProperties.TargetCriteria](xref:DevExpress.Persistent.Validation.RuleBaseProperties.TargetCriteria) property is not satisfied by the validated object.
syntax:
  content: |-
    [DefaultValue("The \"{Id}\" rule was not checked because the target object does not satisfy rule's target criteria.")]
    string MessageTemplateTargetDoesNotSatisfyTargetCriteria { get; set; }
  parameters: []
  return:
    type: System.String
    description: Specifies the template for the message displayed when the Validation Rule was not checked because the criteria specified by the **TargetCriteria** property is not satisfied by the validated object.
seealso:
- linkId: DevExpress.Persistent.Validation.RuleBaseAttribute.TargetCriteria
---
This property has the **RulePropertiesLocalized** attribute applied. So, the corresponding property of the [Application Model](xref:112580) is considered localizable.