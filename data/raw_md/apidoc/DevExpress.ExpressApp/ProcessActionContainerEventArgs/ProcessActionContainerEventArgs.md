---
uid: DevExpress.ExpressApp.ProcessActionContainerEventArgs
name: ProcessActionContainerEventArgs
type: Class
summary: Represents arguments passed to the [Frame.ProcessActionContainer](xref:DevExpress.ExpressApp.Frame.ProcessActionContainer) event.
syntax:
  content: 'public class ProcessActionContainerEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.ProcessActionContainerEventArgs._members
  altText: ProcessActionContainerEventArgs Members
---
The **ProcessActionContainer** event occurs when a [Template](xref:112609) is assigned to a [](xref:DevExpress.ExpressApp.Frame), and allows you to customize the Template's [Action Containers](xref:112610). The **ProcessActionContainerEventArgs** class exposes a single [ProcessActionContainerEventArgs.ActionContainer](xref:DevExpress.ExpressApp.ProcessActionContainerEventArgs.ActionContainer) property, which specifies the Action Container currently being processed.