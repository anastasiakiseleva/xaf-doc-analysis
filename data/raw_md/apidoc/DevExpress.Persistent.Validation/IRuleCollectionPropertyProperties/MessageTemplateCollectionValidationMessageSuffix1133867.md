---
uid: DevExpress.Persistent.Validation.IRuleCollectionPropertyProperties.MessageTemplateCollectionValidationMessageSuffix
name: MessageTemplateCollectionValidationMessageSuffix
type: Property
summary: Specifies the additional text that will be displayed in the Validation Error window when the [Validation Rule](xref:113008) applied to a collection property is broken.
syntax:
  content: |-
    [DefaultValue("(For the \"{TargetCollectionOwnerType}.{TargetCollectionPropertyName}\" collection elements).")]
    string MessageTemplateCollectionValidationMessageSuffix { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the additional text that will be displayed in the Validation Error window when the Rule applied to a collection property is broken.
seealso: []
---
By default, this text specifies the validated collection. For additional information, refer to the [Collection Validation](xref:113217) topic.