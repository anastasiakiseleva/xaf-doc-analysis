---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPage
name: IModelRibbonPage
type: Interface
summary: Defines functionality of the **RibbonPage** [Application Model](xref:112580#node-types--interfaces) node.
syntax:
  content: 'public interface IModelRibbonPage : IModelNode, IModelList<IModelRibbonPageGroup>, IList<IModelRibbonPageGroup>, ICollection<IModelRibbonPageGroup>, IEnumerable<IModelRibbonPageGroup>, IEnumerable, IModelIndexedNode'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPage._members
  altText: IModelRibbonPage Members
---
The **RibbonPage** Application Model node specifies settings of a page in the Ribbon UI. You can set the page @DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPage.Caption, order @DevExpress.ExpressApp.Model.IModelNode.Index, and access the list of nested **RibbonPageGroup** elements. Set the page's @DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPage.Contextual property to `true` to highlight the page header and display it after standard ribbon pages.

[!include[](~/templates/xaf-blazor-ribbon-note.md)]

![Context Ribbon Page](~/images/xaf-blazor-ribbon-structure.png)