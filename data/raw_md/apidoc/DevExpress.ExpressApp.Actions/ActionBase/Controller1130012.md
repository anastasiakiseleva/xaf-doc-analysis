---
uid: DevExpress.ExpressApp.Actions.ActionBase.Controller
name: Controller
type: Property
summary: Provides access to an [Action](xref:112622)'s [Controller](xref:112621).
syntax:
  content: |-
    [Browsable(false)]
    public Controller Controller { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Controller
    description: A [](xref:DevExpress.ExpressApp.Controller) object representing the current action's Controller.
seealso: []
---
Actions are contained in Controllers. This property allows you to access members of the current Action's Controller (for instance, [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View), [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window), etc.).