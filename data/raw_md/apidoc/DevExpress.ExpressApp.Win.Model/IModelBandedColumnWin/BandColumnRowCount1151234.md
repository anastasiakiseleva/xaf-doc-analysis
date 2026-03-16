---
uid: DevExpress.ExpressApp.Win.Model.IModelBandedColumnWin.BandColumnRowCount
name: BandColumnRowCount
type: Property
summary: Specifies the [Band Header](xref:566) height in rows.
syntax:
  content: |-
    [Browsable(false)]
    [DefaultValue(1)]
    int BandColumnRowCount { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the band header height in rows. Values less than 1 are not accepted.
seealso: []
---
The **BandColumnRowCount** value is passed to the [GridBand.RowCount](xref:DevExpress.XtraGrid.Views.BandedGrid.GridBand.RowCount) property.