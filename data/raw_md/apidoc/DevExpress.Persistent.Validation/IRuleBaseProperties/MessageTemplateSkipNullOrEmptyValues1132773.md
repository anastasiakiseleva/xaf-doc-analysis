---
uid: DevExpress.Persistent.Validation.IRuleBaseProperties.MessageTemplateSkipNullOrEmptyValues
name: MessageTemplateSkipNullOrEmptyValues
type: Property
summary: Specifies the template for the message displayed when the [Validation Rule](xref:113008) was not checked because the target properties are not specified.
syntax:
  content: |-
    [DefaultValue("The \"{Id}\" rule was not checked because one of the target properties is empty.")]
    string MessageTemplateSkipNullOrEmptyValues { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string holding the template for the message displayed when the Validation Rule was not checked because the target properties are not specified.
seealso: []
---
This property has the **RulePropertiesLocalized** attribute applied. So, the corresponding property of the [Application Model](xref:112580) is considered localizable.