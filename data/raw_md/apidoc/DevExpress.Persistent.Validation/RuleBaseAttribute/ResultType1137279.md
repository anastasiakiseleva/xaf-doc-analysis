---
uid: DevExpress.Persistent.Validation.RuleBaseAttribute.ResultType
name: ResultType
type: Property
summary: Specifies the application behavior when the rule is broken.
syntax:
  content: public ValidationResultType ResultType { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Validation.ValidationResultType
    description: A [](xref:DevExpress.Persistent.Validation.ValidationResultType) enumeration value that specifies the application behavior when the rule is broken.
seealso: []
---
The default value is **Error**, i.e., a user must make data valid in order to proceed. However, you can define validation rules that can be ignored by end users by setting **ResultType** to **Warning** or **Info**.