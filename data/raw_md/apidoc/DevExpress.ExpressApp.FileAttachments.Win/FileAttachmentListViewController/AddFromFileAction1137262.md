---
uid: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentListViewController.AddFromFileAction
name: AddFromFileAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentListViewController)'s **AddFromFile** [Action](xref:112622).
syntax:
  content: public SimpleAction AddFromFileAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object that is the **AddFromFile** Action.
seealso: []
---
The **AddFromFile** Action invokes a [OpenFileDialog](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.openfiledialog) dialog to obtain a file name to be added (multiple files can also be selected). For each selected file, a new object is created and its  [](xref:DevExpress.Persistent.Base.IFileData) type property is initialized with the selected file. The **IFileData** property that stores a file is specified via the [](xref:DevExpress.Persistent.Base.FileAttachmentAttribute) applied to the current persistent object declaration.

![FileAttach_AddFromFileAction](~/images/fileattach_addfromfileaction117296.png)

To ascertain why the **AddFromFile** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

Information on the **AddFromFile** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).

Refer to the following topics for more information on file attachment properties:
* [File Attachment Properties](xref:113548)
* [Attach Files to Objects](xref:403288)
