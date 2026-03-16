---
uid: DevExpress.ExpressApp.CreateCustomTemplateEventArgs
name: CreateCustomTemplateEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event.
syntax:
  content: 'public class CreateCustomTemplateEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.CreateCustomTemplateEventArgs._members
  altText: CreateCustomTemplateEventArgs Members
- linkId: "112618"
- linkId: "113706"
---
The **CreateCustomTemplateEventArgs** class declares properties specific to the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event designed to create a custom [Template](xref:112609), instead of a default one. To determine the context of the currently created Template, use the [CreateCustomTemplateEventArgs.Context](xref:DevExpress.ExpressApp.CreateCustomTemplateEventArgs.Context) property. Assign the newly created Template to the [CreateCustomTemplateEventArgs.Template](xref:DevExpress.ExpressApp.CreateCustomTemplateEventArgs.Template) property.
