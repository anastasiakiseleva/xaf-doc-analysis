---
uid: DevExpress.ExpressApp.Model.IModelNode
name: IModelNode
type: Interface
summary: Serves as the base interface for interfaces that represent [Application Model](xref:112580) nodes.
syntax:
  content: public interface IModelNode
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelNode._members
  altText: IModelNode Members
- linkId: "112579"
---
The Application Model consists of nodes and properties. Nodes can have child nodes and they form the structure of the Application Model. A node typically has a set of properties that hold the Application Model's data. For example, the Application Model has the [](xref:DevExpress.ExpressApp.Model.IModelOptions) node. This node has child nodes as well as properties that represent an XAF application's settings.

The **IModelNode** interface represents the Application Model's node, and exposes members to manage it. Using them, you can access the node's child nodes and properties.