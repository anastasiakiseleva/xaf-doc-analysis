---
uid: DevExpress.ExpressApp.Model.IModelBOModel
name: IModelBOModel
type: Interface
summary: The BOModel node provides access to all the Application Model's [persistent classes](xref:112570) and their properties.
syntax:
  content: |-
    [ImageName("ModelEditor_Business_Object_Model")]
    [ModelNodesGenerator(typeof(ModelBOModelClassNodesGenerator))]
    public interface IModelBOModel : IModelNode, IModelList<IModelClass>, IList<IModelClass>, ICollection<IModelClass>, IEnumerable<IModelClass>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelBOModel._members
  altText: IModelBOModel Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelBOModel** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelClass) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelClassNodesGenerator) Nodes Generator.