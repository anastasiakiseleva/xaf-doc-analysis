---
uid: DevExpress.ExpressApp.Security.NonSecureActionsInitializingEventArgs
name: NonSecureActionsInitializingEventArgs
type: Class
summary: Provides data for the @DevExpress.ExpressApp.Security.SecurityModule.NonSecureActionsInitializing event.
syntax:
  content: 'public class NonSecureActionsInitializingEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Security.NonSecureActionsInitializingEventArgs._members
  altText: NonSecureActionsInitializingEventArgs Members
---
The @DevExpress.ExpressApp.Security.SecurityModule.NonSecureActionsInitializing event occurs before the [Security System](xref:113366) initializes the collection of non-secure Actions. You cannot manage these Actions in the [Denied Actions](xref:404633#action-permissions) tab in the UI. Handle this event and add Actions you want to mark non-secure to the @DevExpress.ExpressApp.Security.NonSecureActionsInitializingEventArgs.NonSecureActions collection.
