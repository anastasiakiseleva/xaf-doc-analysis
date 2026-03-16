---
uid: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentListViewController
name: FileAttachmentListViewController
type: Class
summary: A [](xref:DevExpress.ExpressApp.ViewController) that allows users to create a new object with the selected [file attachment](xref:112781) via the **AddFromFile** [Action](xref:112622) and by dragging and dropping a file into the List Editor's control.
syntax:
  content: 'public class FileAttachmentListViewController : FileAttachmentControllerBase'
seealso:
- linkId: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentListViewController._members
  altText: FileAttachmentListViewController Members
---
The **FileAttachmentListViewController** Controller is activated in List Views when the [](xref:DevExpress.Persistent.Base.FileAttachmentAttribute) is applied to the current List View's object type. The [FileAttachmentAttribute.FileDataPropertyName](xref:DevExpress.Persistent.Base.FileAttachmentAttribute.FileDataPropertyName) parameter passed to the attribute specifies the [](xref:DevExpress.Persistent.Base.IFileData) type property that stores files added via the **AddFromFile** Action.

![FileAttach_AddFromFileAction](~/images/fileattach_addfromfileaction117296.png)

Additionally, an object with the associated file attachment can be created by dragging and dropping a file to the grid control. To provide this functionality, the **FileAttachmentListViewController** controller handles the [DragDrop](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.dragdrop) event of the List Editor's control.

![FileAttach_DragDrop](~/images/fileattach_dragdrop117295.png)

To customize the **FileAttachmentListViewController** controller behavior, you can access the **AddFromFile** Action exposed via the [FileAttachmentListViewController.AddFromFileAction](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentListViewController.AddFromFileAction) property and handle Action's  events, or override the following virtual methods.

| Method | Description |
|---|---|
| **AddFromFile** | Displays the [OpenFileDialog](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.openfiledialog) dialog to obtain the names of files to add. To get file names in a custom manner, override this method and pass file names list to the protected **AddFiles** method. |
| **GetFileTypesFilter** | Gets the file types filter passed to the [FileDialog.Filter](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.filedialog.filter#System_Windows_Forms_FileDialog_Filter) property of the [OpenFileDialog](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.openfiledialog) dialog displayed by the **AddFromFile** Action. |

Refer to the following topics for more information on file attachment properties:
* [File Attachment Properties](xref:113548)
* [Attach Files to Objects](xref:403288)
