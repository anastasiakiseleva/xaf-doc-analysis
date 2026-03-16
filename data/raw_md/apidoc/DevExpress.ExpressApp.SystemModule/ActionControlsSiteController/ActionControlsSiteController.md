---
uid: DevExpress.ExpressApp.SystemModule.ActionControlsSiteController
name: ActionControlsSiteController
type: Class
summary: The [Controllers](xref:112621) that manage binding between [Actions](xref:112622) and their controls in [Templates](xref:112609) that support the **IActionControlsSite** interface.
syntax:
  content: 'public class ActionControlsSiteController : Controller, IModelExtender'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ActionControlsSiteController._members
  altText: ActionControlsSiteController Members
- linkId: "113183"
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/e1977/xaf-winforms-create-a-custom-action-type-and-a-custom-associated-control-barcheckitem
  altText: How to create a custom action type with a custom control (BarCheckItem), associated with it
---
The **ActionControlsSiteController** Controller uses mapping specified in the **ActionDesign** | **ActionToContainerMapping** [Application Model](xref:112579) node to place Action controls to the Action Containers. You can customize this Controller behavior by handling the following events.

* [ActionControlsSiteController.CustomAddActionControlToContainer](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomAddActionControlToContainer)
* [ActionControlsSiteController.CustomBindActionControlToAction](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomBindActionControlToAction)
* [ActionControlsSiteController.CustomizeActionControl](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomizeActionControl)
* [ActionControlsSiteController.CustomizeContainerActions](xref:DevExpress.ExpressApp.SystemModule.ActionControlsSiteController.CustomizeContainerActions)
