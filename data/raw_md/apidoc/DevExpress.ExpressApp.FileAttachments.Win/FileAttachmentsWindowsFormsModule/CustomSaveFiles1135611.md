---
uid: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsWindowsFormsModule.CustomSaveFiles
name: CustomSaveFiles
type: Event
summary: Occurs when attached files are about to be saved to a hard disk.
syntax:
  content: public event EventHandler<CustomFileListOperationEventArgs> CustomSaveFiles
seealso: []
---
When the [FileAttachmentController](xref:113142)'s **SaveTo** [Action](xref:112622) is executed or the file data manager's (see [FileAttachmentsWindowsFormsModule.GetFileDataManager](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsWindowsFormsModule.GetFileDataManager(DevExpress.ExpressApp.XafApplication))) **SaveTo** method is invoked, a dialog prompting the end-user to choose the destination folder is invoked. You can override this behavior by handling the **CustomSaveFiles** event. After manually saving the attached files data, set the handler's **Handled** parameter to **true**, to suppress display of the default dialog.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.FileAttachments.Win;
using DevExpress.Persistent.Base;
//...
public class MyViewController : ViewController {
    FileAttachmentsWindowsFormsModule fileAttachmentsModule;
    protected override void OnActivated() {
        base.OnActivated();
        fileAttachmentsModule = Application.Modules.FindModule<FileAttachmentsWindowsFormsModule>();
        fileAttachmentsModule.CustomSaveFiles += fileAttachmentsModule_CustomSaveFiles;
    }
    void fileAttachmentsModule_CustomSaveFiles(object sender, CustomFileListOperationEventArgs e) {
        foreach (IFileData fileData in e.FileDataList) {
            //manually save attached files to a disk
            //...
        }
        e.Handled = true;
    }
    protected override void OnDeactivated() {
        fileAttachmentsModule.CustomSaveFiles -= fileAttachmentsModule_CustomSaveFiles;
        fileAttachmentsModule = null;
        base.OnDeactivated();
    }        
}
```
***