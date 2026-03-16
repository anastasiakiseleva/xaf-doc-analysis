---
uid: DevExpress.ExpressApp.Actions.ActionBase.TargetViewId
name: TargetViewId
type: Property
summary: Specifies the identifier of the [View](xref:112611) for which the Action is activated, or a semicolon-separated list of identifiers if the Action targets multiple Views.
syntax:
  content: |-
    [DefaultValue(null)]
    public string TargetViewId { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that is a View identifier or a semicolon-separated list of View identifiers.
seealso:
- linkId: "113103"
---
If an Action is contained in a View Controller, you can specify the ID of the View that must be displayed to activate the Action. The **TargetViewId** property is set to "Any" (the [ActionBase.AnyCaption](xref:DevExpress.ExpressApp.Actions.ActionBase.AnyCaption) constant value) by default which means that the Action is activated in any View where the View Controller is activated. You can set another **TargetViewId** value in the Controller's constructor and specify the identifier of a View to activate the Action for a specific View. You can also specify multiple target Views by separating their identifiers with a semicolon (;). The Action will be activated for each listed View. The **TargetViewId** value is passed to the [Application Model](xref:112580)'s [IModelAction.TargetViewId](xref:DevExpress.ExpressApp.Model.IModelAction.TargetViewId) property.