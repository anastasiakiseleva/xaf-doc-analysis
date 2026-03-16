---
uid: DevExpress.ExpressApp.FileAttachments.Win.IModelCommonFileTypeFilters
name: IModelCommonFileTypeFilters
type: Interface
summary: Used to extend the [Application Model](xref:112580) with the FileTypeFilters node.
syntax:
  content: 'public interface IModelCommonFileTypeFilters : IModelNode'
seealso:
- linkId: DevExpress.ExpressApp.FileAttachments.Win.IModelCommonFileTypeFilters._members
  altText: IModelCommonFileTypeFilters Members
- linkId: "112579"
- linkId: "112580"
- linkId: "112781"
---
The **FileTypeFilters** node is added to the [](xref:DevExpress.ExpressApp.Model.IModelClass) and [](xref:DevExpress.ExpressApp.Model.IModelMember) nodes. The image below illustrates nodes exposed via the **FileTypeFilters** node.

![FileAttachmentProperties](~/images/fileattachmentproperties117301.png)

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases. The **IModelCommonFileTypeFilters** is used by the **FileAttachmentsWindowsFormsModule**, to extend the [](xref:DevExpress.ExpressApp.Model.IModelClass) and [](xref:DevExpress.ExpressApp.Model.IModelMember) interfaces. 