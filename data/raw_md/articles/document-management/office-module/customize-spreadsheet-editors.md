---
uid: '401211'
title: 'Customize the Spreadsheet Editors'
seealso:
  - linkId: '400894'
---
# Customize the Spreadsheet Editors

[!include[blazor-does-not-support-spreadsheet](~/templates/blazor-does-not-support-spreadsheet.md)]
## In the Model Editor

This section shows how to use the [Model Editor](xref:112582) to customize the [Spreadsheet Property Editor](xref:400931) in a [WinForms project](xref:118045).

### Show or Hide the Formula Bar

The `SpreadsheetPropertyEditor` displays the Spreadsheet control with a Formula Bar ([WinForms](xref:16484)). 

> [!ImageGallery]
> ![Formula Bar in a WinForms application](~/images/spreadsheet-formulabar.png)

In the Model Editor, navigate to the [!include[](~/templates/node_views_detailview_items_propertyeditor111384.md)] node and specify the @DevExpress.ExpressApp.Office.IModelSpreadsheetPropertyEditorSettings.EnableFormulaBar property to show or hide the Formula Bar.

![Formula Bar](~/images/spreadsheet-formulabar-modeleditor.png)

### Specify MenuManagerType for a Detail View
Note that the `SpreadsheetPropertyEditor` menu manager contains a [Ribbon Control](xref:2492) or [Bars](xref:5361)d.

Navigate to the [!include[](~/templates/node_views_detailview_items_propertyeditor111384.md)] node and set the editor's [MenuManagerType](xref:DevExpress.ExpressApp.Office.Win.IModelWinOfficeMenuManagerSettings.MenuManagerType).

![MenuManagerType property in Model Editor](~/images/spreadsheet-menumanagertype-modeleditor.png)

## In Code

### Change the Document Storage Format

1. In the  [WinForms application project](xref:118045), create a [View Controller](xref:112621#view-controllers).

2. In the overridden `OnActivated` method, access the `SpreadsheetPropertyEditor` as described in the [Ways to Access UI Elements and Their Controls](xref:120092#get-the-viewitem-or-property-editor-object) topic.

3. Specify the editor's `DocumentFormat` property.

    # [C#](#tab/tabid-csharp)
    
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Office.Win;
    using DevExpress.Spreadsheet;
    // ...
    public class SpreadsheetDocumentFormatController : ObjectViewController<DetailView, Document> {
        protected override void OnActivated() {
            base.OnActivated();
            SpreadsheetPropertyEditor spreadsheetPropertyEditor = View.FindItem("Data") as SpreadsheetPropertyEditor;
            if (spreadsheetPropertyEditor != null) {
                spreadsheetPropertyEditor.DocumentFormat = DocumentFormat.OpenXml;
            }
        }
    }
    ```
    ***

### Customize the WinForms SpreadsheetPropertyEditor Menu

The `SpreadsheetPropertyEditor` menu does not display all available toolbars and ribbon tabs. Use the static `SpreadsheetPropertyEditor.DefaultSpreadsheetToolbarType` property to customize toolbars. The available items are listed in the @DevExpress.XtraSpreadsheet.SpreadsheetToolbarType enumeration. 

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Office.Win;
using DevExpress.XtraSpreadsheet;
// ...
SpreadsheetPropertyEditor.DefaultSpreadsheetToolbarType |= 
    SpreadsheetToolbarType.ChartTools | SpreadsheetToolbarType.TableTools;
```
***

Handle the `SpreadsheetMenuManagerController.CustomizeSpreadsheetToolbarType` event to change the toolbars and tabs for a specific editor only:

1. In the [WinForms Module project](xref:118045), create a [View Controller](xref:112621#view-controllers). If your solution does not contain this project, add the Controller to the [WinForms application project](xref:118045).

2. Access the `SpreadsheetMenuManagerController` and subscribe to its `CustomizeSpreadsheetToolbarType` event in the overridden `OnActivated` method.

3. In the event handler, specify the `CustomizeSpreadsheetToolbarTypeEventArgs.SpreadsheetToolbarType` property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Office.Win;
using DevExpress.XtraSpreadsheet;
// ...
public class CustomSpreadsheetController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        SpreadsheetMenuManagerController controller = Frame.GetController<SpreadsheetMenuManagerController>();
        if (controller != null) {
            controller.CustomizeSpreadsheetToolbarType += Controller_CustomizeSpreadsheetToolbarType;
        }
    }
    private void Controller_CustomizeSpreadsheetToolbarType(object sender, CustomizeSpreadsheetToolbarTypeEventArgs e) {
        e.SpreadsheetToolbarType |= SpreadsheetToolbarType.ChartTools | SpreadsheetToolbarType.TableTools;
    }
}
```
***

You can also [customize the Bars menu at runtime](xref:117515). Your customizations are stored in the [user's model differences](xref:403527).