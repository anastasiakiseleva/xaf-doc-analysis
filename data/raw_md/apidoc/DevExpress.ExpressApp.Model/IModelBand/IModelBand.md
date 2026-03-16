---
uid: DevExpress.ExpressApp.Model.IModelBand
name: IModelBand
type: Interface
summary: The Band node defines a logical group ([band](xref:113695)) of columns. A band is visually represented by a header displayed above headers of the columns it combines.
syntax:
  content: |-
    [ImageName("ModelEditor_Band")]
    public interface IModelBand : IModelBandedLayoutItem, IModelLayoutElement, IModelNode
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelBand._members
  altText: IModelBand Members
- linkId: "113694"
---
> [!IMPORTANT]
> You cannot add the **IModelBand** node in the [Model Editor](xref:112582) unless you set the [IModelBandsLayout.Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property of the **ListView** | **BandsLayout** node to **true**.

To create an **IModelBand** node, right-click the **Column** node and choose **Add…** | **Band**. You can also add a child band into an existing band to create a band hierarchy.

![Bands_AddBand](~/images/bands_addband117587.png)

To add columns into a band, select one or more **Column** nodes and drag them into the band:

![Bands_DragToTaskDetails](~/images/bands_dragtotaskdetails117590.png)

In WinForms applications, the **IModelBand** node is extended with properties from [](xref:DevExpress.ExpressApp.Win.Model.IModelBandWin).

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.