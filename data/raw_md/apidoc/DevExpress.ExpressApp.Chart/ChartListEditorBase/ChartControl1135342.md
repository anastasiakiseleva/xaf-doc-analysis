---
uid: DevExpress.ExpressApp.Chart.ChartListEditorBase.ChartControl
name: ChartControl
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.Chart.ChartListEditorBase)'s control.
syntax:
  content: public object ChartControl { get; }
  parameters: []
  return:
    type: System.Object
    description: An object representing the current List Editor's control.
seealso: []
---
You can use this property to customize the List Editor's control. Generally, the recommended place to do this is a custom [Controller](xref:112621)'s [ViewController.ViewControlsCreated](xref:DevExpress.ExpressApp.ViewController.ViewControlsCreated) event handler. The [](xref:402154) article illustrates this approach.

If you need to execute a custom action after a List Editor's control has been created, handle the [ListEditor.ControlsCreated](xref:DevExpress.ExpressApp.Editors.ListEditor.ControlsCreated) event.