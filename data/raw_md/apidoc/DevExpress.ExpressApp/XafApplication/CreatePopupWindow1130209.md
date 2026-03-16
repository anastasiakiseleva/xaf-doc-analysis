---
uid: DevExpress.ExpressApp.XafApplication.CreatePopupWindow(DevExpress.ExpressApp.TemplateContext,System.String,System.Boolean,DevExpress.ExpressApp.Controller[])
name: CreatePopupWindow(TemplateContext, String, Boolean, Controller[])
type: Method
summary: Creates a new pop-up [Window](xref:112608).
syntax:
  content: public Window CreatePopupWindow(TemplateContext context, string viewId, bool createAllControllers, params Controller[] controllers)
  parameters:
  - id: context
    type: DevExpress.ExpressApp.TemplateContext
    description: A [](xref:DevExpress.ExpressApp.TemplateContext) instance specifying the template context for the new pop-up Window. This parameter value is assigned to the [Frame.Context](xref:DevExpress.ExpressApp.Frame.Context) property.
  - id: viewId
    type: System.String
    description: The identifier of the View that will be displayed by the new pop-up Window.
  - id: createAllControllers
    type: System.Boolean
    description: '**true** if all Controllers from the [Application Model](xref:112580) must be created; otherwise, **false**.'
  - id: controllers
    type: DevExpress.ExpressApp.Controller[]
    description: An array of [](xref:DevExpress.ExpressApp.Controller) objects that contains the additional Controllers that must be activated for the new pop-up Window.
  return:
    type: DevExpress.ExpressApp.Window
    description: The created pop-up [](xref:DevExpress.ExpressApp.Window).
seealso: []
---
This method is intended for internal use.