---
uid: DevExpress.ExpressApp.Validation.ContextValidatingEventArgs
name: ContextValidatingEventArgs
type: Class
summary: Arguments passed to the [PersistenceValidationController.ContextValidating](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController.ContextValidating) event.
syntax:
  content: 'public class ContextValidatingEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Validation.ContextValidatingEventArgs._members
  altText: ContextValidatingEventArgs Members
---
The **ContextValidating** event occurs when validation rules associated with the **Delete** or **Save** validation contexts are about to be checked. Handle this event to force validation of specific objects, which otherwise would not be validated automatically in a particular situation.