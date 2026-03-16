---
uid: DevExpress.ExpressApp.Model.IModelBOModelClassMembers
name: IModelBOModelClassMembers
type: Interface
summary: The OwnMembers node defines the members declared in a particular [business class](xref:112570).
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelBOModelMemberNodesGenerator))]
    public interface IModelBOModelClassMembers : IModelNode, IModelList<IModelMember>, IList<IModelMember>, ICollection<IModelMember>, IEnumerable<IModelMember>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelBOModelClassMembers._members
  altText: IModelBOModelClassMembers Members
- linkId: "112579"
- linkId: "112580"
- linkId: "112600"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelBOModelClassMembers** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelMember) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelMemberNodesGenerator) Nodes Generator.