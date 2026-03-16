---
uid: DevExpress.ExpressApp.Model.IModelColumnSummary
name: IModelColumnSummary
type: Interface
summary: The Summary node provides access to a List View column's summaries.
syntax:
  content: 'public interface IModelColumnSummary : IModelNode, IModelList<IModelColumnSummaryItem>, IList<IModelColumnSummaryItem>, ICollection<IModelColumnSummaryItem>, IEnumerable<IModelColumnSummaryItem>, IEnumerable'
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelColumnSummary._members
  altText: IModelColumnSummary Members
- linkId: "112579"
- linkId: "112580"
- linkId: "113285"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelColumnSummary** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelColumnSummaryItem) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelListViewColumnsNodesGenerator) Nodes Generator.