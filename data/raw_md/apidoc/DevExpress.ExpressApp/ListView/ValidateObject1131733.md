---
uid: DevExpress.ExpressApp.ListView.ValidateObject
name: ValidateObject
type: Event
summary: Occurs when the object represented by the [](xref:DevExpress.ExpressApp.ListView)'s focused row must be validated.
syntax:
  content: public event EventHandler<ValidateObjectEventArgs> ValidateObject
seealso: []
---
Handle this event to perform custom validation of the objects represented by an editable [List View](xref:112611). The object that is being validated can be accessed via the handler's **Object** parameter. Check whether it is valid, and if it is not, set the [ValidateObjectEventArgs.Valid](xref:DevExpress.ExpressApp.ValidateObjectEventArgs.Valid) to **false** and the [ValidateObjectEventArgs.ErrorText](xref:DevExpress.ExpressApp.ValidateObjectEventArgs.ErrorText) to the message that must be displayed in a UI. In this instance, it will be impossible to change the focused row until the entered data is corrected.