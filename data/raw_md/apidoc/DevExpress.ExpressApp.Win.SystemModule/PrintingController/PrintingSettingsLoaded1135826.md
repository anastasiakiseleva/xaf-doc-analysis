---
uid: DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintingSettingsLoaded
name: PrintingSettingsLoaded
type: Event
summary: Occurs when the [PrintingController.PrintAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintAction) is executed.
syntax:
  content: public event EventHandler<PrintableComponentLinkEventArgs> PrintingSettingsLoaded
seealso:
- linkId: "113283"
- linkId: DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomGetPrintableControl
---
Handle the `PrintingSettingsLoaded` event in a custom [View Controller](xref:112621) to customize the [](xref:DevExpress.XtraPrinting.PrintableComponentLink), which represents a printing link to the printable control. In the handler, you can access the **PrintableComponentLink** object in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Win.SystemModule;
// ...
public class ConfigurePrintingSettingsViewController : ViewController {
    private PrintingController printingService;
    protected override void OnActivated() {
        base.OnActivated();
        printingService = Frame.GetController<PrintingController>();
            if (printingService != null)
                printingService.PrintingSettingsLoaded += printingService_PrintingSettingsLoaded;
    }
    private void printingService_PrintingSettingsLoaded(
        object sender, PrintableComponentLinkEventArgs e) {
        e.PrintableComponentLink.PaperKind = System.Drawing.Printing.PaperKind.A4;
        e.PrintableComponentLink.Landscape = true;
    }
    protected override void OnDeactivated() {
        if (printingService != null)
            printingService.PrintingSettingsLoaded -= printingService_PrintingSettingsLoaded;
        base.OnDeactivating();
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp.Win.SystemModule
' ...
Public Class ConfigurePrintingSettingsViewController
    Inherits ViewController
    Private printingService As PrintingController
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        printingService = Frame.GetController(Of PrintingController)()
            If printingService IsNot Nothing Then
                AddHandler printingService.PrintingSettingsLoaded, _
                AddressOf printingService_PrintingSettingsLoaded
            End If
    End Sub
    Private Sub printingService_PrintingSettingsLoaded( _
    ByVal sender As Object, ByVal e As PrintableComponentLinkEventArgs)
        e.PrintableComponentLink.PaperKind = System.Drawing.Printing.PaperKind.A4
        e.PrintableComponentLink.Landscape = True
    End Sub
    Protected Overrides Sub OnDeactivated()
        If printingService IsNot Nothing Then
            RemoveHandler printingService.PrintingSettingsLoaded, _
            AddressOf printingService_PrintingSettingsLoaded
        End If
        MyBase.OnDeactivating()
    End Sub
End Class
```

***

The **PrintableComponentLink** object provides access to the [](xref:DevExpress.XtraPrinting.PrintingSystem) object using the **PrintingSystem** property. Refer to the [How to: Customize Export Options of the Printing System](xref:113283), to see an example on how to access the Printing System in the **PrintingSettingsLoaded** event handler.

> [!NOTE]
> The **PrintingSettingsLoaded** event is not raised when **GridControl** is used with a **CollectionSource** object in [Server](xref:118450) mode (see [CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode)), or when the [PrintingController.CustomForceGridControlMethods](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomForceGridControlMethods) event is handled and its  **Force** parameter is set to **true**. In this case, you can customize the grid print preview options using the [](xref:DevExpress.XtraGrid.Views.Grid.GridOptionsPrint) object.