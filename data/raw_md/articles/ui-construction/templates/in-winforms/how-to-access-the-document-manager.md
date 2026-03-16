---
uid: "113443"
seealso: []
title: 'How to: Access the Document Manager'
owner: Ekaterina Kiseleva
---
# How to: Access the Document Manager

This topic demonstrates how to access the [Document Manager](xref:11359) that the [](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy) uses to show [Views](xref:112611) in a WinForms application. You will locate tab captions to the left and orient them horizontally.

![AccessDocumentManager](~/images/accessdocumentmanager117085.png)

Here, it is assumed that you have the UI type set to **TabbedMDI** in the Model Editor for your Windows Forms application (see [IModelOptionsWin.UIType](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.UIType)). Perform the following steps to access the [](xref:DevExpress.XtraBars.Docking2010.DocumentManager) object and customize its default settings.

1. Create a new [](xref:DevExpress.ExpressApp.WindowController) in the WinForms module's _Controllers_ folder.
2. The Document Manager is located on the MainForm [Template](xref:112609). Override the Controller's **OnActivated** method and subscribe to the main Window's [Frame.TemplateChanged](xref:DevExpress.ExpressApp.Frame.TemplateChanged) event to access the MainForm Template after it has been created or changed.
3. Cast the MainForm Template by the **IDocumentsHostWindow** interface and access the Document Manager using the **DocumentManager** property.
4. Subscribe to the [DocumentManager.ViewChanged](xref:DevExpress.XtraBars.Docking2010.DocumentManager.ViewChanged) event that occurs when the Document Manager has switched to another View.
5. Add the following **CustomizeDocumentManagerView** method that changes the location and orientation of tab captions if the Document Manager's View is of the **TabbedView** type.
6. Call the **CustomizeDocumentManagerView** method from both **Frame.TemplateChanged** and **DocumentManager.ViewChanged** event handlers.
7. Override the **OnDeactivated** method and unsubscribe from the **Window.TemplateChanged** event when the Controller is deactivated.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.XtraBars.Docking2010;
using DevExpress.XtraBars.Docking2010.Views;
using DevExpress.XtraBars.Docking2010.Views.Tabbed;
using DevExpress.ExpressApp.Templates;
// ...
public class TabsCustomizationWindowController : WindowController {
    public TabsCustomizationWindowController() {
        TargetWindowType = WindowType.Main;
    }
    protected override void OnActivated() {
        base.OnActivated();
        Window.TemplateChanged += Window_TemplateChanged;
    }
    private void Window_TemplateChanged(object sender, EventArgs e) {
        IFrameTemplate template = Window.Template;
        DocumentManager docManager = ((IDocumentsHostWindow)template).DocumentManager;
        docManager.ViewChanged += docManager_ViewChanged;
        CustomizeDocumentManagerView(docManager.View);
    }
    private void docManager_ViewChanged(object sender, ViewEventArgs args) {
        CustomizeDocumentManagerView(args.View);
    }
    private static void CustomizeDocumentManagerView(BaseView view) {
        if(view is TabbedView) {
            ((TabbedView)view).DocumentGroupProperties.HeaderLocation = 
                DevExpress.XtraTab.TabHeaderLocation.Left;
            ((TabbedView)view).DocumentGroupProperties.HeaderOrientation = 
                DevExpress.XtraTab.TabOrientation.Horizontal;
        }
    }
    protected override void OnDeactivated() {
        Window.TemplateChanged -= Window_TemplateChanged;
        base.OnDeactivated();
    }
}
```
***

Run the application to ensure that the tab captions location is changed.
