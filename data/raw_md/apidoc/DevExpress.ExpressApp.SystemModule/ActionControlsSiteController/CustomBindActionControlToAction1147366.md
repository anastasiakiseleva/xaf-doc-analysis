---
uid: DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomBindActionControlToAction
name: CustomBindActionControlToAction
type: Event
summary: Occurs when an [Action](xref:112622) control is bound to Action settings.
syntax:
  content: public event EventHandler<CustomBindEventArgs> CustomBindActionControlToAction
seealso:
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/e1977/xaf-winforms-create-a-custom-action-type-and-a-custom-associated-control-barcheckitem
  altText: How to create a custom action type with a custom control (BarCheckItem), associated with it
---
Handle the **CustomBindActionControlToAction** event together with the [ActionControlsSiteController.CustomAddActionControlToContainer](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomAddActionControlToContainer) event when you create a custom control for a certain Action. To specify Action binding, inherit the **ActionBinding** class and pass an instance of your descendant to the **e.Binding** parameter.
