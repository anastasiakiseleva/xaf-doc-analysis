---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.SynchronizeItemsWithSecurityMode
name: SynchronizeItemsWithSecurityMode
type: Property
summary: Specifies whether all navigation items or the selected item must be synchronized with the security permissions when an end-user clicks an item.
syntax:
  content: |-
    [Browsable(false)]
    [DefaultValue(SynchronizeItemsWithSecurityMode.SelectedItem)]
    public SynchronizeItemsWithSecurityMode SynchronizeItemsWithSecurityMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SystemModule.SynchronizeItemsWithSecurityMode
    description: A **SynchronizeItemsWithSecurityMode** enumeration value specifying the mode in which to check security permissions for the current user.
seealso: []
---
When an end-user clicks a navigation item, the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController) checks whether they has permissions to navigate to and read the data displayed by this item. Dependent on the result, the item is enabled/disabled, if it has been active; or activated, if it has been inactive. You can set how many items must be checked when an end-user clicks an item. Set this property to **SelectedItem**, if you want only the selected item to be checked. Set this property to **AllItems**, if you want all items to be checked each time an end-user clicks an item. By default, this property is set to **SelectedItem**.