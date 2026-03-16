---
uid: DevExpress.ExpressApp.CustomizeTemplateEventArgs
name: CustomizeTemplateEventArgs
type: Class
summary: Arguments passed to the [XafApplication.CustomizeTemplate](xref:DevExpress.ExpressApp.XafApplication.CustomizeTemplate) event.
syntax:
  content: 'public class CustomizeTemplateEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.CustomizeTemplateEventArgs._members
  altText: CustomizeTemplateEventArgs Members
---
The **CustomizeTemplateEventArgs** class declares properties specific to the [XafApplication.CustomizeTemplate](xref:DevExpress.ExpressApp.XafApplication.CustomizeTemplate) event which is designed to customize a [Template](xref:112609) after it has been created. To access this Template, use the [CustomizeTemplateEventArgs.Template](xref:DevExpress.ExpressApp.CustomizeTemplateEventArgs.Template) property. To determine whether the Template is in the required context, use the [CustomizeTemplateEventArgs.Context](xref:DevExpress.ExpressApp.CustomizeTemplateEventArgs.Context) property.