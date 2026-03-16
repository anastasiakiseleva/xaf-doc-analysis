---
uid: DevExpress.Persistent.Validation.RuleCriteriaProperties.UsedProperties
name: UsedProperties
type: Property
summary: Specifies the names of the properties to be highlighted when the [Validation Rule](xref:113008) is broken.
syntax:
  content: |-
    [RulePropertiesIndex(2)]
    public string UsedProperties { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string holding a comma-separated list of property names that represent the properties to be highlighted when the Validation Rule is broken.
seealso:
- linkId: DevExpress.Persistent.Validation.RuleCriteriaAttribute.UsedProperties
---
> [!IMPORTANT]
> Always define **UsedProperties** for _warning_ and _info_ rules.