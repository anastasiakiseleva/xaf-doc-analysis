---
uid: DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin
name: IModelBandsLayoutWin
type: Interface
summary: Used to extend the [Application Model](xref:112580)'s BandsLayout node.
syntax:
  content: 'public interface IModelBandsLayoutWin : IModelBandsLayout, IModelNode, IModelList<IModelBand>, IList<IModelBand>, ICollection<IModelBand>, IEnumerable<IModelBand>, IEnumerable'
seealso:
- linkId: DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin._members
  altText: IModelBandsLayoutWin Members
- linkId: "113694"
---
This interface extends the BandsLayout node with WinForms-specific properties. The following **IModelBandsLayoutWin** properties can be used to restrict bands layout customizations by users:

* [IModelBandsLayoutWin.AllowBandMoving](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowBandMoving)
* [IModelBandsLayoutWin.AllowChangeBandParent](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowChangeBandParent)
* [IModelBandsLayoutWin.AllowChangeColumnParent](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowChangeColumnParent)
* [IModelBandsLayoutWin.AllowColumnMoving](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowColumnMoving)

![Bands_BandsLayoutWin](~/images/bands_bandslayoutwin_customization117595.png)

The following **IModelBandsLayoutWin** properties are used setup the visibility of band and column headers.

* [IModelBandsLayoutWin.ShowBands](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.ShowBands)
* [IModelBandsLayoutWin.ShowColumnHeaders](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.ShowColumnHeaders)

![Bands_BandsLayoutWin_Headers](~/images/bands_bandslayoutwin_headers117598.png)

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases. The **IModelBandsLayoutWin** interface is used by the [](xref:DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule), to extend the [](xref:DevExpress.ExpressApp.Model.IModelBandsLayout) interface. 