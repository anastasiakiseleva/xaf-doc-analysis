---
uid: "403361"
title: 'Customize the File Attachments Module'
owner: Yekaterina Kiseleva
---
# Customize the File Attachments Module

## WinForms 
### Use Custom Logic to Open and Save Files
#### The CustomOpenFileWithDefaultProgram Event

To open an attached file, the module saves it to the operating system's temporary folder and passes the saved file to the operating system to open. The operating system searches for a default program and starts it. The module does not delete the saved file, because it cannot determine when a file becomes unnecessary. A user is responsible for the temporary folder's content.

Handle the [FileAttachmentsWindowsFormsModule.CustomOpenFileWithDefaultProgram](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsWindowsFormsModule.CustomOpenFileWithDefaultProgram) event to implement custom logic. Set the handler's **Handled** parameter to **true** to cancel the default behavior. To access the module, use the [XafApplication.Modules](xref:DevExpress.ExpressApp.XafApplication.Modules) property of your **WinApplication** class instance in a [custom Controller](xref:112621#implement-custom-controllers).

#### The CustomSaveFiles Event

The module invokes the **SaveFile** dialog to save an attached file. A user saves the file to a folder (the default folder is _MyDocuments_).
	
Handle the [FileAttachmentsWindowsFormsModule.CustomSaveFiles](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsWindowsFormsModule.CustomSaveFiles) event to implement a custom behavior. Set the handler's **Handled** parameter to **true** to cancel the default operations. To access the module, use the [XafApplication.Modules](xref:DevExpress.ExpressApp.XafApplication.Modules) property of your **WinApplication** class instance in a custom Controller.

### File Type Filters in the Open Dialog

In XAF WinForms applications, you can specify file type filters that appear in the **Files of type** box:

![FileTypeFilterAttribute](~/images/filetypefilterattribute116364.png)

You can use the @DevExpress.Persistent.Base.FileTypeFilterAttribute:
# [C#](#tab/tabid-csharp)

```csharp
[FileTypeFilter("Document files", 1, "*.txt", "*.doc")]
[FileTypeFilter("Image files", 2, "*.bmp", "*.png", "*.gif", "*.jpg")]
[FileTypeFilter("All files", 3, "*.*")]
public FileData Document {
   // ...
}
```
***

Alternatively, specify file type filters in the [Application Model](xref:112580). For more information, see the **Remarks** section of the following topic: @DevExpress.Persistent.Base.FileTypeFilterAttribute.

## ASP.NET Core Blazor 

`FileAttachmentsBlazorModule` uses the @DevExpress.Blazor.DxFileInput underlying component. Access it to customize file uploading options (for example, maximum file size or accepted file type).

[!include[](~/templates/dxfileinputmodel-customization.md)]

Alternatively, use the [FileAttachmentsOptions.DefaultMaxFileSize](xref:DevExpress.ExpressApp.FileAttachments.Blazor.FileAttachmentsOptions.DefaultMaxFileSize) property to change the maximum upload file size.

[!include[<options.DefaultMaxFileSize = 2097152;>](~/templates/AddFileAttachments_Blazor_example.md)]
