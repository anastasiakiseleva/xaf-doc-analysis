---
uid: DevExpress.ExpressApp.XafApplication.CreateWindow(DevExpress.ExpressApp.TemplateContext,System.Collections.Generic.ICollection{DevExpress.ExpressApp.Controller},System.Boolean)
name: CreateWindow(TemplateContext, ICollection<Controller>, Boolean)
type: Method
summary: Creates a new [Window](xref:112608).
syntax:
  content: public Window CreateWindow(TemplateContext context, ICollection<Controller> controllers, bool isMain)
  parameters:
  - id: context
    type: DevExpress.ExpressApp.TemplateContext
    description: A [](xref:DevExpress.ExpressApp.TemplateContext) instance specifying the template context for the new Window. This parameter value is assigned to the [Frame.Context](xref:DevExpress.ExpressApp.Frame.Context) property.
  - id: controllers
    type: System.Collections.Generic.ICollection{DevExpress.ExpressApp.Controller}
    description: An **ICollection\<**[](xref:DevExpress.ExpressApp.Controller)**>** collection that contains the additional Controllers that must be activated for the new Window.
  - id: isMain
    type: System.Boolean
    description: '**true** if the newly created Window is main; otherwise, **false**.'
  return:
    type: DevExpress.ExpressApp.Window
    description: The created [](xref:DevExpress.ExpressApp.Window).
seealso: []
---
This method is intended for internal use.
[comment]: <> (<\!--This method creates a new Window, specifying the <see cref="P:DevExpress.ExpressApp.Frame.Context"/> and <see cref="P:DevExpress.ExpressApp.Window.IsMain"/> properties by the passed values. In addition, it registers the Controllers from the <%UrlDocument$112580#Application Model Basics.Application Model%> and the ones passes as the <i>controllers</i> parameter within the new Window, and then activates them. -->)