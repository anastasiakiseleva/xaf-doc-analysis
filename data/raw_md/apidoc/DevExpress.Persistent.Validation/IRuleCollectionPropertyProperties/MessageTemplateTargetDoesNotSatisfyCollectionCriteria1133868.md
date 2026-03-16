---
uid: DevExpress.Persistent.Validation.IRuleCollectionPropertyProperties.MessageTemplateTargetDoesNotSatisfyCollectionCriteria
name: MessageTemplateTargetDoesNotSatisfyCollectionCriteria
type: Property
summary: Specifies the message displayed when the [Validation Rule](xref:113008) was not checked because a validated object is not an element of the target collection.
syntax:
  content: |-
    [DefaultValue("The \"{Id}\" rule was not checked because the target is not an element of the \"{TargetCollectionOwnerType}.{TargetCollectionPropertyName}\" collection.")]
    string MessageTemplateTargetDoesNotSatisfyCollectionCriteria { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the message displayed when the Rule was not checked because a validated object is not an element of the target collection.
seealso: []
---
When using the **ShowAllContexts** [Action](xref:112622), the invoked window shows the broken rules grouped by contexts. Double-click a context to invoke a Detail View for it. In the Detail View, you will be able to see the list of all rules checked in the current context. The text that is set for this property will be written for those rules that are not checked because the validated object is not an element of the target collection. For additional information, refer to the [Collection Validation](xref:113217) topic.