---
uid: "403446"
title: 'WinForms Application Templates'
owner: Alexey Kazakov
---
# WinForms Application Templates

The **XAF** uses built-in Templates for automatic UI construction. The templates for WinForms applications are listed below.

## Main Form Template (LightStyleMainForm)

![LightStyleMainForm](~/images/lightstylemainform131512.png)

**Class:** `LightStyleMainForm`

**Namespace:** `DevExpress.ExpressApp.Win.Templates.Bars`.

Displays the main Window without excessive borders. To use this template, set the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property to **Standard** and [WinApplication.UseLightStyle](xref:DevExpress.ExpressApp.Win.WinApplication.UseLightStyle) to **true**.


## Main Ribbon Form Template (LightStyleMainRibbonForm)

![LightStyleMainRibbonForm](~/images/lightstylemainribbonform131513.png)

**Class:** `LightStyleMainRibbonForm`

**Namespace:** `DevExpress.ExpressApp.Win.Templates.Ribbon`

Displays the main Window with the [Ribbon](xref:2500) form style without excessive borders. To use this template, set the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property to **Ribbon** and [WinApplication.UseLightStyle](xref:DevExpress.ExpressApp.Win.WinApplication.UseLightStyle) to **true**.


## Detail Form Template (DetailFormV2)

![Contact_DetailView](~/images/contact_detailview115291.png)

**Class:** `DetailFormV2`

**Namespace:** `DevExpress.ExpressApp.Win.Templates.Bars`

Displays a Detail View in a new Window.  To use this template, set the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property to **Standard**.

## Detail Ribbon Form Template (DetailRibbonFormV2)

![DetailRibbonFormTemplate](~/images/detailribbonformtemplate121638.png)

**Class:** `DetailRibbonFormV2`

**Namespace:** `DevExpress.ExpressApp.Win.Templates.Ribbon`

Displays a Detail View in a new Window with the [Ribbon](xref:2500) form style.  To use this template, set the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property to **Ribbon**.

## Popup Form Template (PopupForm)

![PopupFormTemplate](~/images/popupformtemplate115359.png)

**Class:** `PopupForm`

**Namespace:** `DevExpress.ExpressApp.Win.Templates`

Used to display pop-up windows with a Detail View. For instance, a logon form is displayed by the PopupForm Template.

## Nested Frame Template (NestedFrameTemplateV2)

![NestedFrameTemplate](~/images/nestedframetemplate115362.png)

**Class:** `NestedFrameTemplateV2`

**Namespace:** `DevExpress.ExpressApp.Win.Templates.Bars`

Used to display a Window or Frame nested into another Window or Frame. For instance, a List Property Editor or Detail Property Editor's window is displayed by the NestedFrameTemplateV2 Template.

## Lookup Form Template (LookupForm)

![LookupFormTemplate](~/images/lookupformtempalte115360.png)

**Class:** `LookupForm`

**Namespace:** `DevExpress.ExpressApp.Win.Templates`

Used to display pop-up windows with a List View. For instance, PopupWindowShowAction type Actions use the LookupForm Template to display their pop-up window.

## Lookup Control Template (LookupControlTemplate)

![LookupControlTemplate](~/images/lookupcontroltemplate115361.png)

**Class:** `LookupControlTemplate`

**Namespace:** `DevExpress.ExpressApp.Win.Templates`

Used to display a Lookup Property Editor's drop down window.

## Logon Window Template (LogonPopupForm)

**Class:** `LogonPopupForm`

**Namespace:** `DevExpress.ExpressApp.Win.Templates`

Defines the logon window layout and appearance.


## OutlookStyleMainRibbonForm 

![OutlookStyleMainRibbonForm](~/images/outlookstylemainribbonform123038.png)

**Class:** `OutlookStyleMainRibbonForm`

**Namespace:** `DevExpress.ExpressApp.Win.Templates.Ribbon`

Used to display the main Window with the Outlook form style. To use this template, apply settings as the [IModelRootGroupsStyle.RootGroupsStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelRootGroupsStyle.RootGroupsStyle) article describes, and set the **RootGroupStyle** property to **OutlookSimple** or **OutlookAnimated**.

## Deprecated Templates

### MainFormV2

![MainFormTemplate](~/images/mainformtemplate115363.png)

**Class:** `MainFormV2`

**Namespace:** `DevExpress.ExpressApp.Win.Templates`

Displays the main Window. To use this template, set the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property to **Standard**.

### MainRibbonFormV2

![MainRibbonFormV2](~/images/mainribbonformtemplate121637.png)

**Class:** `MainRibbonFormV2`

**Namespace:** `DevExpress.ExpressApp.Win.Templates.Bars`

Displays the main Window with the [Ribbon](xref:2500) form style. To use this template, set the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property to **Ribbon**.


> [!NOTE]
> Refer to the [](xref:404212) topic to learn how to toggle a Ribbon user interface in your WinForms application.


## How To's

- [](xref:115213)
- [](xref:113443)
- [](xref:115214)
- [](xref:112618)
- [](xref:113706)
- [](xref:117231)
- [](xref:113253)
- [](xref:118084)
