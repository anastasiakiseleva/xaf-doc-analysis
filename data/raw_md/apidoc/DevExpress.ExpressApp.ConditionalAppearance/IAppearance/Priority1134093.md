---
uid: DevExpress.ExpressApp.ConditionalAppearance.IAppearance.Priority
name: Priority
type: Property
summary: Specifies the volume of the conditional appearance rule. Used when several rules affect the same UI element.
syntax:
  content: int Priority { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the volume of the conditional appearance rule.
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Priority
- linkId: "113286"
---
There can be several conditional appearance rules affecting a property, layout item, layout group or Action. In this instance, the rules are applied according to the value specified by the **Priority** property. So, rules with higher **Priority** may override changes made by rules with a lower **Priority**.

Priority is not taken into account for rules that change the visibility state. A rule that hides a certain item always overrides other rules that enable the same item.