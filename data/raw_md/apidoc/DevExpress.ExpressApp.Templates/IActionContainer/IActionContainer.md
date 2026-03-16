---
uid: DevExpress.ExpressApp.Templates.IActionContainer
name: IActionContainer
type: Interface
summary: Declares members implemented by [Action Containers](xref:112610).
syntax:
  content: 'public interface IActionContainer : ISupportUpdate, IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.Templates.IActionContainer._members
  altText: IActionContainer Members
---
The **XAF** design is based on the concept of abstract elements and actual controls. An [Action](xref:112622) is an abstract entity. It can be displayed by any control that suits its type. Actions' controls are displayed via [Action Containers](xref:112610) - the objects that implement the [](xref:DevExpress.ExpressApp.Templates.IActionContainer) interface. An Action Container has a collection of Actions. To add an Action to an Action Container, the latter has the [IActionContainer.Register](xref:DevExpress.ExpressApp.Templates.IActionContainer.Register(DevExpress.ExpressApp.Actions.ActionBase)) method. To determine in which Action Container an Action will be contained, the [Application Model](xref:112580)'s **Application** | **ActionDesign** | **ActionToContainerMapping** node is designed.
