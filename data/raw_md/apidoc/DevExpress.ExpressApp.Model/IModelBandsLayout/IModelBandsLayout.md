---
uid: DevExpress.ExpressApp.Model.IModelBandsLayout
name: IModelBandsLayout
type: Interface
summary: The BandsLayout node provides access to a List View's [bands layout](xref:113695).
syntax:
  content: 'public interface IModelBandsLayout : IModelNode, IModelList<IModelBand>, IList<IModelBand>, ICollection<IModelBand>, IEnumerable<IModelBand>, IEnumerable'
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelBandsLayout._members
  altText: IModelBandsLayout Members
---
The child nodes of this node specify the bands layout:

![Bands_DragToScheduleResult](~/images/bands_dragtoscheduleresult117589.png)

To enable bands, set the [IModelBandsLayout.Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property to `true`. For more information, refer to the following topic: [](xref:113694).

![Bands_BandsLayout.Enable](~/images/bands_bandslayout.enable117588.png)

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement it in most cases.

The `IModelBandsLayout` node exposes a list of the [](xref:DevExpress.ExpressApp.Model.IModelBand) nodes.
<!--TODO: does it work for Blazor? -->