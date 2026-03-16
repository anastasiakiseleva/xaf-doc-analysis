---
uid: DevExpress.ExpressApp.Model.IModelOptions
name: IModelOptions
type: Interface
summary: The Options node allows editing different UI settings.
syntax:
  content: |-
    [ImageName("ModelEditor_Settings")]
    [ModelNodesGenerator(typeof(ModelOptionsNodesGenerator))]
    public interface IModelOptions : IModelNode
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelOptions._members
  altText: IModelOptions Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelOptionsNodesGenerator) Nodes Generator.