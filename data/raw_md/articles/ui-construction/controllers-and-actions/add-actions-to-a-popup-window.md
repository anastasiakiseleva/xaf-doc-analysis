---
uid: "112804"
title: Add Actions to a Pop-up Window
seealso:
- linkId: "402128"
- linkId: "112609"
- linkId: "112610"
- linkId: "112618"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_how-to-add-custom-buttons-actions-to-the-lookup-and-popup-windows
  altText: 'GitHub Example: XAF - Add Custom Buttons (Actions) to Lookup and Popup Windows'
---
# Add Actions to a Pop-up Window

A pop-up Window can contain a Detail or List [View](xref:112611) and [Actions](xref:112622). Actions are displayed by [Action Containers](xref:112610). If you need to add an action to a pop-up window, add it to the action container of a corresponding template. This topic describes which built-in templates are used to display pop-up windows. For instructions on how to display a window in response to an action, refer to the following topic: [Ways to Show a View](xref:112803).

The following table shows Action Container availability in built-in pop-up templates:

{|
|-

! Template name
! Platform
! Action Containers
|-

| `PopupWindowTemplate`
| ASP.NET Core Blazor
| `ObjectsCreation`  

`FullTextSearch`  

`Diagnostic`  

`PopupActions`  

`Search`  

`Filters`
|-

| `PopupForm`
| Windows Forms
| `ObjectsCreation`  

`Diagnostic`

`PopupActions`

`RecordEdit`

`View`

`Print`

`OpenObject`

`UndoRedo`

`Export`
|-

| `LookupForm`
| Windows Forms
| `ObjectsCreation`  

`FullTextSearch`  

`Diagnostic`  

`PopupActions`
|-

| `DialogTemplateContent`
|}
