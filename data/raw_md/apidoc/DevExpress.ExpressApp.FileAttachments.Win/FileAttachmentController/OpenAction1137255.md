---
uid: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController.OpenAction
name: OpenAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController)'s **Open** [Action](xref:112622).
syntax:
  content: public SimpleAction OpenAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object that is the **Open** Action.
seealso: []
---
The **Open** Action opens a file stored within the [](xref:DevExpress.Persistent.Base.IFileData) type property of the current object. A file is opened in an external application associated with the file's extension. The **IFileData** property that stores the file to be opened is specified via the [](xref:DevExpress.Persistent.Base.FileAttachmentAttribute) applied to the current persistent object declaration.

![FileAttach_OpenAction](~/images/fileattach_openaction117293.png)

To ascertain why the **Open** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

Information on the **Open** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).