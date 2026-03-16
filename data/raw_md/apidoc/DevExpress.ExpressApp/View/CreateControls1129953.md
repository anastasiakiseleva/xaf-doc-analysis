---
uid: DevExpress.ExpressApp.View.CreateControls
name: CreateControls()
type: Method
summary: Creates controls that visualize a View in a UI.
syntax:
  content: public void CreateControls()
seealso: []
---
A view is an abstract UI element. It is visualized via special controls. For [](xref:DevExpress.ExpressApp.DetailView) objects, controls of their [View Items](xref:112612) are created. For [](xref:DevExpress.ExpressApp.ListView) objects, a control of their [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor) is created.

The **CreateControls** method is called when a View needs to be displayed. After creating controls, this method raises the [View.ControlsCreated](xref:DevExpress.ExpressApp.View.ControlsCreated) event.

Generally, you do not need to call this method because Views are visualized automatically.