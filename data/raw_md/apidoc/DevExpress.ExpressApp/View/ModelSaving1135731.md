---
uid: DevExpress.ExpressApp.View.ModelSaving
name: ModelSaving
type: Event
summary: Occurs before saving information on a View's controls to the [Application Model](xref:112580).
syntax:
  content: public event EventHandler<CancelEventArgs> ModelSaving
seealso:
- linkId: DevExpress.ExpressApp.View.ModelSaved
- linkId: DevExpress.ExpressApp.View.LoadModel*
- linkId: 118592
---
Handle this event to cancel saving the current parameters of the View's controls to the Application Model, before setting a new value for the [View.Model](xref:DevExpress.ExpressApp.View.Model) property and updating settings of the View and its controls.