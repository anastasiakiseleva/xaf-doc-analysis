---
uid: DevExpress.ExpressApp.Actions.ActionBase.TargetViewType
name: TargetViewType
type: Property
summary: Specifies the type of the [View](xref:112611), for which an [Action](xref:112622) is intended.
syntax:
  content: |-
    [DefaultValue(ViewType.Any)]
    public ViewType TargetViewType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ViewType
    description: A [](xref:DevExpress.ExpressApp.ViewType) enumeration value identifying a View type.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetViewId
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetViewNesting
- linkId: "113103"
---
If an Action is contained in a [](xref:DevExpress.ExpressApp.ViewController), you can use this property to specify the type of a View for which the Action will be activated. By default, this property is set to [ViewType.Any](xref:DevExpress.ExpressApp.ViewType.Any). You can set another value in the Controller's constructor or **Designer**. This value will be saved to the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Model.IModelAction) node.