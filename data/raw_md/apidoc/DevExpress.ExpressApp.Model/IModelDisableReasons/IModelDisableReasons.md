---
uid: DevExpress.ExpressApp.Model.IModelDisableReasons
name: IModelDisableReasons
type: Interface
summary: The **DisableReasons** node lists the disabling reasons for an Action, specifying a definition for each of them.
syntax:
  content: |-
    [ImageName("ModelEditor_Actions_DisableReasons")]
    public interface IModelDisableReasons : IModelNode, IModelList<IModelReason>, IList<IModelReason>, ICollection<IModelReason>, IEnumerable<IModelReason>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelDisableReasons._members
  altText: IModelDisableReasons Members
- linkId: "112579"
- linkId: "112580"
---
The [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property returns a collection of key reason/value pairs. When all the keys in this collections have true as a value, an Action is enabled. When an Action is disabled, a hint with the description of the disabling reason will appear. The reason is specified by the corresponding key.

By default, this node contains several reasons. You can use them when disabling an Action. If you specify a new reason in the **Enabled.SetItemValue** method call, specify the definition for it.  To do this, add a new reason via the DisableReasons node's context menu or in code, and specify its [IModelReason.Id](xref:DevExpress.ExpressApp.Model.IModelReason.Id) and [IModelReason.Caption](xref:DevExpress.ExpressApp.Model.IModelReason.Caption) properties.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases. 

The **IModelDisableReasons** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelReason) nodes.