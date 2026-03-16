---
uid: DevExpress.ExpressApp.FileAttachments.Win.IModelFileTypeFilters
name: IModelFileTypeFilters
type: Interface
summary: The FilteTypeFilters node defines file type filters (see [](xref:DevExpress.Persistent.Base.FileTypeFilterAttribute)) for properties whose type implements the **DevExpress.Persistent.Base.IFileData** interface or inherits from the **DevExpress.Persistent.BaseImpl.FileAttachmentBase** class.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(FileTypeFiltersNodesGenerator))]
    public interface IModelFileTypeFilters : IModelNode, IModelList<IModelFileTypeFilter>, IList<IModelFileTypeFilter>, ICollection<IModelFileTypeFilter>, IEnumerable<IModelFileTypeFilter>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.FileAttachments.Win.IModelFileTypeFilters._members
  altText: IModelFileTypeFilters Members
- linkId: "112579"
- linkId: "112580"
- linkId: "112781"
---
Via the context menu's **Add FileTypeFilters** menu item, you can add file type filters for an appropriate property. It will be supported in your application, as well as file type filters defined in code.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelFileTypeFilters** node represents a list of the [](xref:DevExpress.ExpressApp.FileAttachments.Win.IModelFileTypeFilter) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.FileAttachments.Win.FileTypeFiltersNodesGenerator) Nodes Generator.