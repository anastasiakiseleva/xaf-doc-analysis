---
uid: DevExpress.ExpressApp.View.ModelChanging
name: ModelChanging
type: Event
summary: Occurs before setting the [View.Model](xref:DevExpress.ExpressApp.View.Model) property for a View.
syntax:
  content: public event EventHandler ModelChanging
seealso:
- linkId: DevExpress.ExpressApp.View.ModelChanged
- linkId: 118592
---
After the  [View.Model](xref:DevExpress.ExpressApp.View.Model) property's value is changed, the View's settings will be updated and its controls will be created (recreated). Handle this event to perform custom actions before changing the [View.Model](xref:DevExpress.ExpressApp.View.Model) property's value.