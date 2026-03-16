---
uid: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController
name: FileAttachmentController
type: Class
summary: A [](xref:DevExpress.ExpressApp.ViewController) that provides [Actions](xref:112622) to open and save [file attachments](xref:112781) (**Open** and **SaveTo**).
syntax:
  content: 'public class FileAttachmentController : FileAttachmentControllerBase'
seealso:
- linkId: DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController._members
  altText: FileAttachmentController Members
- linkId: "112781"
---
The **FileAttachmentController** Controller is activated in List and Detail Views when the [](xref:DevExpress.Persistent.Base.FileAttachmentAttribute) is applied to the current View's object type. The [FileAttachmentAttribute.FileDataPropertyName](xref:DevExpress.Persistent.Base.FileAttachmentAttribute.FileDataPropertyName) parameter passed to the attribute specifies the [](xref:DevExpress.Persistent.Base.IFileData) type property that stores files to be opened or saved via the **FileAttachmentController**'s Actions. These Actions are:

* [FileAttachmentController.OpenAction](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController.OpenAction)
    
    ![FileAttach_OpenAction](~/images/fileattach_openaction117293.png)
* [FileAttachmentController.SaveToAction](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController.SaveToAction)
    
    ![FileAttach_SaveToAction](~/images/fileattach_savetoaction117294.png)