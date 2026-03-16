---
uid: DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.ChangeVariantAction
name: ChangeVariantAction
type: Property
summary: Gets a [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) used to change [View](xref:112611) variants.
syntax:
  content: public SingleChoiceAction ChangeVariantAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SingleChoiceAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) object representing the [Action](xref:112622) used to change [View](xref:112611) variants.
seealso:
- linkId: "113011"
---
**ChangeVariantAction** is the **SingleChoiceAction** Action that allows users to select a View variant to be displayed within the current Window (Frame). This Action has the `View` caption and the `ChangeVariant` ID.

In a Windows Forms application:

![ViewChangeActionInWindow](~/images/viewchangeactioninwindow115369.png)

Predefined items displayed in the drop-down list are specified by the **Views** | **View** | **Variants** node of the [Application Model](xref:112580). The action is visible if there are two or more variants available for a current varied View. This action can be customized via the **ActionDesign** | **Actions** | **View** node.

To see why the **ChangeVariant** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.