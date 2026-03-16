---
uid: DevExpress.ExpressApp.SystemModule.IExportable.Printable
name: Printable
type: Property
summary: Specifies the [](xref:DevExpress.XtraPrinting.IPrintable) control of the current List Editor.
syntax:
  content: IBasePrintable Printable { get; }
  parameters: []
  return:
    type: DevExpress.XtraPrinting.IBasePrintable
    description: An **IPrintable** control of the current List Editor.
seealso:
- linkId: "113012"
- linkId: "113362"
---
The [](xref:DevExpress.ExpressApp.SystemModule.ExportController) and [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController) Controllers use the **XtraPrintingLibrary** to perform printing and exporting operations under List Editors. This library exposes types that print and export data from the controls that implement the [](xref:DevExpress.XtraPrinting.IPrintable) interface. So, the PrintingController and ExportController Controllers print and export data only from List Editors that embed a control implementing the **IPrintable** interface. To access the printable control of the current exportable List Editor, use the **Printable** property.

It may be required to change the current control to be exported, when implementing a custom [](xref:DevExpress.ExpressApp.SystemModule.IExportable) List Editor. In this instance, trigger the [IExportable.PrintableChanged](xref:DevExpress.ExpressApp.SystemModule.IExportable.PrintableChanged) event in the **Printable** property's setter, to notify the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) that the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) should be updated.

# [C#](#tab/tabid-csharp)

```csharp
public IPrintable Printable {
    get { return printable; }
    set {
        if(printable != value) {
            printable = value;
            if(PrintableChanged != null) {
                PrintableChanged(this, new PrintableChangedEventArgs(printable));
            }
        }
    }
}
```
***