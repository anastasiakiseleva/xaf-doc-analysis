---
uid: DevExpress.ExpressApp.Model.IModelClassInterfaces
name: IModelClassInterfaces
type: Interface
summary: The InterfaceLinks node lists classes aggregated by the current `IModelClass`.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelClassInterfacesNodesGenerator))]
    public interface IModelClassInterfaces : IModelNode, IModelList<IModelInterfaceLink>, IList<IModelInterfaceLink>, ICollection<IModelInterfaceLink>, IEnumerable<IModelInterfaceLink>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelClassInterfaces._members
  altText: IModelClassInterfaces Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelClassInterfaces** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelInterfaceLink) nodes.