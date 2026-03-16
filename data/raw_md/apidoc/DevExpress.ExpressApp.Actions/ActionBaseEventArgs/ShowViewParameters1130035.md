---
uid: DevExpress.ExpressApp.Actions.ActionBaseEventArgs.ShowViewParameters
name: ShowViewParameters
type: Property
summary: Provides access to the **ShowViewParameters** object, specifying a [View](xref:112611), displayed after executing the current [Action](xref:112622).
syntax:
  content: public ShowViewParameters ShowViewParameters { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ShowViewParameters
    description: A **ShowViewParameters** object that specifies the View created after executing the current Action.
seealso:
- linkId: "112803"
---
In addition to custom operations performed when executing an Action, you can provide display of an additional View after executing this Action. This property allows you to specify this View and its settings in the **Execute** event handler. To access the View before it has been shown, handle the [ActionBase.ProcessCreatedView](xref:DevExpress.ExpressApp.Actions.ActionBase.ProcessCreatedView) event.