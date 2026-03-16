---
uid: DevExpress.ExpressApp.Frame.SetTemplate(DevExpress.ExpressApp.Templates.IFrameTemplate)
name: SetTemplate(IFrameTemplate)
type: Method
summary: Sets a specified [Template](xref:112609) for the current [](xref:DevExpress.ExpressApp.Frame).
syntax:
  content: public void SetTemplate(IFrameTemplate val)
  parameters:
  - id: val
    type: DevExpress.ExpressApp.Templates.IFrameTemplate
    description: An object that implements the [](xref:DevExpress.ExpressApp.Templates.IFrameTemplate) interface to be used for the current [](xref:DevExpress.ExpressApp.Frame).
seealso:
- linkId: "112696"
- linkId: "112618"
---
Use this method to set a Template specified by the _template_ parameter for the current [](xref:DevExpress.ExpressApp.Frame). After setting the Template, the [Frame.TemplateChanged](xref:DevExpress.ExpressApp.Frame.TemplateChanged) event is raised. Handle this event to customize the Template that has been set for the current Frame.

If the current Frame contains a [View](xref:112611), the **SetTemplate** method sets this View for the new Template.

> [!NOTE]
> To set your own Template, it is recommended that you handle the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event instead of using the **SetTemplate** method.