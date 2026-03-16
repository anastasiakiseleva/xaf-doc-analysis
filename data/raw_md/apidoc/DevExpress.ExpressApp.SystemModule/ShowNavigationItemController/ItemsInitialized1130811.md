---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ItemsInitialized
name: ItemsInitialized
type: Event
summary: Occurs after the **Items** collection of the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController)'s **ShowNavigationItem** Action has been populated.
syntax:
  content: public event EventHandler<EventArgs> ItemsInitialized
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomInitializeItems
---
This event is raised as a result of calling the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController)'s **InitializeItems** method. Handle this event to access a particular element of the **ShowNavigationItem** Action's **Items** collection, and modify it.