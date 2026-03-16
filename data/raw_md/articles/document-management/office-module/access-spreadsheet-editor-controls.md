---
uid: '400894'
title: 'Access the Spreadsheet Editor Controls'
owner: Yekaterina Kiseleva
seealso:
  - linkId: '401211'
---
# Access the Spreadsheet Editor Controls

This topic describes how to access and customize the @DevExpress.XtraSpreadsheet.SpreadsheetControl control used to display [Spreadsheet documents](xref:400931)in XAF Windows Forms applications with the [Office Module](xref:400003):

[!include[blazor-does-not-support-spreadsheet](~/templates/blazor-does-not-support-spreadsheet.md)]

## Access the WinForms-Specific Control (SpreadsheetControl)

Follow the steps below to access the `SpreadsheetControl` and restrict the number of visible rows and columns in a worksheet.

1. Create a custom @DevExpress.ExpressApp.ViewController in the [WinForms application project](xref:118045) (_MySolution.Win_).
2. In the overridden `OnActivated` method, get the `SpreadsheetServiceController` and subscribe to its `CustomizeSpreadsheetControl` event.
3. In the `CustomizeSpreadsheetControl`'s handler, access the @DevExpress.XtraSpreadsheet.SpreadsheetControl and subscribe to its @DevExpress.XtraSpreadsheet.SpreadsheetControl.DocumentLoaded event.
4. In the `DocumentLoaded` event handler, use the @DevExpress.XtraSpreadsheet.WorksheetDisplayArea.SetSize* method to specify the number of visible rows and columns for an [active worksheet](xref:DevExpress.XtraSpreadsheet.SpreadsheetControl.ActiveWorksheet).

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Office.Win;
    using DevExpress.Spreadsheet;
    using DevExpress.XtraSpreadsheet;
    // ...
    public class WinSpreadsheetController : ViewController {
        protected override void OnActivated() {
            base.OnActivated();
            SpreadsheetServiceController controller = Frame.GetController<SpreadsheetServiceController>();
            if(controller != null) {
                controller.CustomizeSpreadsheetControl += Controller_CustomizeSpreadsheetControl;
            }
        }
        private void Controller_CustomizeSpreadsheetControl(object sender, CustomizeSpreadsheetEventArgs e) {
            SpreadsheetControl spreadsheetControl = ((SpreadsheetPropertyEditor)sender).SpreadsheetControl;
            spreadsheetControl.DocumentLoaded += SpreadsheetControl_DocumentLoaded;
        }
        private void SpreadsheetControl_DocumentLoaded(object sender, System.EventArgs e) {
            SpreadsheetControl spreadsheetControl = (SpreadsheetControl)sender;
            Worksheet worksheet = spreadsheetControl.ActiveWorksheet;
            spreadsheetControl.WorksheetDisplayArea.SetSize(worksheet.Index, 5, 10);
        }
    }
    ```
    ***
