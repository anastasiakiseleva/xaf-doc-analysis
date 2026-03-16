---
uid: DevExpress.ExpressApp.Win.Model.IModelBandedColumnWin.RowIndex
name: RowIndex
type: Property
summary: Specifies the vertical position of the column header within a [band](xref:113695).
syntax:
  content: |-
    [Browsable(false)]
    int RowIndex { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value representing the zero-based index of the band row where a column header is displayed.
seealso:
- linkId: "113694"
---
You can arrange column headers across rows in WinForms applications using the **RowIndex**.

![Bands_RowIndex](~/images/bands_rowindex117596.png)

The **RowIndex** property specifies the zero-based row number of the current column within a band. In the image below, the **Subject** column's **RowIndex** is **1**. The **RowIndex** of the **Status** and **Assigned To** columns is **0**.

![Bands_WinAdv](~/images/bands_winadv117594.png)