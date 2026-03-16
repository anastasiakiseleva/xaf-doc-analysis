---
uid: DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1.UpdateCachedNode(DevExpress.ExpressApp.Model.Core.ModelNode)
name: UpdateCachedNode(ModelNode)
type: Method
summary: Updates the specified node after it has been recovered from the cache file.
syntax:
  content: public virtual void UpdateCachedNode(ModelNode node)
  parameters:
  - id: node
    type: DevExpress.ExpressApp.Model.Core.ModelNode
    description: A **ModelNode** object for which a custom Generator Updater is implemented (see [Extend and Customize the Application Model in Code](xref:112810)).
seealso: []
---
When the [XafApplication.EnableModelCache](xref:DevExpress.ExpressApp.XafApplication.EnableModelCache) property is set to **true**, the Application Model content is cached to a file when the application is first launched, and recovered on subsequent runs. Override this method to update the node after it has been recovered from the cache.