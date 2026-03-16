---
uid: DevExpress.Persistent.Validation.RuleBase
name: RuleBase
type: Class
summary: Serves as the base class for [Validation Rules](xref:113008).
syntax:
  content: 'public abstract class RuleBase : IRule, ISupportCheckRuleIntegrity, IObjectSpaceLink, ICaptionHelperProviderLink, IRulePropertiesCache'
seealso:
- linkId: DevExpress.Persistent.Validation.RuleBase._members
  altText: RuleBase Members
- linkId: "113008"
---
The **RuleBase** class is the basic abstract class implementing the [](xref:DevExpress.Persistent.Validation.IRule) interface. All the built-in Validation Rules inherit from **RuleBase**.

You can implement a custom Validation Rule by inheriting from the **RuleBase** class. To see an example, refer to the [Implement Custom Rules](xref:113051) topic.