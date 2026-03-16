---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.UpdateSelectedItem(DevExpress.ExpressApp.ViewShortcut)
name: UpdateSelectedItem(ViewShortcut)
type: Method
summary: Changes the [ShowNavigationItemController.ShowNavigationItemAction](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction)'s selected item to the specified one.
syntax:
  content: public void UpdateSelectedItem(ViewShortcut currentViewShortcut)
  parameters:
  - id: currentViewShortcut
    type: DevExpress.ExpressApp.ViewShortcut
    description: A [](xref:DevExpress.ExpressApp.ViewShortcut) object that specifies a View which has a corresponding **ShowNavigationItemAction**'s item.
seealso:
- linkId: DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItem
---
This method is used by the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController) to change the **ShowNavigationItemAction**'s selected item to the appropriate one when the active [View](xref:112611) is changed. 
The **ShowNavigationItemController** tracks the active View changes, so you do not have to do any additional programming. However, if you need to perform custom actions when this method is called, or want to perform the change of the selected item in a custom way, handle the [ShowNavigationItemController.CustomUpdateSelectedItem](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomUpdateSelectedItem) event.