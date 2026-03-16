---
uid: DevExpress.Persistent.Validation.IRuleSource.CreateRules
name: CreateRules()
type: Method
summary: Instantiates custom [Validation Rules](xref:113008).
syntax:
  content: ICollection<IRule> CreateRules()
  return:
    type: System.Collections.Generic.ICollection{DevExpress.Persistent.Validation.IRule}
    description: An **ICollection\<**[](xref:DevExpress.Persistent.Validation.IRule)**>** object, which represents custom Validation Rules.
seealso: []
---
When implementing the [](xref:DevExpress.Persistent.Validation.IRuleSource) interface, use this property to supply the Validation Module with custom Validation Rules.

To see an example of implementing the **IRuleSource** interface, refer to the "Custom Rule Source" section of the [Declare Validation Rules](xref:113251) topic.