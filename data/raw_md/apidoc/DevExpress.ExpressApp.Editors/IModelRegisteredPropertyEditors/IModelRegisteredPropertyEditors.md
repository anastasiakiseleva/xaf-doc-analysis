---
uid: DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditors
name: IModelRegisteredPropertyEditors
type: Interface
summary: The PropertyEditors node represents a map of data types and Property Editors registered in an Application Model.
syntax:
  content: 'public interface IModelRegisteredPropertyEditors : IModelRegisteredViewItem, IModelNode, IModelList<IModelRegisteredPropertyEditor>, IList<IModelRegisteredPropertyEditor>, ICollection<IModelRegisteredPropertyEditor>, IEnumerable<IModelRegisteredPropertyEditor>, IEnumerable'
seealso:
- linkId: DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditors._members
  altText: IModelRegisteredPropertyEditors Members
- linkId: "112579"
- linkId: "112580"
---
You can add a child to this node via the context menu, to specify a Property Editor for your data type.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelRegisteredPropertyEditors** node represents a list of the [](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor) nodes.