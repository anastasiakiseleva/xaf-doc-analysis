---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomShowNavigationItem
name: CustomShowNavigationItem
type: Event
summary: Occurs when an end-user clicks a navigation item in the navigation control.
syntax:
  content: public event EventHandler<CustomShowNavigationItemEventArgs> CustomShowNavigationItem
seealso: []
---
This event is raised as a result of calling the **ShowNavigationItem** method, which serves as the **Navigation** Action's [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event handler. If you need to show a custom View or a separate form, handle this event. Use the handler's [CustomShowNavigationItemEventArgs.ActionArguments](xref:DevExpress.ExpressApp.SystemModule.CustomShowNavigationItemEventArgs.ActionArguments).**SelectedChoiceActionItem** parameter, to get the clicked item. Set the handler's **CustomShowNavigationItemEventArgs.Handled** parameter to **true** to avoid display of the default View set for the clicked item. To see an example, refer to the [How to: Create a New Object using the Navigation Control](xref:112920) topic.

As an alternative to this event, you can override the **ShowNavigationItem** method in the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController)'s descendant. 