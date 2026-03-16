---
uid: DevExpress.ExpressApp.ValidateObjectEventArgs
name: ValidateObjectEventArgs
type: Class
summary: Represents arguments passed to the [ListView.ValidateObject](xref:DevExpress.ExpressApp.ListView.ValidateObject) and [ListEditor.ValidateObject](xref:DevExpress.ExpressApp.Editors.ListEditor.ValidateObject) events.
syntax:
  content: 'public class ValidateObjectEventArgs : ObjectManipulatingEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.ValidateObjectEventArgs._members
  altText: ValidateObjectEventArgs Members
---
The **ValidateObject** event occurs when a row must be validated. You can use the **ValidateObject** event to perform custom validation of a [List Editor](xref:113189)'s rows. The [ObjectManipulatingEventArgs.Object](xref:DevExpress.ExpressApp.ObjectManipulatingEventArgs.Object) parameter specifies the object that is being checked. The [ValidateObjectEventArgs.Valid](xref:DevExpress.ExpressApp.ValidateObjectEventArgs.Valid) parameter indicates whether the object is valid or not. If you need to perform custom validation, handle the **ValidateObject** event, and check the **Object**. If it is not valid, set the **Valid** parameter to **false**, and the [ValidateObjectEventArgs.ErrorText](xref:DevExpress.ExpressApp.ValidateObjectEventArgs.ErrorText) parameter to the message that must be displayed in a UI. This will prevent a user from changing focus from the row until the entered data is corrected.