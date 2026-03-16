---
uid: DevExpress.Persistent.Validation.CodeRuleAttribute
name: CodeRuleAttribute
type: Class
summary: Applied to a validation rule. Specifies that the rule is intended for a particular business class and does not have a corresponding validation attribute.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class, AllowMultiple = false)]
    public class CodeRuleAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Validation.CodeRuleAttribute._members
  altText: CodeRuleAttribute Members
---
The rule's target class can be specified as the base class' generic parameter or via the rule's constructor. For details, refer to the "Implement a Code Rule" section of the [Implement Custom Rules](xref:113051) topic.