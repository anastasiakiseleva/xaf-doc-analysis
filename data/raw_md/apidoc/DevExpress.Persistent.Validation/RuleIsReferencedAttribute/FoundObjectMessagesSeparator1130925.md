---
uid: DevExpress.Persistent.Validation.RuleIsReferencedAttribute.FoundObjectMessagesSeparator
name: FoundObjectMessagesSeparator
type: Property
summary: Specifies a separator for the object list written in the error message for the current rule.
syntax:
  content: public string FoundObjectMessagesSeparator { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that represents a separator.
seealso: []
---
Set this property if the [RuleIsReferencedAttribute.FoundObjectMessageFormat](xref:DevExpress.Persistent.Validation.RuleIsReferencedAttribute.FoundObjectMessageFormat) property is not set to an empty string (by default, it is set to _"{0}"_). When several objects that reference the target object are found, they should be separated by a symbol when being added to the error message of this rule. By default, this property is set to ", ".

> [!NOTE]
> When defining the [](xref:DevExpress.Persistent.Validation.RuleIsReferencedAttribute) in code, the value for the **FoundObjectMessageSeparator** property is passed as a named parameter. This means that you do not have to specify it. However, when specifying, use the following format: `FoundObjectMessageSeparator = "; "`.