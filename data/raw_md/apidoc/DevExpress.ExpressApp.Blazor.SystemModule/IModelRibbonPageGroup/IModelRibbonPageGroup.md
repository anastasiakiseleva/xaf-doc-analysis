---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPageGroup
name: IModelRibbonPageGroup
type: Interface
summary: Defines functionality of the **RibbonPageGroup** [Application Model](xref:112580#node-types--interfaces) node.
syntax:
  content: 'public interface IModelRibbonPageGroup : IModelNode, IModelList<IModelActionContainerToRibbonLink>, IList<IModelActionContainerToRibbonLink>, ICollection<IModelActionContainerToRibbonLink>, IEnumerable<IModelActionContainerToRibbonLink>, IEnumerable, IModelIndexedNode'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPageGroup._members
  altText: IModelRibbonPageGroup Members
---
The **RibbonPageGroup** Application Model node specifies settings of a group in the Ribbon UI. You can set the group @DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPageGroup.Caption, order @DevExpress.ExpressApp.Model.IModelNode.Index, and access the list of nested **ActionContainer** elements.

[!include[](~/templates/xaf-blazor-ribbon-note.md)]

![Context Ribbon Page](~/images/xaf-blazor-ribbon-structure.png)