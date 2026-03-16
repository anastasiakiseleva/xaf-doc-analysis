---
uid: DevExpress.Persistent.Base.FileAttachmentAttribute
name: FileAttachmentAttribute
type: Class
summary: Applied to business classes that expose a property of the [](xref:DevExpress.Persistent.Base.IFileData) type. Activates Controllers that manage [file attachments](xref:112781) for the target business class. Specifies a property that stores a file attachment.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface, Inherited = true)]
    public class FileAttachmentAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.FileAttachmentAttribute._members
  altText: FileAttachmentAttribute Members
- linkId: DevExpress.Persistent.Base.FileTypeFilterAttribute
---
Use this attribute to activate the following Controllers that provide Actions to manage [file attachments](xref:112781):

<!--TODO: add Blazor information if necessary -->

* [](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController) (Windows Forms)
* [](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentListViewController) (Windows Forms)

The **FileAttachmentAttribute** attribute takes a single parameter - the [FileAttachmentAttribute.FileDataPropertyName](xref:DevExpress.Persistent.Base.FileAttachmentAttribute.FileDataPropertyName). The parameter specifies the property of a [](xref:DevExpress.Persistent.Base.IFileData) type to be used by the Controllers listed above. The snippet below illustrate the **FileAttachmentAttribute** attribute usage.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[FileAttachmentAttribute(nameof(File))]
public class MyFileAttachment : BaseObject {
    public virtual FileData File { get; set; }
}

public class FileData : BaseObject, IFileData {
    // ...
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[FileAttachmentAttribute(nameof(File))]
public class MyFileAttachment : BaseObject {
    // ...
    private FileData file;
    public FileData File {
        get { return file; }
        set { SetPropertyValue(nameof(File), ref file, value); }
    }
}
public class FileData : BaseObject, IFileData {
   // ...
}
```
***

As an alternative to using the **FileAttachmentAttribute**, you can inherit from the **FileAttachmentBase** class. It has the **FileAttachmentAttribute** applied, and exposes the **File** property to store file attachments.

> [!NOTE]
> It is not recommended to use the [DataView](xref:118452) mode with the **FileAttachmentAttribute**. In this mode, a separate request to database is made for each focused List View record.