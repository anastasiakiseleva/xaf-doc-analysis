---
uid: DevExpress.ExpressApp.Actions.ActionBase.TypeOfView
name: TypeOfView
type: Property
summary: Specifies the type of the [View](xref:112611) for which an [Action](xref:112622) is intended.
syntax:
  content: |-
    [Browsable(false)]
    [DefaultValue(null)]
    public Type TypeOfView { get; set; }
  parameters: []
  return:
    type: System.Type
    description: A [](xref:System.Type) object representing the View type, for which the current Action is intended.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetViewId
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetViewNesting
---
If an Action is contained in a [](xref:DevExpress.ExpressApp.ViewController), you can use this property to specify the type of a View for which the Action will be activated.