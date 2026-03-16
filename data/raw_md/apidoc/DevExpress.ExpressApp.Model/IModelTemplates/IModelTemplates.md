---
uid: DevExpress.ExpressApp.Model.IModelTemplates
name: IModelTemplates
type: Interface
summary: The Templates node provides access to Templates customizations made by an end-user.
syntax:
  content: |-
    [Browsable(false)]
    [ModelNodesGenerator(typeof(TemplatesModelNodeGenerator))]
    public interface IModelTemplates : IModelNode, IModelList<IModelTemplate>, IList<IModelTemplate>, ICollection<IModelTemplate>, IEnumerable<IModelTemplate>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelTemplates._members
  altText: IModelTemplates Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelTemplates** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelTemplate) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.TemplatesModelNodeGenerator) Nodes Generator.