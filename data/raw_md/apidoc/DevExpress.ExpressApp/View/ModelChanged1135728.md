---
uid: DevExpress.ExpressApp.View.ModelChanged
name: ModelChanged
type: Event
summary: Occurs after setting the [View.Model](xref:DevExpress.ExpressApp.View.Model) property for a View.
syntax:
  content: public event EventHandler ModelChanged
seealso:
- linkId: DevExpress.ExpressApp.View.ModelChanging
- linkId: 118592
---
After the  [View.Model](xref:DevExpress.ExpressApp.View.Model) property's value is changed, the View's settings will be updated and its controls will be created (recreated). Handle this event to perform custom actions after the [View.Model](xref:DevExpress.ExpressApp.View.Model) property is changed and the controls are created.
