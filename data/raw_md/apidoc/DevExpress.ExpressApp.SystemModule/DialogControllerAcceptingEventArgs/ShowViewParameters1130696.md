---
uid: DevExpress.ExpressApp.SystemModule.DialogControllerAcceptingEventArgs.ShowViewParameters
name: ShowViewParameters
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.ShowViewParameters) object used to specify a View to be displayed after executing the [DialogController.Accepting](xref:DevExpress.ExpressApp.SystemModule.DialogController.Accepting) event.
syntax:
  content: public ShowViewParameters ShowViewParameters { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ShowViewParameters
    description: A [](xref:DevExpress.ExpressApp.ShowViewParameters) object that represents a set of parameters used to display a new [View](xref:112611).
seealso: []
---
In addition to custom operations performed when executing the [DialogController.Accepting](xref:DevExpress.ExpressApp.SystemModule.DialogController.Accepting) Action, you can provide display of an additional View after executing this Action. This property allows you to specify this View and its settings. To access the View after it has been shown, handle the [ActionBase.ExecuteCompleted](xref:DevExpress.ExpressApp.Actions.ActionBase.ExecuteCompleted) event of the Accept Action specified by the [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction) property.