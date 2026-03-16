---
uid: DevExpress.Persistent.Validation.RuleBase.UsedProperties
name: UsedProperties
type: Property
summary: Specifies the names of the properties to be highlighted when the current [Validation Rule](xref:113008) is broken.
syntax:
  content: public virtual ReadOnlyCollection<string> UsedProperties { get; }
  parameters: []
  return:
    type: System.Collections.ObjectModel.ReadOnlyCollection{System.String}
    description: A **ReadOnlyCollection\<String>** object representing a list of property names that must be highlighted as invalid when the Validation Rule is broken.
seealso: []
---
The [Validation Module](xref:113684) can highlight [Property Editors](xref:112612) in a [View](xref:112611) when a Validation Rule is broken. If certain properties contain invalid values, their names are specified via this property. In the [](xref:DevExpress.Persistent.Validation.RuleBase) class, this property returns an empty list. To see how to implement this property in your custom rule, refer to the [IRule.UsedProperties](xref:DevExpress.Persistent.Validation.IRule.UsedProperties) topic.
> [!IMPORTANT]
> Always define the **UsedProperties** value for _warning_ and _info_ rules.