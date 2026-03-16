---
uid: "112781"
seealso:
- linkId: "113548"
- linkId: "112571"
- linkId: "112658"
- linkType: HRef
  linkId: 'xref:403288'
  altText: Attach Files to Objects (.NET)
- linkId: DevExpress.Persistent.Base.IFileData.LoadFromStream(System.String,System.IO.Stream)
- linkId: DevExpress.Persistent.Base.IFileData.SaveToStream(System.IO.Stream)
title: File Attachments (Store Custom Files)
owner: Ekaterina Kiseleva
---
# File Attachments (Store Custom Files)

XAF includes a **File Attachments** [module](xref:118046) and file data types for file management (upload, download, open, and save files). This module contains [Property Editors](xref:112612) and [Controllers](xref:112621) for the file data type.

[!demo[File Attachment Properties ASP.NET Core Blazor](https://demos.devexpress.com/XAF/featurecenter)]

[!video[XAF - Store file attachments in Dropbox instead of the database (XPO)](https://www.youtube.com/watch?v=lVfUeDj9T7U)]

## Supported Functionality

### ASP NET Core Blazor

![|File Attachment Properties Blazor|](~/images/file-attachment-properties-blazor.png)

[!include[dxfiledatapropertyeditor](~/templates/dxfiledatapropertyeditor.md)]

The default maximum file size is 4 MB.

`FileAttachmentsBlazorModule` uses the @DevExpress.Blazor.DxFileInput underlying component. Access it to customize file uploading options (for example, maximum file size or accepted file type).

[!include[dxfileinputmodel-customization](~/templates/dxfileinputmodel-customization.md)]

Alternatively, use the [FileAttachmentsOptions.DefaultMaxFileSize](xref:DevExpress.ExpressApp.FileAttachments.Blazor.FileAttachmentsOptions.DefaultMaxFileSize) property to change the default maximum size:

[!include[<options.DefaultMaxFileSize = 2097152;>](~/templates/AddFileAttachments_Blazor_example.md)]

### Windows Forms

![IFileDataWin](~/images/ifiledatawin115391.png)

Attach a File
:   When a user clicks the ellipsis button on the `FileDataPropertyEditor`, the application invokes the @System.Windows.Forms.OpenFileDialog dialog, which you can use to select an attached file.

Save an Attached File to a Disk
:   The `FileDataPropertyEditor` context menu contains the **SaveTo** [Action](xref:112622). The `FileAttachmentController.SaveFileData` method handles this Action's `Execute` event. You can override this method in the `FileAttachmentController` descendant to change the default logic.

Open an Attached File
:   The `FileDataPropertyEditor` context menu contains the **Open** Action. The `FileAttachmentController.Open` method handles this Action's `Execute` event. You can override this method in the `FileAttachmentController` descendant to change the default logic.

Detach a File
:   The `FileDataPropertyEditor` context menu contains the **ClearContent** Action. This Action's `Execute` event handler calls the property type's `Clear` method to clear file content. Override the [IFileData.Clear](xref:DevExpress.Persistent.Base.IFileData.Clear) method to implement your logic.

## File Attachments Module Components

The following table contains classes for different platforms:

{|
|-
! Platform 
! Module Class
! NuGet package
|-

| ASP.NET Core Blazor 
| `FileAttachmentsBlazorModule`
| **DevExpress.ExpressApp.FileAttachment.Blazor**
|-

| WinForms
| @DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsWindowsFormsModule
| **DevExpress.ExpressApp.FileAttachment.Win**
|} 

The File Attachments Module contains the following Property Editors to display file data properties in the UI:

* `DevExpress.ExpressApp.FileAttachment.Blazor.FileDataPropertyEditor`
* `DevExpress.ExpressApp.FileAttachment.Win.FileDataPropertyEditor`

## Add the File Attachments Module to an XAF Application

Install the appropriate platform-specific NuGet package and use one of the following techniques to add the File Attachments Module:

* [!include[ExtraModulesNote](~/templates/extramodulesnote1111180.md)]
* [!include[<@DevExpress.ExpressApp.Win.ApplicationBuilder.FileAttachmentsApplicationBuilderExtensions.AddFileAttachments(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsOptions})>,<ASP.NET Core Blazor/WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]
* Alternatively, you can add these Modules to the [ModuleBase.RequiredModuleTypes](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) collection of the platform-specific Module.

### Entity Framework Core-Based Application

The following additional step is required if you use Entity Framework Core:

1. Navigate to the _YourSolutionName.Module\BusinessObjects\YourSolutionNameDbContext.cs_ file and include the `FileData` entity in the data model:

    ```csharp
    using DevExpress.Persistent.BaseImpl.EF;
    // ...
    public class YourSolutionNameEFCoreDbContext : DbContext {
        // ...
        public DbSet<FileData> FileData { get; set; }
        // ...
    }
    ```

## Define a File Data Object and Storage

The file data object is a business class that implements the @DevExpress.Persistent.Base.IFileData interface. You can also use the built-in `FileData` class (XPO: the _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl\FileData.cs_ file, EF Core: the _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl.EF\FileData.cs_ file).

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;

namespace MySolution.Module.BusinessObjects {
    [FileAttachmentAttribute(nameof(File))]
    public class MyFileAttachment : BaseObject {
        // ...
        [ExpandObjectMembers(ExpandObjectMembers.Never)]
        [FileTypeFilter("DocumentFiles", 1, "*.txt", "*.doc")]
        [FileTypeFilter("AllFiles", 2, "*.*")]
        public virtual FileData File { get; set; }
    }
    public class FileData : BaseObject, IFileData {
        // ...
    }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;

namespace MySolution.Module.BusinessObjects {
    [FileAttachmentAttribute(nameof(File))]
    public class MyFileAttachment : BaseObject {
        // ...
        private FileData file;
        [Aggregated, ExpandObjectMembers(ExpandObjectMembers.Never)]
        [FileTypeFilter("DocumentFiles", 1, "*.txt", "*.doc")]
        [FileTypeFilter("AllFiles", 2, "*.*")]
        public FileData File {
            get { return file; }
            set { SetPropertyValue(nameof(File), ref file, value); }
        }
    }
    public class FileData : BaseObject, IFileData {
    // ...
    }
}    
```
***

Refer to the following help topic for more information on file data properties: [File Attachment Properties](xref:113548).

XAF stores attached files in a [database in a binary form](#read-compressed-files-in-the-filedata-database-table-from-external-non-xaf-net-applications). When you use the `DevExpress.Persistent.BaseImpl.FileData` type, the _gzip_ compression is applied to a file. Maximum file size is 2 GB. 

### Upload and Download File Attachments Programmatically (in Code)

Call the [IFileData.LoadFromStream](xref:DevExpress.Persistent.Base.IFileData.LoadFromStream(System.String,System.IO.Stream)) method to upload a file in code. To obtain the file, call the [IFileData.SaveToStream](xref:DevExpress.Persistent.Base.IFileData.SaveToStream(System.IO.Stream)) method. The `LoadFromStream` method does not require a full path to the file. This method accepts a file name as the first parameter.

### Examples 

[!example[How to: Store file attachments in the file system instead of the database](https://github.com/DevExpress-Examples/XAF_how-to-store-file-attachments-in-the-file-system-instead-of-the-database)]
[!example[How to: Store file attachments in Dropbox instead of the database](https://github.com/egarim/FileDataDropBox)]
[!example[How to: Use the File Attachment Module with a legacy database](https://github.com/DevExpress-Examples/xaf-how-to-use-the-file-attachment-module-with-a-legacy-database)]

> [!TIP]
>The following example implements a business class with a file data property and a file collection property: [How to: Implement File Data Properties](xref:112658).

## Read Compressed Files in the FileData Database Table from External Non-XAF .NET Applications

XAF stores attached files in a database in a binary form. Maximum file size is 2 GB. The XPO `DevExpress.Persistent.BaseImpl.FileData` type compresses files when it adds them to the database and decompresses files when they are accessed in the database. The `DevExpress.Persistent.Base.CompressionConverter` class (a custom [XPO Value Converter](xref:2053) class from the `DevExpress.Persistent.BaseImpl.Xpo` assembly) applies GZIP compression to files. For more information on the GZIP compression algorithm, refer to the source code at _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl.Xpo\CompressionUtils.cs_.

Use one of the following options to read compressed files in the `FileData` database table from external non-XAF .NET apps:

* If you can use XPO and `FileData` for data access, call the @DevExpress.Persistent.Base.IFileData.SaveToStream(System.IO.Stream) method.

* Otherwise, call the `CompressionConverter.ConvertFromStorageType` method as shown below:

    ```csharp
    using DevExpress.Data.Filtering;
    using DevExpress.Xpo;
    using SolutionName.Module.BusinessObjects;
    using System;
    using System.Data.SqlClient;
    using System.IO;
    using DevExpress.Persistent.Base;

    namespace SolutionName {
        class Program {
            static void Main(string[] args) {
                string cons = @"Integrated Security=SSPI;Pooling=false;Data Source=(localdb)\mssqllocaldb;Initial Catalog=XafDbWithFiles";
                SqlConnection conn = new SqlConnection(cons);
                conn.Open();
                SqlCommand sqlCmd = new SqlCommand("SELECT Content, FileName FROM FileData Where oid = 'B4C546BB-807D-4951-8443-50B800B6BE2D'", conn);
                using(SqlDataReader rdr = sqlCmd.ExecuteReader()) {
                    while(rdr.Read()) {
                        byte[] column1 =(byte[]) rdr["Content"];
                        var conv = new CompressionConverter();
                        byte[] decomp = (byte[]) conv.ConvertFromStorageType(column1);
                        string column2 = rdr["FileName"].ToString();
                        using(var fs = new FileStream("c:\\test\\1ok_"+column2, FileMode.CreateNew)) {
                            fs.Write(decomp, 0, decomp.Length);
                            fs.Flush();
                        }
                    }
                }
                conn.Close();
                conn.Dispose();
            }
        }
    }
    ```

    If you do not want to reference the `DevExpress.Persistent.BaseImpl.Xpo` assembly, copy the source code of the `CompressionConverter` class to your external non-XAF .NET project.

* If you do not need default file compression, you can create a custom @DevExpress.Persistent.Base.IFileData implementation and use it instead of the `DevExpress.Persistent.BaseImpl.FileData` type in your application. To do this, copy the source code of the `FileData.cs` class. You can find it in the _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl.Xpo_ folder. In the copied code, remove the `[ValueConverter(typeof(CompressionConverter))]` line from the `Content` property, and rename the class and namespaces.
