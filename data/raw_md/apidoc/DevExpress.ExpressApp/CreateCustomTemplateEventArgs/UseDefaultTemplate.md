---
uid: DevExpress.ExpressApp.CreateCustomTemplateEventArgs.UseDefaultTemplate
name: UseDefaultTemplate
type: Property
summary: Defines whether the application creates default templates on startup.
syntax:
  content: public bool UseDefaultTemplate { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true**, to create default templates on an application's startup; otherwise, **false**. The default value is **true**."
seealso: []
---
If you use [custom templates](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) and do not need default templates, set this property to **false** to speed up the application's startup. 