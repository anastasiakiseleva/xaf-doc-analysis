---
uid: DevExpress.ExpressApp.Validation.ActionValidationController
name: ActionValidationController
type: Class
summary: A [](xref:DevExpress.ExpressApp.Controller) descendant that allows [Actions](xref:112622) to be used as [Validation Contexts](xref:113008).
syntax:
  content: 'public class ActionValidationController : Controller, IModelExtender'
seealso:
- linkId: DevExpress.ExpressApp.Validation.ActionValidationController._members
  altText: ActionValidationController Members
---
The `ActionValidationController` extends the [Application Model](xref:112580) so that Actions can be used as Validation Contexts. The `ValidationContexts` property is added to the [!include[Node_Action](~/templates/node_action111373.md)] node. Additionally, the Controller adds a handler to the [ActionBase.Executing](xref:DevExpress.ExpressApp.Actions.ActionBase.Executing) event of each Action. In the event handler, the `ActionValidationController` invokes the [IRuleSet.ValidateAll](xref:DevExpress.Persistent.Validation.IRuleSet.ValidateAll*) method.

Generally, there is no need to inherit from the `ActionValidationController`, unless you want to disable the capability to use Actions as Validation Contexts. In this instance, inherit from the `ActionValidationController`, and override the protected `OnFrameAssigned` method, so that its body is empty.