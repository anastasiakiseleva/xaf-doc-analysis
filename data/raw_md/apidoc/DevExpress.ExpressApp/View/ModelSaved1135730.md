---
uid: DevExpress.ExpressApp.View.ModelSaved
name: ModelSaved
type: Event
summary: Occurs after the information on a View has been saved to the [Application Model](xref:112580).
syntax:
  content: public event EventHandler ModelSaved
seealso:
- linkId: DevExpress.ExpressApp.View.ModelSaving
- linkId: DevExpress.ExpressApp.View.LoadModel*
- linkId: 118592
---
Before setting a new value for the [View.Model](xref:DevExpress.ExpressApp.View.Model) property and updating settings of the View and its controls, the current parameters of the View's controls are saved to the Application Model. Handle this event to save custom information on the current View and its controls to the appropriate Application Model node.