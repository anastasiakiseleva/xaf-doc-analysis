---
uid: DevExpress.Persistent.Validation.RuleCriteriaAttribute.UsedProperties
name: UsedProperties
type: Property
summary: Specifies the names of the properties to be highlighted when the rule generated from the current attribute is broken.
syntax:
  content: public string UsedProperties { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string holding a comma-separated list of property names that represent the properties to be highlighted when the Validation Rule is broken.
seealso:
- linkId: DevExpress.Persistent.Validation.RuleCriteriaProperties.UsedProperties
---
The [Validation Module](xref:113684) can highlight [Property Editors](xref:112612) in a [View](xref:112611) when a Validation Rule is broken. If certain properties contain invalid values, their names are specified via this property. 
> [!IMPORTANT]
> Always define **UsedProperties** for _warning_ and _info_ rules.