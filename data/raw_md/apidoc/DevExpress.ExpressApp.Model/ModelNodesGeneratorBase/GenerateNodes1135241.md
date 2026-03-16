---
uid: DevExpress.ExpressApp.Model.ModelNodesGeneratorBase.GenerateNodes(DevExpress.ExpressApp.Model.Core.ModelNode)
name: GenerateNodes(ModelNode)
type: Method
summary: Generates the specified node's content.
syntax:
  content: public void GenerateNodes(ModelNode node)
  parameters:
  - id: node
    type: DevExpress.ExpressApp.Model.Core.ModelNode
    description: A **ModelNode** object which is the [Application Model](xref:112580) node to be generated.
seealso: []
---
This method also invokes the [IModelNodesGeneratorUpdater.UpdateNode](xref:DevExpress.ExpressApp.Model.IModelNodesGeneratorUpdater.UpdateNode(DevExpress.ExpressApp.Model.Core.ModelNode)) method of each Generator Updater attached to the current Nodes Generator.