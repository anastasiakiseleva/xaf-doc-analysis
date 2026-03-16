---
uid: "405489"
title: Access and Customize PDF Viewer Controls
seealso: []
---
# Access and Customize PDF Viewer Controls

The PDF Viewer Property Editor uses the following components internally: @DevExpress.Blazor.PdfViewer.DxPdfViewer (Blazor) or @DevExpress.XtraPdfViewer.PdfViewer (WinForms). This topic describes how to access and customize these components in XAF applications.

This approach follows the standard method for accessing and customizing a property editor with the [CustomizeViewItemControl](xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem})) event, as described in the following guide: <xref:402153>.

1. Create a custom @DevExpress.ExpressApp.ViewController in the _Controllers_ folder of the **SolutionName.Blazor.Server** / **SolutionName.Win** project.
2. Call the [CustomizeViewItemControl](xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0})) method to access the `PdfViewerPropertyEditor` in the `OnActivated` method handler.
3. Use the editor's `ComponentModel` (Blazor) or `Control` (WinForms) property to access the underlying component settings.
4. Modify component settings. The following code samples specify zoom level and hide the toolbar:

# [BlazorPdfViewerController.cs](#tab/tabid-blazor)
 
```csharp
using DevExpress.Blazor.Reporting.Models;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Office.Blazor.Editors;
using Microsoft.AspNetCore.Components;

public class BlazorPdfViewerController : ViewController<DetailView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<PdfViewerPropertyEditor>(this, editor => {
            editor.ComponentModel.ZoomLevel = 0.7;
            editor.ComponentModel.CustomizeToolbar = 
                EventCallback.Factory.Create<ToolbarModel>(this, toolbar => toolbar.AllItems.Clear());
        });
    }
}
```

# [WinPdfViewerController.cs](#tab/tabid-win)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Office.Win;

namespace MainDemo.Win.Controllers;

public class WinPdfViewerController : ViewController<DetailView> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<PdfViewerPropertyEditor>(this, editor => {
            editor.Control.ZoomFactor = 70f;
            editor.Control.NavigationPaneInitialVisibility = 
                DevExpress.XtraPdfViewer.PdfNavigationPaneVisibility.Hidden;
        });
    }
}
```
***

> [!ImageGallery]
> ![PDF Viewer in an XAF Blazor app](~/images/xaf-blazor-customized-pdf-viewer.png)
> ![PDF Viewer in an XAF WinForms app](~/images/xaf-win-customized-pdf-viewer.png)

## Specify PDF Viewer Menu Type: Ribbon, Toolbar, or No Menu (WinForms)

The WinForms PDF Viewer can display its menu as a Ribbon or Toolbar. Use the @DevExpress.ExpressApp.Office.Win.IModelWinOfficeMenuManagerSettings.MenuManagerType property to specify the menu type or hide the menu.

> [!ImageGallery]
> ![PDF Viewer ribbon menu merged into the main form's ribbon (`MenuManagerType = Default` and `FormStyle = Ribbon`)](~/images/xaf-win-pdf-viewer-menu-type-ribbon.png)
> ![Separate toolbar menu in PDF Viewer (`MenuManagerType = Bars`)](~/images/xaf-win-pdf-viewer-menu-type-toolbar.png)
> ![No menu in PDF Viewer (`MenuManagerType = None`)](~/images/xaf-win-pdf-viewer-menu-type-no-menu.png)

## Hide PDF Viewer Toolbar Groups/Ribbon Tabs (WinForms)

The WinForms PDF Viewer menu can display the following toolbar groups/ribbon tabs, listed in the @DevExpress.XtraPdfViewer.PdfViewerToolbarKind enumeration:
- Main
- Interactive Form (available when a document contains interactive form fields)
- Comment (not available when a document is read-only)

You can use the static `PdfViewerPropertyEditor.DefaultPdfViewerToolbarKind` property to list toolbars/tabs for display. The default property value is `All`, and the PDF Viewer displays every available toolbar.

# [SolutionName.Win\Program.cs](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Office.Win;
// ...
public class Program {
    public static void Main(string[] arguments) {
        PdfViewerPropertyEditor.DefaultPdfViewerToolbarKind = PdfViewerToolbarKind.Comment;
        // Use the vertical bar (|) to list several toolbars/tabs
        // PdfViewerPropertyEditor.DefaultPdfViewerToolbarKind = PdfViewerToolbarKind.Comment | PdfViewerToolbarKind.Main;
        // ...
    }  
    // ...
}
```
***

![Comment Tab in PDF Viewer](~/images/xaf-win-pdf-viewer-menu-comment-tab.png)


You can also [use the Toolbar Customization menu at runtime](xref:117515). The result is saved to the user's model differences.
