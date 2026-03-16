---
uid: "113549"
seealso: []
title: File Attachment Properties in XPO
owner: Ekaterina Kiseleva
---
# File Attachment Properties in XPO

Properties of the [](xref:DevExpress.Persistent.Base.IFileData) type are named [file attachment properties](xref:113548) and use the File Attachment [Property Editors](xref:112612). This topic describes the XPO-oriented ways to add a file attachment property in an persistent class.

## Add a FileData Property Explicitly

In this section, the code snippet demonstrates an example of a `FileData` property to be added in your persistent class.  Refer to the following topics for details on the attributes used in this example.

* [](xref:DevExpress.Xpo.AggregatedAttribute)
* [](xref:DevExpress.Persistent.Base.ExpandObjectMembersAttribute)
* [](xref:DevExpress.Persistent.Base.FileTypeFilterAttribute)

# [C#](#tab/tabid-csharp)

```csharp
private FileData document;
[Aggregated, ExpandObjectMembers(ExpandObjectMembers.Never)]
[FileTypeFilter("DocumentFiles", 1, "*.txt", "*.doc")]
[FileTypeFilter("AllFiles", 2, "*.*")]
public FileData Document {
    get { return document; }
    set { SetPropertyValue(nameof(Document), ref document, value); }
}
```

***

You can use the [](xref:DevExpress.Persistent.Base.FileAttachmentAttribute) to enable Actions that manage file attachments in addition to the Property Editor functionality.

## Add a FileData Property by Inheriting the FileAttachmentBase Class

The built-in abstract `FileAttachmentBase` class from the [Business Class Library](xref:112571) is decorated with the [](xref:DevExpress.Persistent.Base.FileAttachmentAttribute) and has the `File` property of the `FileData` type. To use the file attachment property, you can create a custom descendant of this class.

See an example of using this approach in the [Attach Files to Objects](xref:403288) topic.

## Add XPCollection\<FileAttachment> Type Properties

You can add a property of the `XPCollection\<FileAttachment>` type where `FileAttachment` is a class that uses the `FileAttachment` attribute (for example, the `FileAttachmentBase` class). In this case, a List Property Editor with the `FileAttachment` object collection will be displayed in a UI.

This Property Editor will be accompanied by the special Controller's Actions in WinForms applications:

- The `FileAttachmentController` - the **Open** and **SaveTo** Actions.
- The `FileAttachmentListViewController` - the **AddFromFile** Action.

Both these Controllers are activated only for Views with an object(s) that uses the `FileAttachment` attribute (List Views in the case of a `FileAttachmentListViewController`).

> [!NOTE]
> To add file collections to a business class, you can implement the `XPCollection\<IFileData>` type properties instead of the `XPCollection\<FileAttachment>` type properties (`FileAttachment` is a class that uses the `FileAttachment` attribute). In this case, these properties will be displayed by the List Property Editor as well. However, the Actions listed above will not be displayed, because the special Controllers will not be activated.

## Add a Custom File Attachment Property by Implementing the IFileData Interface
You can create your own `IFileData` implementation when required. To see an example, refer to the `FileData` class sources at _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Persistent\DevExpress.Persistent.BaseImpl.EFCore\FileData.cs_, or to the following articles: 
* [How to: Store file attachments in the file system instead of the database](https://supportcenter.devexpress.com/ticket/details/e965/how-to-store-file-attachments-in-the-file-system-instead-of-the-database-xpo-and-ef-core) 
* [How to: Store file attachments in Dropbox instead of the database](https://github.com/egarim/FileDataDropBox)([video](https://www.youtube.com/watch?v=lVfUeDj9T7U))
* [How to: Use the File Attachment Module with a legacy database](https://github.com/DevExpress-Examples/xaf-how-to-use-the-file-attachment-module-with-a-legacy-database)
