---
uid: DevExpress.ExpressApp.Actions.ActionBase.TargetViewNesting
name: TargetViewNesting
type: Property
summary: Specifies whether the [View](xref:112611), for which an [Action](xref:112622) is intended, must be root, nested or any.
syntax:
  content: |-
    [DefaultValue(Nesting.Any)]
    public Nesting TargetViewNesting { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Nesting
    description: A [](xref:DevExpress.ExpressApp.Nesting) enumeration value identifying a View kind.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetViewId
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetViewType
- linkId: "113103"
---
If an Action is contained in a View Controller, you can specify the kind of a View for which the Action will be activated via the **TargetViewNesting** property. By default, this property is set to **Any**. You can set another value in the Controller's constructor. This value will be saved to the [Application Model](xref:112580)'s [!include[Node_Action](~/templates/node_action111373.md)] node.