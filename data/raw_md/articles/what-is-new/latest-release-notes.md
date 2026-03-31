---
uid: '405329'
title: 'v25.2 Release Notes'
seealso:
- linkId: 405330
---
# v25.2 Release Notes

> [!Tip]
> Visit our website to explore new features/capabilities available across the entire DevExpress product line: [What's New in our Latest Update](https://www.devexpress.com/subscriptions/whats-new/).

## .NET 10 and Visual Studio 2026 Support

XAF Blazor/WinForms UI and Web API Service now support .NET 10 and Visual Studio 2026.

[Microsoft Downloads](https://visualstudio.microsoft.com/)

## XAF No Longer Supports Microsoft's .NET Framework (WebForms/WinForms)

[As documented in our Roadmap](https://community.devexpress.com/blogs/xaf/archive/2025/08/15/xaf-cross-platform-net-app-ui-and-web-api-service-year-end-roadmap-v25-2.aspx) (published in August 2025), v25.2+ marks the official end of XAF WebForms & WinForms .NET Framework support. We also removed all XAF .NET Framework and legacy .NET modules/APIs, and older/deprecated Security System implementations from our source code.

Moving forward, we will focus our efforts on .NET (Blazor & WinForms & Web API Service) and scalable, multi-tenant/SaaS-based apps. We will also ship security and other critical fixes for v25.1.XX minor builds (.NET Framework 4.8) for as long as we can. 

[Migration Guidelines](xref:405693) | [Future Plans](https://community.devexpress.com/blogs/xaf/archive/2025/08/15/xaf-cross-platform-net-app-ui-and-web-api-service-year-end-roadmap-v25-2.aspx)

## Cross-IDE Project and Item Template Kit (.NET | Windows | macOS)

With v25.2, DevExpress Template Kit is fully integrated into JetBrains Rider (including macOS support). You can create new projects and items using the same set of DevExpress templates already available in Visual Studio and VS Code.

The new Template Kit also ships with our Unified Component Installer and replaces our legacy XAF Solution Wizard. 
The "DevExpress 25.2 Template Kit" item is available within the following Visual Studio 2022+ dialogs:
- File → New → Project 
- Add → New Item/Add → Class

[Documentation](xref:405447)

![Template Kit](~/images/what-s-new/xaf-template-kit.png)

## XPO ORM - Connection Provider Updates

We now support the most recent versions of the following database engines (for both .NET and .NET Framework):

- PostgreSQL 18.0
- Microsoft SQL Server 2025

[Documentation](xref:2114)

## DevExpress MCP Server for AI-Powered Documentation Access

We introduced an MCP server that connects GitHub Copilot Chat, Cursor, and other MCP-compatible AI tools directly to our comprehensive documentation database. The server provides instant access to over 300,000 help topics through natural language queries within your IDE. This allows you and AI coding agents such as Claude Code to access current DevExpress documentation directly within the AI assistant's context. 

[Documentation](xref:405551) | [Blog Post](https://community.devexpress.com/Blogs/news/archive/2025/10/16/transform-your-development-experience-with-the-devexpress-mcp-server.aspx)

![|Documentation MCP Server|](~/images/what-s-new/dx-mcp-docs-assistant.png)

## XAF Blazor UI Enhancements

### Middle Tier Security: Official Release/RTM

[XAF Blazor](https://demos.devexpress.com/XAF/BlazorMainDemo) now supports [Middle Tier Security](xref:404389) for secure communication between the frontend and backend, helping to protect sensitive data and enforce stricter access controls.

[General Security Considerations](xref:404691) | [Security-Related Blog Posts](https://community.devexpress.com/Tags/access+control)

### Fluent Themes and Icons: Official Release/RTM

We released Dark and Light Fluent Themes for XAF Blazor v25.2 and expanded our SVG icon pack with colorful XAF-specific icons that match the Fluent Theme and its dark/light palettes.
You can now set the [Primary Accent Color](xref:405530#primary-accent-color-select-from-the-predefined-palette) using our Theme Chooser.

![Fluent images in the Image Picker](~/images/what-s-new/xaf-blazor-image-picker.png)

![Fluent Theme Chooser](~/images/what-s-new/xaf-blazor-theme-chooser.png)

### Ribbon UI Support

With XAF v25.2, you can display the application main menu as a Ribbon UI (combined with a Tabbed MDI by default). Our implementation supports Ribbon UI command merge operations: XAF Controller's Actions are processed across main and detail form templates (just like our XAF WinForms implementation).

![Ribbon UI](~/images/what-s-new/xaf-blazor-ribbon-ui.png)

Open the Model Editor and set the [IModelOptionsBlazor.FormStyle](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.FormStyle) property to `Ribbon` to activate this feature. You can use the new **ActionDesign | ActionToRibbonMapping** node to customize the Ribbon's structure.

![Model Editor Ribbon Customization](~/images/what-s-new/xaf-blazor-ribbon-model-editor.png)

### Native Blazor Filter Builder Integration (CTP)

v25.2 ships with our new CriteriaPropertyEditor (available as a Community Technology Preview). CriteriaPropertyEditor uses the new [DevExpress Blazor Filter Builder](xref:DevExpress.Blazor.DxFilterBuilder) component and supports simpler localization, better performance, and native Blazor themes/palettes. 

You can manually activate and test the CriteriaPropertyEditor in the Model Editor or in code. We hope to replace our existing JS-based FilterPropertyEditor with the new CriteriaPropertyEditor in v26.1. 

![CriteriaPropertyEditor](~/images/what-s-new/xaf-blazor-criteriapropertyeditor.png)

<!--### TODO Configure XAF Report Data Sources within the Blazor Report Designer-->

## Cross-Platform Property and List Editor Enhancements (XAF Blazor and WinForms UI)

### TagBox, ComboBox, and Progress Bar Property Editors: Official Release/RTM

v25.2 includes the official release of our TagBox, ComboBox, and Progress Bar Property Editors.
TagBox and checked ComboBox are two popular options if you need to save space in detail forms (for collection data and as an alternative to large data grids).
Progress Bar displays the progress of an operation in both List and Detail Views (now supports inline-editing).

[TagBoxListPropertyEditor](xref:113568#tagboxlistpropertyeditor) | [ComboBoxListPropertyEditor](xref:113568#comboboxlistpropertyeditor) | [ProgressBarPropertyEditor](xref:113532#progressbarpropertyeditor)

![TagBox](~/images/what-s-new/25-2-xaf-new-built-in-property-editors.png)
![ComboBox](~/images/what-s-new/xaf-combobox.png)
![ProgressBar](~/images/what-s-new/25.2-progress-bar-property-editor.png)

### PDF Viewer Property Editors: Official Release/RTM

In our v25.1 release cycle, we introduced the [PDF Viewer Property Editors](xref:405488) as a Community Technology Preview (CTP) for XAF Blazor and XAF WinForms. v25.2 marks its official release, complete with new customization options designed to enhance usability and flexibility within your WinForms applications. New features include:

* **Customizable Ribbon and Toolbar.** The WinForms PDF Viewer allows you to display the command interface as a Ribbon, Toolbar, or hide it entirely. You can also customize the available command set as requirements dictate.

* **Open in a Separate Window.** A new context menu option opens the PDF Viewer in a standalone window for a more focused viewing experience.

* **PDF Field Editing**. The WinForms PDF Viewer now allows you to edit fillable form fields and save these changes to the database.

![PDF Viewer](~/images/what-s-new/xaf-win-pdf-viewer-menu-type-ribbon.png)

[Documentation](xref:405489)

<!--### TODO Windows/macOS Desktop Support via Blazor UI & Electron.NET -->

<!--### TODO AI-related Enhancements-->

### Simplified Access to Column Settings for Grid List Editors

You can write platform-agnostic code (see below) or access platform-specific column settings via `ColumnWrapper` descendants:

```csharp
protected override void OnViewControlsCreated() {
    base.OnViewControlsCreated();
    if (View.Editor is ColumnsListEditor listEditor) {
        foreach (var column in listEditor.Columns) {
            column.ShowInCustomizationForm = false;
        }
    }
}
```