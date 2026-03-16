---
uid: DevExpress.ExpressApp.SystemModule.FilterController.SetFilterActionRefreshed
name: SetFilterActionRefreshed
type: Event
summary: Occurs after the Application Model's **Filters** node settings (the list of filters and the selected filter item) are applied to the [FilterController.SetFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.SetFilterAction) and before the current filter is applied to the List View's collection source.
syntax:
  content: public event EventHandler<EventArgs> SetFilterActionRefreshed
seealso: []
---
Handle the **SetFilterActionRefreshed** event to modify the list of filters and/or change the active filter. The list of filters is accessible using the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection of the **SetFilter** Action. If you need to add a custom filter to the collection, create a [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) instance and pass the criteria to the [ChoiceActionItem.Data](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Data) property. To select the active filter, use the [SingleChoiceAction.SelectedItem](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItem) property of the **SetFilter** Action.