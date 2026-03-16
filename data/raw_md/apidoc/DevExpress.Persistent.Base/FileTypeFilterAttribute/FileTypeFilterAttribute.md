---
uid: DevExpress.Persistent.Base.FileTypeFilterAttribute
name: FileTypeFilterAttribute
type: Class
summary: Specifies a file type filter in the **Open** dialog's "Files of type" box. You can apply this attribute to file data business classes, interfaces, and their properties in ASP.NET Core Blazor and Windows Forms applications.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Property | AttributeTargets.Interface, AllowMultiple = true, Inherited = false)]
    public class FileTypeFilterAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.FileTypeFilterAttribute._members
  altText: FileTypeFilterAttribute Members
- linkId: DevExpress.Persistent.Base.FileAttachmentAttribute
---
The [File Attachments module](xref:112781) supplies [File Property Editors](xref:113548). XAF uses these Property Editors if the corresponding property type implements the `DevExpress.Persistent.Base.IFileData` interface. To load files, the `FileDataPropertyEditor` displays the **Open** dialog. The `FileTypeFilter` attribute specifies a file type filter that appears in the **Open** dialog's "Files of type" box. You can apply this attribute to a file data property if its type implements the `IFileData` interface or inherits from the `DevExpress.Persistent.BaseImpl.FileAttachmentBase` class. If you apply the attribute to a class or interface, then it affects the property specified by the [FileAttachmentAttribute.FileDataPropertyName](xref:DevExpress.Persistent.Base.FileAttachmentAttribute.FileDataPropertyName) attribute parameter.

The `FileTypeFilter` attribute has two constructors. One constructor accepts two parameters: a filter description and a list of associated file extensions. Another constructor requires an additional parameter that allows you to arrange type filter strings in the required order if you apply multiple `FileTypeFilter` attributes.

File type filters defined via the `FileTypeFilter` attribute are reflected by the [Application Model](xref:112580). A `FileTypeFilters` child node appears in the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node that corresponds to the target file data property. A **FileTypeFilters** child node contains **FileTypeFilter** child nodes. Each **FileTypeFilter** child node represents a single file type filter, and a **FileTypeFilter** contains **Extension** child nodes that define file extensions. You can define new and modify existing file type filters by editing the **FileTypeFilters** node in the [Model Editor](xref:112582).

![FileTypesFilter_ME](~/images/filetypesfilter_me129555.png)

The following code snippet demonstrates how to use the `FileTypeFilter` attribute:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

public class CustomClass : BaseObject {
    [FileTypeFilter("Document files", 1, "*.txt", "*.doc")]
    [FileTypeFilter("Image files", 2, "*.bmp", "*.png", "*.gif", "*.jpg")]
    [FileTypeFilter("All files", 3, "*.*")]
    public virtual FileData Document { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;

public class CustomClass : BaseObject {
    private FileData document;

    public CustomClass(Session session) : base(session) { }

    [FileTypeFilter("Document files", 1, "*.txt", "*.doc")]
    [FileTypeFilter("Image files", 2, "*.bmp", "*.png", "*.gif", "*.jpg")]
    [FileTypeFilter("All files", 3, "*.*")]
    public FileData Document {
        get { return document; }
        set { SetPropertyValue(nameof(Document), ref document, value); }
    }
}
```
***

> [!TIP]
> If you have no access to the business class source to apply the attribute (for example, when you use a built-in `FileAttachmentBase`), use the Application Model instead.

The following image shows the resulting **Open** dialog:

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor FileTypeFilterAttribute, DevExpress](~/images/xaf-blazor-filetypefilterattribute-devexpress.png)

Windows Forms
:   ![XAF Windows Forms FileTypeFilterAttribute, DevExpress](~/images/filetypefilterattribute116364.png)

> [!NOTE]
> Currently, only XAF ASP.NET Core Blazor and Windows Forms applications support the `FileTypeFilterAttribute`.  
>
> ASP.NET Core Blazor functionality is limited by modern browser capabilities:
> 1. All type filters are collected into a single filter list. For more information, refer to the following document: https://www.w3schools.com/TAGS/att_input_accept.asp.
> 2. You cannot remove the "All Files (\*.\*)" option. You can only specify the [`DxUpload.AllowedFileExtensions`](xref:DevExpress.Blazor.DxUpload.AllowedFileExtensions) property to verify file extensions on the client side.

For more information about the **File Attachments** module, refer to the following topic: [File Attachments Module Overview](xref:112781).
