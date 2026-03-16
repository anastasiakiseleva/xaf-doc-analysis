---
uid: DevExpress.ExpressApp.Office.Win.ISpreadsheetValueStorage
name: ISpreadsheetValueStorage
type: Interface
summary: Declares members of the Spreadsheet editor's value storage.
syntax:
  content: public interface ISpreadsheetValueStorage
seealso:
- linkId: DevExpress.ExpressApp.Office.Win.ISpreadsheetValueStorage._members
  altText: ISpreadsheetValueStorage Members
---
A Spreadsheet editor's value storage allows you to implement custom logic executed when saving or loading a Spreadsheet document. Follow the steps below to create a custom value storage that specifies a file storage format. 

> [!Tip]
> We recommend you to use the `SpreadsheetPropertyEditor.DocumentFormat` property to specify a document storage format (see [How to: Customize the Spreadsheet Editor](xref:401211#change-the-document-storage-format)). The example below is shown for demonstration purposes.

1. Create a class that implements the `ISpreadsheetValueStorage` interface as shown below in the [WinForms application project](xref:118045) (_MySolution.Win_).

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp.Office.Win;
    using DevExpress.Spreadsheet;
    using DevExpress.XtraSpreadsheet;
    // ...
    public class OpenXmlSpreadsheetValueStorage : ISpreadsheetValueStorage {
        public object GetValue(SpreadsheetControl control) {
            return control.SaveDocument(DocumentFormat.OpenXml);
        }
        public void SetValue(SpreadsheetControl control, object propertyValue) {
            byte[] byteArray = propertyValue as byte[];
            if(byteArray != null) {
                control.LoadDocument(byteArray, DocumentFormat.OpenXml);
            }
        }
    }
    ```
    ***

2. Create a [View Controller](xref:112621#view-controllers) and access the `SpreadsheetPropertyEditor` as described in the [Ways to Access UI Elements and Their Controls](xref:120092#get-the-viewitem-or-property-editor-object) topic. Set the editor's `ValueStorage` property to an instance of `CustomSpreadsheetValueStorage` as shown below:

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Office.Win;
    // ...
    public class CustomSpreadsheetValueStorageController : ObjectViewController<DetailView, Document> {
        protected override void OnActivated() {
            base.OnActivated();
            SpreadsheetPropertyEditor spreadsheetPropertyEditor = View.FindItem("Data") as SpreadsheetPropertyEditor;
            if (spreadsheetPropertyEditor != null) {
                spreadsheetPropertyEditor.ValueStorage = new OpenXmlSpreadsheetValueStorage();
            }
        }
    }
    ```    
    ***