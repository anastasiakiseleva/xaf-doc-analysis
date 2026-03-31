---
uid: "404762"
title: Accessibility Support
---
# Accessibility Support

XAF UI for ASP.NET Core Blazor and WinForms platforms offers partial accessibility support at the same level as the corresponding DevExpress controls for the respective UI platforms:

* [DevExpress ASP.NET Core Blazor](xref:404749)
* [DevExpress WinForms](xref:404293)
* [DevExpress DevExtreme](xref:js-DevExtreme.Guide.Common.Accessibility) (DevExtreme UI controls are used in XAF ASP.NET Core Blazor UI.)

XAF includes its own UI components and elements. As of v24.1, **XAF Blazor UI** components have been assessed for accessibility conformance and updated to meet additional accessibility criteria (see [Accessibility in XAF UI for ASP.NET Core Blazor](#accessibility-in-xaf-ui-for-aspnet-core-blazor)).

Accessibility assessments and enhancements for WinForms UI components are scheduled for 2024.

## Accessibility Standards and Guidelines

Many XAF Blazor UI components comply with [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Level AA), [Section 508](https://www.access-board.gov/ict/), and [EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.01.01_60/en_301549v030101p.pdf) standards. To learn more about how XAF Blazor UI components satisfy these requirements, refer to the DevExpress Accessibility Conformance Report (ACR). 

[!download[DevExpress XAF for ASP.NET Core Blazor ACR v24.1(based on VPAT®)](https://www.devexpress.com/products/net/accessibility/ACR-DevExpress-XAF-Blazor-24.1.pdf)]

## Accessibility in XAF UI for ASP.NET Core Blazor

### Accessibility Conformance of Underlying UI Libraries

XAF UI for ASP.NET Core Blazor is built on top of Blazor-compatible DevExpress UI libraries. For information on compatibility conformance in these libraries, refer to their respective documentation sections:

- [Blazor Components - Accessibility](xref:404749)
- [DevExpress DevExtreme - Accessibility](xref:js-DevExtreme.Guide.Common.Accessibility) (DevExtreme UI controls are used in XAF ASP.NET Core Blazor UI.)
- [Accessibility in Reporting for Web](xref:402561)

### Accessibility Conformance of XAF-Specific Features and Components

<!-- ## Accessibility Conformance Report 

_(Checked, hidden until ACRs are published)_

The accessibility conformance report for XAF UI for ASP.NET Core Blazor is based on [VPAT® Version 2.5](https://www.itic.org/policy/accessibility/vpat). It includes sections corresponding to leading ICT accessibility standards: Section 508 (U.S.), EN 301 549 (EU), and W3C/WAI WCAG.

[!download[ACR-DevExpress-Blazor-23.2](todo)] -->

The table below lists XAF-specific features and components, along with their accessibility conformance status.

✅ - The feature or component fully conforms to related accessibility requirements.

⚠️ - The feature or component partially conforms to related accessibility requirements (exceptions are listed).

{|
|-
! Feature / Component 
! Accessibility Support
! Comments
|-
| Header Buttons
| ✅
| All buttons displayed in the page header have localizable labels and tooltips; buttons use focus frames that look consistent with the rest of the UI.
|-
| Image Editor
| ⚠️
| The Image Editor component supports accessibility on the following levels: 
- The displayed image has alternative text.
- The editor's _"Change Image"_ button has a title and tooltip detectable by assistive technology.
- The editor supports keyboard navigation with some exceptions (see the _Keyboard Navigation_ section below).
|-
| Keyboard Navigation
| ⚠️
| XAF Blazor UI supports keyboard navigation with the following exceptions:
- The Detail View layout customization window does not support keyboard navigation. 
- The Image Editor component loses focus after the displayed image is modified or removed. 
- It is impossible to focus and press the _Customize_ button in the grid column chooser using a keyboard interface. 
- The vertical splitter displayed in master-detail mode cannot be operated (moved to the right or left) using a keyboard.
|-
| Navigation
| ✅
| The navigation pane fully supports keyboard navigation and assistive technology.
|-
| Page Markup
| ✅
| The main page markup includes the global `lang` attribute. The page title reflects the purpose of the active view. The page contains an initially hidden _"Skip to main content"_ link, which is the first to be focused when a user presses the 'Tab' key.
|-
| Popups
| ✅
| Popups support keyboard navigation and assistive technology. Popups can be closed by the 'Esc' key press.
|-
| Property Editors
| ✅
| ARIA labels for property editors correctly reflect validation statuses and error messages.
|-
| Settings Menu
| ✅
| The "Settings" Menu supports accessibility on the following levels:
- Each `<nav>` element in the menu's layout has a label.
- The _Settings_ menu obtains a `visibility: hidden` style when collapsed to avoid unnecessary focusing.
- The _Settings_ menu can be closed by the 'Esc' key press.
|}
