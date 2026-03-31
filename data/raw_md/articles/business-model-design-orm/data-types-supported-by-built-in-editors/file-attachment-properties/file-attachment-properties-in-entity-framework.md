---
uid: "113550"
title: File Attachment Properties in EF Core
seealso:  
- linkId: "117395"
---
# File Attachment Properties in EF Core

The example below illustrates how to implement [File Attachment Properties](xref:113548) in an EF Core class.

If your XAF application is EF-based, you can use the built-in **DevExpress.Persistent.BaseImpl.EF.FileData** class, which implements [](xref:DevExpress.Persistent.Base.IFileData). (File Attachment Property Editors are designed for **IFileData** type properties.) The example below illustrates how to implement [File Attachment Properties](xref:113548) in an entity class.

# [C#](#tab/tabid-csharp)

```csharp
[ExpandObjectMembers(ExpandObjectMembers.Never)]
[FileTypeFilter("DocumentFiles", 1, "*.txt", "*.doc")]
[FileTypeFilter("AllFiles", 2, "*.*")]
public virtual FileData File { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

Refer to the [](xref:DevExpress.Persistent.Base.FileTypeFilterAttribute) description for details on the use of this attribute.

> [!NOTE]
> Use the [](xref:DevExpress.Persistent.Base.FileAttachmentAttribute) attribute to enable Actions that manage file attachments, in addition to the Property Editor functionality.