---
uid: DevExpress.Persistent.Base.ISupportFullName
name: ISupportFullName
type: Interface
summary: Declares the property used to store a full path to the file specified by the object which implements the [](xref:DevExpress.Persistent.Base.IFileData) interface.
syntax:
  content: public interface ISupportFullName
seealso:
- linkId: DevExpress.Persistent.Base.ISupportFullName._members
  altText: ISupportFullName Members
---
You can implement the `ISupportFullName` interface in your custom class that supports [](xref:DevExpress.Persistent.Base.IFileData) to access the file's full path. XAF assigns the file's full path to the [ISupportFullName.FullName](xref:DevExpress.Persistent.Base.ISupportFullName.FullName) property before the [IFileData.LoadFromStream](xref:DevExpress.Persistent.Base.IFileData.LoadFromStream(System.String,System.IO.Stream)) method is called.

> [!NOTE]
> In ASP.NET Core Blazor applications, the `FullName` property stores the file's name only, because a web browser does not allow reading the uploaded file full path for security reasons (see [UploadedFile.FileName](xref:DevExpress.Web.UploadedFile.FileName)).


You can implement `ISupportFullName` in your custom FileData object:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel.DataAnnotations;
// ...
public class FileDataEx : FileData, ISupportFullName {
    private string fullName;
    [ModelDefault("AllowEdit", "False")]
    public virtual string FullName {
        get { return fullName; }
        set { SetPropertyValue(ref fullName, value); }
    }
}
public class DemoObject : BaseObject {
    public virtual FileDataEx File { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
// ...
public class FileDataEx : FileData, ISupportFullName {
    public FileDataEx(Session session) : base(session) { }
    private string fullName;
    [ModelDefault("AllowEdit", "False")]
    public string FullName {
        get { return fullName; }
        set { SetPropertyValue(nameof(FullName), ref fullName, value); }
    }
}
[DefaultClassOptions]
public class DemoObject : BaseObject {
    public DemoObject(Session session)
        : base(session) { }
    private FileDataEx file;
    public FileDataEx File {
        get { return file; }
        set { SetPropertyValue(nameof(File), ref file, value); }
    }
}
```
***