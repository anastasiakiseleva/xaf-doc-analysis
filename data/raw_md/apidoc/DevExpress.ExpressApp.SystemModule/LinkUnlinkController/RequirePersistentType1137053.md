---
uid: DevExpress.ExpressApp.SystemModule.LinkUnlinkController.RequirePersistentType
name: RequirePersistentType
type: Property
summary: Specifies whether or not the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) and [LinkUnlinkController.UnlinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.UnlinkAction) actions are active for persistent objects only.
syntax:
  content: |-
    [Browsable(false)]
    [DefaultValue(true)]
    public bool RequirePersistentType { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the **Link** and **Unlink** actions are active for persistent objects only; otherwise - **false**.'
seealso: []
---
Set this property to **false** to enable Link/Unlink actions for a [non-persistent objects](xref:116516). In this case, handle the [LinkUnlinkController.CustomCreateLinkView](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.CustomCreateLinkView) event and manually create a [](xref:DevExpress.ExpressApp.ListView) object that will be shown by a **Link** and **Unlink** action.