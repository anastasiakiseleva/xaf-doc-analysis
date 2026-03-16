---
uid: DevExpress.Persistent.Validation.RuleBaseAttribute.TargetContextIDs
name: TargetContextIDs
type: Property
summary: Specifies a context for checking the current Rule.
syntax:
  content: public string TargetContextIDs { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string representing a list of identifiers of the contexts when the current rule should be checked.
seealso:
- linkId: "113008"
- linkId: "402980"
---
When defining a rule via a validation attribute, you should specify the contexts when this rule will be checked. For this purpose, pass a string containing a list of context identifiers separated by semicolons as the _targetContextIDs_ parameter. A context identifier can be represented by any string value. To associate a context identifier with a particular Action, set it for the **ValidationContexts** property of the [Application Model](xref:112580)'s [!include[Node_Action](~/templates/node_action111373.md)] node. Via this property, you can associate any number of context identifiers with one Action, by listing them, separated by semicolons.

In addition to the Action-associated contexts, you can use predefined contexts represented by the [DefaultContexts.Save](xref:DevExpress.Persistent.Validation.DefaultContexts.Save) and [DefaultContexts.Delete](xref:DevExpress.Persistent.Validation.DefaultContexts.Delete) enumeration values. The **Save** context occurs when data is committed to the database (see [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges)). The **Delete** context occurs when an object is deleted from the database (see [BaseObjectSpace.Delete](xref:DevExpress.ExpressApp.BaseObjectSpace.Delete*)).

The contexts specified for a validation rule in code are set for the **TargetContextIDs** property of the [](xref:DevExpress.ExpressApp.Validation.IModelRuleBase) node. So, you can customize the context identifiers list directly in the Application Model.

> [!NOTE]
> You can specify an additional contextual criteria for a rule. If this criteria is satisfied by the validated object or property, the rule is checked. To do this, use [RuleBaseAttribute.TargetCriteria](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.TargetCriteria).