---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelActionContainerToRibbonLink
name: IModelActionContainerToRibbonLink
type: Interface
summary: Defines the functionality of the **ActionContainerToRibbonLink** [Application Model](xref:112580#node-types--interfaces) node.
syntax:
  content: |-
    [KeyProperty("ContainerId")]
    public interface IModelActionContainerToRibbonLink : IModelNode, IModelIndexedNode
seealso:
- linkId: DevExpress.ExpressApp.Blazor.SystemModule.IModelActionContainerToRibbonLink._members
  altText: IModelActionContainerToRibbonLink Members
---
The **ActionContainerToRibbonLink** Application Model node defines a link (placeholder for an [Action Container](xref:112610)) in the Ribbon UI. Use the @DevExpress.ExpressApp.Blazor.SystemModule.IModelActionContainerToRibbonLink.ActionContainer property to specify the mapped Action Container. The @DevExpress.ExpressApp.Model.IModelNode.Index property determines the order in which these nodes appear.

[!include[](~/templates/xaf-blazor-ribbon-note.md)]

![Action Container Property in the Model Editor](~/images/xaf-blazor-ribbon-action-container.png)