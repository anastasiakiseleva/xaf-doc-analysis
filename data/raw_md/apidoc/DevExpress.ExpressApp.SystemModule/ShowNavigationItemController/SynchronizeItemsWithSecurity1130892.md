---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.SynchronizeItemsWithSecurity
name: SynchronizeItemsWithSecurity()
type: Method
summary: Makes the [ShowNavigationItemController.ShowNavigationItemAction](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction)'s items disabled if the [Security System](xref:113366) prohibits reading and navigating to the object type associated with the items.
syntax:
  content: public void SynchronizeItemsWithSecurity()
seealso:
- linkId: DevExpress.ExpressApp.Security.ObjectAccess
- linkId: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ItemsInitialized
---
Use this method when customizing the **Items** collection of the **ShowNavigationItemAction**. This method will disable the items that are not allowed for the current user. The items are allowed when the user has two permissions:

* To navigate to the Views associated with the items.
* To read the objects represented by the Views that are associated with the items.