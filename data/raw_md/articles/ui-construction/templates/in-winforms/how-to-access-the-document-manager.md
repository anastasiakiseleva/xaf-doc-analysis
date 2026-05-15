---
uid: "113443"
seealso: []
title: 'How to: Access the Document Manager'
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

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.XtraBars.Docking2010
Imports DevExpress.XtraBars.Docking2010.Views
Imports DevExpress.XtraBars.Docking2010.Views.Tabbed
Imports DevExpress.ExpressApp.Templates
' ...
Public Class TabsCustomizationWindowController
    Inherits WindowController
    Public Sub New()
        TargetWindowType = WindowType.Main
    End Sub
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        AddHandler Window.TemplateChanged, AddressOf Window_TemplateChanged
    End Sub
    Private Sub Window_TemplateChanged(ByVal sender As Object, ByVal e As EventArgs)
        Dim template As IFrameTemplate = Window.Template
        Dim docManager As DocumentManager = CType(template, IDocumentsHostWindow).DocumentManager
        AddHandler docManager.ViewChanged, AddressOf docManager_ViewChanged
        CustomizeDocumentManagerView(docManager.View)
    End Sub
    Private Sub docManager_ViewChanged(ByVal sender As Object, ByVal args As ViewEventArgs)
        CustomizeDocumentManagerView(args.View)
    End Sub
    Private Shared Sub CustomizeDocumentManagerView(ByVal view As BaseView)
        If TypeOf view Is TabbedView Then
            CType(view, TabbedView).DocumentGroupProperties.HeaderLocation = _
            DevExpress.XtraTab.TabHeaderLocation.Left
            CType(view, TabbedView).DocumentGroupProperties.HeaderOrientation = _
            DevExpress.XtraTab.TabOrientation.Horizontal
        End If
    End Sub
    Protected Overrides Sub OnDeactivated()
        RemoveHandler Window.TemplateChanged, AddressOf Window_TemplateChanged
        MyBase.OnDeactivated()
    End Sub
End Class
```

***

Run the application to ensure that the tab captions location is changed.
