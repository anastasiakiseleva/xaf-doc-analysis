---
uid: DevExpress.ExpressApp.XafApplication.CreateWindow(DevExpress.ExpressApp.TemplateContext,System.Collections.Generic.ICollection{DevExpress.ExpressApp.Controller},System.Boolean,System.Boolean)
name: CreateWindow(TemplateContext, ICollection<Controller>, Boolean, Boolean)
type: Method
summary: Creates a new [Window](xref:112608).
syntax:
  content: public Window CreateWindow(TemplateContext context, ICollection<Controller> controllers, bool createAllControllers, bool isMain)
  parameters:
  - id: context
    type: DevExpress.ExpressApp.TemplateContext
    description: A [](xref:DevExpress.ExpressApp.TemplateContext) instance specifying the template context for the new Window. This parameter value is assigned to the [Frame.Context](xref:DevExpress.ExpressApp.Frame.Context) property.
  - id: controllers
    type: System.Collections.Generic.ICollection{DevExpress.ExpressApp.Controller}
    description: An **ICollection\<**[](xref:DevExpress.ExpressApp.Controller)**>** collection that contains the additional Controllers that must be activated for the new Window.
  - id: createAllControllers
    type: System.Boolean
    description: '**true** if all Controllers from the [Application Model](xref:112580) must be created; otherwise, **false**.'
  - id: isMain
    type: System.Boolean
    description: '**true** if the newly created Window is main; otherwise, **false**.'
  return:
    type: DevExpress.ExpressApp.Window
    description: The created [](xref:DevExpress.ExpressApp.Window).
seealso: []
---
This method is intended for internal use.