---
uid: "403450"
title: 'Blazor Application Templates'
---
# Blazor Application Templates

XAF uses built-in Templates to build the application UI. 

 The sections below describe built-in templates for Blazor applications.

## Main Form Template (ApplicationWindowTemplate)

Defines the main window's layout and appearance when the application displays the standard UI (the @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.FormStyle property is set to `Standard`).

**Template:** `DevExpress.ExpressApp.Blazor.Templates.ApplicationWindowTemplate`  
**Template Content:** `DevExpress.ExpressApp.Blazor.Templates.ApplicationWindowTemplateComponent`

![XAF ASP.NET Core Blazor Application Window Template, DevExpress](~/images/xaf-blazor-application-window-template.png)

## Main Ribbon Form Template (ApplicationRibbonWindowTemplate)

Defines the main window's layout and appearance when the application displays the ribbon UI (the @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.FormStyle property is set to `Ribbon`).

**Template:** `DevExpress.ExpressApp.Blazor.Templates.ApplicationRibbonWindowTemplate`  
**Template Content:** `DevExpress.ExpressApp.Blazor.Templates.ApplicationRibbonWindowTemplateComponent`

![XAF ASP.NET Core Blazor Application Window Template, DevExpress](~/images/xaf-blazor-application-ribbon-window-template.png)

## Detail Form Template (DetailFormTemplate)

Defines a tab content's layout and appearance in TabbedMDI mode when the application displays the standard UI (the @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.UIType property is set to `TabbedMDI` and the @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.FormStyle property is set to `Standard`).

**Template:** `DevExpress.ExpressApp.Blazor.Templates.DetailFormTemplate`  
**Template Content:** `DevExpress.ExpressApp.Blazor.Templates.DetailFormTemplateComponent`

![XAF ASP.NET Core Blazor Detail Form Template, DevExpress](~/images/xaf-blazor-detail-form-template.png)

## Detail Ribbon Form Template (DetailRibbonFormTemplate)

Defines a tab content's layout and appearance in TabbedMDI mode when the application displays the ribbon UI (the @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.UIType property is set to `TabbedMDI` and the @DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.FormStyle property is set to `Ribbon`).

**Template:** `DevExpress.ExpressApp.Blazor.Templates.DetailRibbonFormTemplate`  
**Template Content:** `DevExpress.ExpressApp.Blazor.Templates.DetailRibbonFormTemplateComponent`

![XAF ASP.NET Core Blazor Detail Form Template, DevExpress](~/images/xaf-blazor-detail-ribbon-form-template.png)

## Logon Window Template (LogonWindowTemplate)

Defines the logon window layout and appearance.

**Template:** `DevExpress.ExpressApp.Blazor.Templates.LogonWindowTemplate`  
**Template Content:** `DevExpress.ExpressApp.Blazor.Templates.LogonWindowTemplateComponent`

![XAF ASP.NET Core Blazor Logon Window Template, DevExpress](~/images/xaf-blazor-logon-window-template.png)

## Nested Frame Template (NestedFrameTemplate)

Defines the nested frames' layout and appearance.

**Template:** `DevExpress.ExpressApp.Blazor.Templates.NestedFrameTemplate`  
**Template Content:** `DevExpress.ExpressApp.Blazor.Templates.NestedFrameTemplateComponent`

![XAF ASP.NET Core Blazor Nested Frame Template, DevExpress](~/images/xaf-blazor-nested-frame-template.png)

## Popup Window Template (PopupWindowTemplate)

Defines the popup window layout and appearance. Examples: [](xref:404014).

**Template:** `DevExpress.ExpressApp.Blazor.Templates.PopupWindowTemplate`  
**Template Content:** `DevExpress.ExpressApp.Blazor.Templates.PopupWindowTemplateComponent`

![XAF ASP.NET Core Blazor Popup Window Template, DevExpress](~/images/xaf-blazor-popup-window-template.png)

## Examples

* <xref:112696>
* <xref:403452>
* <xref:404014>
* <xref:404978>
<!--* <xref:405643>-->