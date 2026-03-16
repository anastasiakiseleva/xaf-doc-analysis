---
uid: DevExpress.ExpressApp.SystemModule.LinkUnlinkController.AutoCommit
name: AutoCommit
type: Property
summary: Indicates whether to save changes made to the current List View's collection when the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) or [LinkUnlinkController.UnlinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.UnlinkAction) is executed.
syntax:
  content: public bool AutoCommit { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the changes made to the current collection property are saved to the database when the **Link** or **Unlink** Action is executed; otherwise, **false**.'
seealso: []
---
By default, this property is set to **false**.

This property is set to **true** in the [](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController)'s **WebLinkUnlinkController** descendant.