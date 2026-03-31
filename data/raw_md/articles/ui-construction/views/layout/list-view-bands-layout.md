---
uid: "113695"
seealso:
- linkId: "113694"
- linkId: "114637"
- linkId: "9873"
title: "List Views: Banded Column Layout"
---
# List Views: Banded Column Layout

A band groups multiple columns under the same header.

![XAF ASP.NET Core Blazor and Windows Forms Bands, DevExpress](~/images/bands_winweb117597.png)

## Platform-Specific Components and Features

| Platform | Component | Feature | XAF Built-In List Editor
|-|-|-|-|
| ASP.NET Core Blazor  | @DevExpress.Blazor.DxGrid | @DevExpress.Blazor.DxGridBandColumn | @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor |
| ASP.NET Core Blazor  | @DevExpress.Blazor.DxTreeList | @DevExpress.Blazor.DxTreeListBandColumn | @DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor |
| Windows Forms  | [](xref:3455) | [](xref:114637) | @DevExpress.ExpressApp.Win.Editors.GridListEditor |

## Add and Configure Bands

To configure bands in the same manner across all platforms, navigate to the **YourSolutionName.Module** project and run the Model Editor for the _Model.DesignedDiffs.xafml_ file.

For platform-specific configuration, run the Model Editor for the _Model.xafml_ file in the following projects:

* ASP.NET Core Blazor: **YourSolutionName.Blazor.Server**
* Windows Forms: **YourSolutionName.Win**

In the Model Editor, navigate to the **Views** | **\<Project\>.BusinessObjects** | **\<Class\>** | **\<Class\>_ListView** | **BandsLayout** node and set the [Enable](xref:DevExpress.ExpressApp.Model.IModelBandsLayout.Enable) property to `true`.

   ![XAF Model Editor Enable Bands in List View Layout, DevExpress](~/images/bands_bandslayout.enable117588.png)

## Bands Layout

The [](xref:DevExpress.ExpressApp.Model.IModelBandsLayout) node's structure in the [Application Model](xref:112579) determines the bands layout.

![XAF Model Editor Task List View Bands Layout Result, DevExpress](~/images/bands_dragtoscheduleresult117589.png)

Select the **Add…** | **Band** context menu command to add an @DevExpress.ExpressApp.Model.IModelBand child node. Drag-and-drop columns into the newly created band (node). You can add a band to an existing band and create a multi-level band hierarchy.

> [!NOTE]
> Step-by-step instructions on how to configure bands layout is available in the following topic: [](xref:113694).

## End-User Layout Customization

An end-user can do the following:
* Rearrange bands
* Reorder columns within a band
* Move columns and bands from one parent band to another (Windows Forms)

To undo runtime layout customization in the current View, use the **Reset View Settings** Action. For more information about runtime layout customization, refer to the following topic: [](xref:113679#runtime-customization).

## Additional Configuration Options (Windows Forms)

### Multi-Level Bands

XAF Windows Forms applications allow you to arrange column headers across rows. You can also stretch column headers vertically to occupy more than one row.

> [!NOTE]
> XAF ASP.NET Core Blazor applications do not support multi-level bands.

Use the [RowIndex](xref:DevExpress.ExpressApp.Win.Model.IModelBandedColumnWin.RowIndex) property of the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **BandsLayout** | **Band** | **Column** node to specify the column header vertical position.

![XAF Windows Forms Row Index, DevExpress](~/images/bands_rowindex117596.png)

This property specifies the zero-based row number of the current column within a band. In the following image, the **Subject** column's `RowIndex` is `1`. The `RowIndex` of the other column within the same band is `0`:

![|XAF Windows Forms Row Index Results, DevExpress](~/images/bands_winadv117594.png)

### Header Visibility

Use the [ShowBands](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.ShowBands) and [ShowColumnHeaders](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.ShowColumnHeaders) properties of the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **BandsLayout** node to hide band and column headers.

![XAF Windows Forms Band Header Visibility, De](~/images/bands_bandslayoutwin_headers117598.png)

## Restrict End-User Layout Customization

To restrict layout customization, use the following properties of the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **BandsLayout** node:

* [AllowBandMoving](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowBandMoving)
* [AllowChangeBandParent](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowChangeBandParent)
* [AllowChangeColumnParent](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowChangeColumnParent)
* [AllowColumnMoving](xref:DevExpress.ExpressApp.Win.Model.IModelBandsLayoutWin.AllowColumnMoving)

![Bands_BandsLayoutWin](~/images/bands_bandslayoutwin_customization117595.png)
