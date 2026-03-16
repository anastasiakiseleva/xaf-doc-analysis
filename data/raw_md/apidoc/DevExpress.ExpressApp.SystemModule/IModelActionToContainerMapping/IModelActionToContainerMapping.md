---
uid: DevExpress.ExpressApp.SystemModule.IModelActionToContainerMapping
name: IModelActionToContainerMapping
type: Interface
summary: The ActionToContainerMapping node specifies the Action Containers to which the application's Actions are mapped according to their **Category** property value.
syntax:
  content: |-
    [ImageName("ModelEditor_Actions_ActionToContainerMapping")]
    [ModelNodesGenerator(typeof(ModelActionContainersGenerator))]
    public interface IModelActionToContainerMapping : IModelNode, IModelList<IModelActionContainer>, IList<IModelActionContainer>, ICollection<IModelActionContainer>, IEnumerable<IModelActionContainer>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.IModelActionToContainerMapping._members
  altText: IModelActionToContainerMapping Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelActionToContainerMapping** node represents a list of the [](xref:DevExpress.ExpressApp.SystemModule.IModelActionContainer) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.SystemModule.ModelActionContainersGenerator) Nodes Generator.