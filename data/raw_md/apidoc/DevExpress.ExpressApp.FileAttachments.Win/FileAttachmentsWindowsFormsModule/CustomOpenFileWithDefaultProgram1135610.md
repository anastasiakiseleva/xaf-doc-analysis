---
uid: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsWindowsFormsModule.CustomOpenFileWithDefaultProgram
name: CustomOpenFileWithDefaultProgram
type: Event
summary: Occurs prior to opening an attached file via its associated program.
syntax:
  content: public event EventHandler<CustomFileOperationEventArgs> CustomOpenFileWithDefaultProgram
seealso: []
---
When the [FileAttachmentController](xref:113142)'s **Open** [Action](xref:112622) is executed, a selected file is saved to the operating system's temporary folder, and then passed to the operating system, to be opened. The operating system then searches for an associated program and opens the file. The [](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsWindowsFormsModule) does not delete the saved file, because it cannot determine when the file is no longer used. So, the end-user needs to periodically clean the temporary folder's content. You can override this behavior by handling the **CustomOpenFileWithDefaultProgram** event. After opening an attached file using the associated program and performing necessary cleanup, set the handler's **Handled** parameter to **true**, to cancel the default file opening routine.

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
        fileAttachmentsModule.CustomOpenFileWithDefaultProgram += OnCustomOpenFile;
    }
    void OnCustomOpenFile(object sender, CustomFileOperationEventArgs e) {
        //manually open the e.FileData file and perform necessary cleanup
        //...            
        e.Handled = true;
    }        
    protected override void OnDeactivated() {
        fileAttachmentsModule.CustomOpenFileWithDefaultProgram -= OnCustomOpenFile;
        fileAttachmentsModule = null;
        base.OnDeactivated();
    }        
}
```
***