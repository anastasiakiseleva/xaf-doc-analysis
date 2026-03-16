---
uid: DevExpress.ExpressApp.Model.IModelAction.TargetViewId
name: TargetViewId
type: Property
summary: Specifies the identifier of the [View](xref:112611) for which the Action is activated, or a semicolon-separated list of identifiers if the Action targets multiple Views.
syntax:
  content: string TargetViewId { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that is a View identifier or a semicolon-separated list of View identifiers.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetViewId
---
The **TargetViewId** property is considered for Actions that are contained in View Controllers. In the [Model Editor](xref:112582), the **TargetViewId** property is readonly. The default value is obtained from the [ActionBase.TargetViewId](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewId) property. Refer to this property description for details.