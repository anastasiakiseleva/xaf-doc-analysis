---
uid: DevExpress.ExpressApp.SystemModule.FilterController.SetFilterAction
name: SetFilterAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController)'s **SetFilter** Action.
syntax:
  content: public SingleChoiceAction SetFilterAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SingleChoiceAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) object representing the **Filter** Action.
seealso:
- linkId: "403238"
- linkId: "112992"
- linkId: "112991"
---
The **SetFilter** Action is intended to apply one of the predefined filters to the current List View:

In a Windows Forms application:

![Filters_Win_2](~/images/filters_win_2115951.png)

The predefined filters represent the elements of the **Filter** Action's `Items` collection (see [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items)). This collection's elements are generated using information from the [Application Model](xref:112580)'s [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **Filters** node.

To add filters to this node, use the [Model Editor](xref:112582), or do it in code. For details, refer to the following topics:
* [Filters Application Model Node](xref:112992)
* [](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute)

The **SetFilter** Action is active when the [](xref:DevExpress.ExpressApp.SystemModule.FilterController) is active. To ascertain why the **SetFilter** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively. To change the "visible" or "enabled" state of the **Filter** Action's items, use their [ChoiceActionItem.Active](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Active) and [ChoiceActionItem.Enabled](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Enabled) properties, respectively.

Information on the **SetFilter** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).
