---
uid: DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRule
name: IModelAppearanceRule
type: Interface
summary: The **AppearanceRule** node defines a particular conditional appearance rule.
syntax:
  content: 'public interface IModelAppearanceRule : IModelNode, IAppearanceRuleProperties, IAppearance'
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRule._members
  altText: IModelAppearanceRule Members
- linkId: "113286"
- linkId: "112579"
- linkId: "112580"
---
The **AppearanceRule** node's own properties are used for internal needs. The properties displayed in the Model Editor are inherited from the [](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties) interface supported by this node.

To learn how to use the **AppearanceRule** node to add conditional appearance rules, refer to the [Declare Conditional Appearance Rules in the Application Model](xref:113372) topic.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.