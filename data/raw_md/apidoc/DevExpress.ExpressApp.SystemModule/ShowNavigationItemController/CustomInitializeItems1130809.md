---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomInitializeItems
name: CustomInitializeItems
type: Event
summary: Raised before generating the **Items** collection of the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController)'s **ShowNavigationItem** Action.
syntax:
  content: public event EventHandler<HandledEventArgs> CustomInitializeItems
seealso: []
---
This event is raised as a result of calling the **InitializeItems** method when the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController) is activated. If you need to populate the **ShowNavigationItem** Action's **Items** collection in a custom manner, handle this event. Set the handler's **Handled** parameter, to avoid populating the collection in the default manner. If you leave the **Handled** parameter set to **false**, the collection will be populated using information from the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems) node.

To access the **ShowNavigationItem** Action's **Items** collection after it has been populated, handle the [ShowNavigationItemController.ItemsInitialized](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ItemsInitialized) event.