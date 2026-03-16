---
uid: '400063'
title: 'Access and Customize Rich Text Editor Controls'
owner: Anastasiya Kisialeva
---
# Access and Customize Rich Text Editor Controls

This topic describes how to access and customize the following controls in XAF applications with the [Office Module](xref:400003):

{|
|-
! Platform
! Control
! Purpose
|-

| ASP.NET Core Blazor
| @DevExpress.Blazor.RichEdit.DxRichEdit
| Displays [Rich Text documents](xref:400004)
|-

| WinForms
| @DevExpress.XtraRichEdit.RichEditControl
| Displays [Rich Text documents](xref:400004)
|}

This topic describes the following tasks:

1. Specify font size, spell checker availability, and paper type ([ASP.NET Core Blazor](#aspnet-core-blazor-access-the-rich-text-editor-control), [Windows Forms](#windows-forms-access-the-rich-text-editor-control)).
2. [Change Toolbar and Ribbon Tab availability (Windows Forms)](#change-toolbar-and-ribbon-tab-availability).
5. [Specify a Menu Manager for a Detail View (Windows Forms)](#specify-menumanagertype-for-a-detail-view).
6. [Change the document storage format (Windows Forms)](#change-the-document-storage-format).
7. [Specify the editor height in a List View (Windows Forms)](#specify-the-editor-height-embedded-cell-viewereditor).

## ASP.NET Core Blazor: Access the Rich Text Editor Control

Follow these steps to access the `DxRichEditModel` component model. A component model defines a Blazor component in code. When you modify the model, the underlying component reflects these changes. For more information about component models, refer to the following topic: [](xref:404767).

1. In the _Controllers_ folder of the **YourSolutionName.Blazor.Server** project, create a custom @DevExpress.ExpressApp.ViewController.
2. In the Controller's `OnActivated` method, use the [](xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0})) extension method to customize the `RichTextPropertyEditor`.
3. In the event handlers, access the `DevExpress.ExpressApp.Office.Blazor.Components.Models.DxRichEditModel` component model and do the following:
    * Specify its `ViewType` property to change a document view layout type (see [](xref:DevExpress.Blazor.RichEdit.DxRichEdit.ViewType)).
    * Enable spell checker.
    * Specify the document's font size.
    * Specify the paper type.

    **File:**  
    _YourSolutionName.Blazor.Server\Controllers\BlazorRichEditController.cs_

    ```csharp
    using DevExpress.Drawing.Printing;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Office.Blazor.Components.Models;
    using DevExpress.ExpressApp.Office.Blazor.Editors;
    using DevExpress.ExpressApp.Office.Blazor.Editors.Adapters;
    using DevExpress.XtraRichEdit;
    using Microsoft.AspNetCore.Components;

    namespace dxTestSolution.Blazor.Server.Controllers;

    public class BlazorRichEditController : ViewController<DetailView> {

        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<RichTextPropertyEditor>(this, CustomizeRichTextEditor);
        }

        void CustomizeRichTextEditor(RichTextPropertyEditor propertyEditor) {

            DxRichEditModel richEditModel = propertyEditor.ComponentModel;
            // Specify the View type.
            richEditModel.ViewType = DevExpress.Blazor.RichEdit.ViewType.Simple;

            // Enable spell checker. For more information, refer to the following topic:
            // https://docs.devexpress.com/Blazor/DevExpress.Blazor.RichEdit.SpellCheck.SpellCheckExtensions
            richEditModel.CheckSpelling = true;
            richEditModel.DocumentCulture = "en-US";

            if (propertyEditor.PropertyValue == null) {
                var documentLoadedHandler = richEditModel.DocumentLoaded;
                // Specify the document's font size.
                richEditModel.DocumentLoaded = EventCallback.Factory.Create<DevExpress.Blazor.RichEdit.Document>(this, async document => {
                    await documentLoadedHandler.InvokeAsync(document);
                    await document.ChangeDefaultCharacterPropertiesAsync(properties => {
                        properties.FontSize = 22;
                    });
                    // Specify the paper type.
                    foreach (var section in await document.Sections.GetAllAsync()) {
                        await section.ChangePropertiesAsync(properties => {
                            properties.PaperKind = DXPaperKind.A2;
                        });
                    }
                });
            }
            // Set up the document.
            propertyEditor.CustomizeRichEditDocumentServer += CustomizeDocument;
        }

        void CustomizeDocument(object sender, CustomizeRichEditDocumentServerEventArgs e) {
            e.RichEditDocumentServer.EmptyDocumentCreated += SetupDocument;
        }

        // Specify the document's font size.
        private void SetupDocument(object sender, EventArgs e) {
            RichEditDocumentServer richEditDocumentServer = (RichEditDocumentServer)sender;
            richEditDocumentServer.Document.DefaultCharacterProperties.FontSize = 22;
        }
    }
    ```

## Windows Forms: Access the Rich Text Editor Control

1. In the _Controllers_ folder of the **YourSolutionName.Win** project, create a custom @DevExpress.ExpressApp.ViewController.
2. Add two assemblies to [project references](https://learn.microsoft.com/en-us/visualstudio/ide/managing-references-in-a-project): _DevExpress.SpellChecker.v<:xx.x:>.dll_ and _DevExpress.XtraSpellChecker.v<:xx.x:>.dll_.
3. Override the `OnActivated` method and use the [](xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0})) extension method. Create and set up the @DevExpress.XtraSpellChecker.SpellChecker object and pass this object to the @DevExpress.XtraRichEdit.RichEditControl.SpellChecker property.

    **File:**  
    _YourSolutionName.Win\Controllers\WinRichEditController.cs_

    ```csharp
    using DevExpress.Drawing.Printing;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Office.Win;
    using DevExpress.XtraRichEdit;
    using DevExpress.XtraSpellChecker;

    namespace YourSolutionName.Win;

    public partial class WinRichEditController : ViewController<DetailView> {
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<RichTextPropertyEditor>(this, (propertyEditor) => {
                // Specify the View type.
                propertyEditor.RichEditControl.ActiveViewType = RichEditViewType.Simple;
                // Enable spell checker. For more information refer to the following topic:
                // https://docs.devexpress.com/WindowsForms/9889/controls-and-libraries/rich-text-editor/spell-checking
                SpellChecker spellChecker = new SpellChecker();
                spellChecker.SetSpellCheckerOptions(propertyEditor.RichEditControl, new OptionsSpelling());
                spellChecker.SpellCheckMode = SpellCheckMode.AsYouType;
                propertyEditor.RichEditControl.SpellChecker = spellChecker;
                // Setup the document.
                propertyEditor.RichEditControl.EmptyDocumentCreated += SetupDocument;
            });
        }

        private void SetupDocument(object sender, EventArgs e) {
            RichEditControl richEditControl = (RichEditControl)sender;
            // Specify the font size.
            richEditControl.Document.DefaultCharacterProperties.FontSize = 22;
            // Specify the paper type.
            foreach (var section in richEditControl.Document.Sections) {
                section.Page.PaperKind = DXPaperKind.A2;
            }
        }
    }
    ```

> [!NOTE]  
> The spell checker uses an English dictionary by default. To see how to change the dictionary, refer to the following topic: [Dictionaries](xref:8581).

### Change Toolbar and Ribbon Tab Availability

The `RichTextPropertyEditor` menu does not display all available toolbars and ribbon tabs. Use the static `RichTextPropertyEditor.DefaultRichEditToolbarType` property to customize toolbars. The available toolbars and tabs are listed in the @DevExpress.XtraRichEdit.RichEditToolbarType enumeration.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.XtraRichEdit;
using DevExpress.ExpressApp.Office.Win;
// ...
RichTextPropertyEditor.DefaultRichEditToolbarType = 
    RichEditToolbarType.Home | RichEditToolbarType.Insert | RichEditToolbarType.File | 
    RichEditToolbarType.FloatingObject | RichEditToolbarType.Table | RichEditToolbarType.HeaderFooter;
```
***

Handle the `MenuManagerController.CustomizeRichEditToolbarType` event to change toolbar and tab availability for a single editor:

1. Create a [View Controller](xref:112621#view-controllers) in the [Windows Forms application project](xref:118045) (_YourSolutionName.Win\Controllers_).
2. Access the `MenuManagerController` and subscribe to its `CustomizeRichEditToolbarType` event in the overridden `OnActivated` method.
3. In the event handler, specify the `CustomizeRichEditToolbarTypeEventArgs.RichEditToolbarType` property.

    **File:**  
    _YourSolutionName.Win\Controllers\CustomRichEditController.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Office.Win;
    using DevExpress.XtraRichEdit;

    namespace YourSolutionName.Win.Controllers;

    public class CustomRichEditController : ViewController {
        protected override void OnActivated() {
            base.OnActivated();
            MenuManagerController controller = Frame.GetController<MenuManagerController>();
            if (controller != null) {
                controller.CustomizeRichEditToolbarType += Controller_CustomizeRichEditToolbarType;
            }
        }
        private void Controller_CustomizeRichEditToolbarType(object sender, CustomizeRichEditToolbarTypeEventArgs e) {
            e.RichEditToolbarType = 
                RichEditToolbarType.Home | RichEditToolbarType.Insert | RichEditToolbarType.File | 
                RichEditToolbarType.FloatingObject | RichEditToolbarType.Table | RichEditToolbarType.HeaderFooter;
        }
    }
    ```
    ***

You can also [use the Toolbar Customization menu at runtime](xref:117515). The result is saved to the user's model differences.

### Customize Ribbon Categories and Items

Handle the `CustomizeRibbonControl` event to customize the ribbon. Use the event argument's `RibbonControl` property to access ribbon settings.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Office.Win;
using DevExpress.XtraRichEdit;

namespace YourSolutionName.Win.Controllers;
public class CustomRichEditController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        MenuManagerController controller = Frame.GetController<MenuManagerController>();
        if (controller != null) {
            controller.CustomizeRibbonControl += Controller_CustomizeRibbonControl;
        }
    }
        private void Controller_CustomizeRibbonControl(object sender, CustomizeRibbonControlEventArgs e) {
            BarButtonItem customButton = e.RibbonControl.Items.CreateButton("Test");
            MenuManagerController menuManagerController = (MenuManagerController)sender;
            var defaultCategory = menuManagerController.RibbonObjectsContainer.RichRibbonCategories.FirstOrDefault(t => t.Text == "RichText");
            defaultCategory.Pages[0].Groups[0].ItemLinks.Add(customButton);
        }
}
```

## Use Model Editor to Customize Rich Text Editors

This section demonstrates how to use the [Model Editor](xref:112582) to customize the [Rich Text Property Editor](xref:400004) in a [Windows Forms project](xref:118045).

###  Specify MenuManagerType for a Detail View

The `RichTextPropertyEditor` menu manager can display a [Ribbon Control](xref:2492) or [Bars](xref:5361). 
 
Navigate to the [!include[](~/templates/node_views_detailview_items_propertyeditor111384.md)] node and set the editor's [MenuManagerType](xref:DevExpress.ExpressApp.Office.Win.IModelWinOfficeMenuManagerSettings.MenuManagerType):

![MenuManagerType Property in Model Editor, DevExpress](~/images/richedit-menumanagertype.png)

### Change the Document Storage Format

Set the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's @DevExpress.ExpressApp.Office.IModelRichTextFormatSettings.DocumentStorageFormat property to the desired format (`RTF` or `HTML`) for string properties.

![DocumentStorageFormat Property in Model Editor, DevExpress](~/images/richedit-documentstorageformat.png)

[!include[office-module-properties-for-different-formats](~/templates/office-module-properties-for-different-formats.md)]

### Specify the Editor Height (Embedded Cell Viewer/Editor)

In WinForms applications, the Rich Text Editor's height is fixed and equal to the height of a single-line editor.

To change the editor's height, set the [IModelRichTextColumn.CustomHeight](xref:DevExpress.ExpressApp.Office.Win.IModelRichTextColumn.CustomHeight) property in the [!include[](~/templates/node_views_listview_columns_column111388.md)] node.

Set the `CustomHeight` property to `-1` to allow the grid control to automatically calculate the row height based on the Rich Text Editor's content in WinForms.

![CustomHeight Property in Model Editor, DevExpress](~/images/richedit-customheight.png)
