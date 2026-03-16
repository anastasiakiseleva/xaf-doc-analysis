---
uid: DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomAddActionControlToContainer
name: CustomAddActionControlToContainer
type: Event
summary: Occurs when an [Action](xref:112622) control is added to its [Action Container](xref:112610).
syntax:
  content: public event EventHandler<CustomAddActionControlEventArgs> CustomAddActionControlToContainer
seealso:
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/e1977/xaf-winforms-create-a-custom-action-type-and-a-custom-associated-control-barcheckitem
  altText: How to create a custom action type with a custom control (BarCheckItem), associated with it
---
Handle the **CustomAddActionControlToContainer** event to create a custom control and add it instead of the default one. Additionally, handle the [ActionControlsSiteController.CustomBindActionControlToAction](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomBindActionControlToAction) event to bind your custom control and Action settings.

If you want to customize the default control settings instead of creating a custom control, handle the [ActionControlsSiteController.CustomizeActionControl](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomizeActionControl) event instead.
