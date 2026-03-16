---
uid: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController.SaveToAction
name: SaveToAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController)'s **SaveTo** [Action](xref:112622).
syntax:
  content: public SimpleAction SaveToAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object that is the **SaveTo** Action.
seealso: []
---
The **SaveTo** Action saves a file stored within the [](xref:DevExpress.Persistent.Base.IFileData) type property of the current object to the selected location in the file system. If multiple objects are selected, all of them are saved to the selected folder. The **IFileData** property that stores a file to be saved is specified via the [](xref:DevExpress.Persistent.Base.FileAttachmentAttribute) applied to the current persistent object declaration.

![FileAttach_SaveToAction](~/images/fileattach_savetoaction117294.png)

To ascertain why the **SaveTo** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

Information on the **SaveTo** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).