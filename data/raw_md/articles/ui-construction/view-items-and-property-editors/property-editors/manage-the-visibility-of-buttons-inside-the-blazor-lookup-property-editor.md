---
uid: "403870"
title: 'Manage Button Visibility in a Blazor Lookup Property Editor'
owner: Yekaterina Kiseleva
seealso:
- linkId: "112908"
---
# Manage Button Visibility in a Blazor Lookup Property Editor

XAF manages the visibility of **New** and **Edit** buttons inside an ASP.NET Core Blazor Lookup Property Editor according to Security System permissions, business object settings, and Action parameters.

Lookup Property Editor in a Detail View
:   ![|The Edit and New buttons in the Blazor Lookup Property Editor in Detail View](~/images/LookupActionVisibility.png)

Lookup Property Editor in a List View with in-place editing enabled
:   ![|The Edit and New buttons in the Blazor Lookup Property Editor in List View](~/images/LookupActionVisibility-ListView-InPlace-Editing.png)

Call the following `LookupPropertyEditor` methods to hide or display these buttons:

`HideNewButton`
:   Hides the **New** button.
`HideEditButton`
:   Hides the **Edit** button.
`ResetNewButtonVisibility`
:   Displays the hidden **New** button.
`ResetEditButtonVisibility`
:   Displays the hidden **Edit** button.

> [!NOTE]
> The **Edit** button acts as a clickable link. Use Ctrl + click or click the middle mouse button to open the referenced object in a new browser tab. To disable this behavior, add a Controller to your application, as described in the following topic: [Hide Hyperlinks in Lookup Controls](xref:113572#hide-hyperlinks-in-lookup-controls).

## In a Detail View

The following code snippet uses Actions to manage lookup editor button visibility:

[!include[<MySolution.Blazor.Server\Controllers\LookupActionVisibilityController.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.Persistent.Base;
// ...
public class LookupActionVisibilityController : ViewController<DetailView> {
    public LookupActionVisibilityController() {
        SimpleAction hideNewAction = new SimpleAction(this, "Hide New", PredefinedCategory.Edit);
        SimpleAction hideEditAction = new SimpleAction(this, "Hide Edit", PredefinedCategory.Edit);
        SimpleAction resetNewAction = new SimpleAction(this, "Reset New", PredefinedCategory.Edit);
        SimpleAction resetEditAction = new SimpleAction(this, "Reset Edit", PredefinedCategory.Edit);
        hideNewAction.Execute += (s, e) => {
            View.CustomizeViewItemControl<LookupPropertyEditor>(this, e => {
                e.HideNewButton();
            });
        };
        hideEditAction.Execute += (s, e) => {
            View.CustomizeViewItemControl<LookupPropertyEditor>(this, e => {
                e.HideEditButton();
            });
        };
        resetNewAction.Execute += (s, e) => {
            View.CustomizeViewItemControl<LookupPropertyEditor>(this, e => {
                e.ResetNewButtonVisibility();
            });
        };
        resetEditAction.Execute += (s, e) => {
            View.CustomizeViewItemControl<LookupPropertyEditor>(this, e => {
                e.ResetEditButtonVisibility();
            });
        };
    }
}
```
***

[`SimpleAction`]: xref:DevExpress.ExpressApp.Actions.SimpleAction
[`ViewController`]: xref:DevExpress.ExpressApp.ViewController`1
[`Execute`]: xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute
[`CustomizeViewItemControl`]: xref:DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[])
[`View`]: xref:DevExpress.ExpressApp.ViewController.View

If you do not need to create additional Actions as shown in the code sample above, call `HideNewButton` and `HideEditButton` in the Controller's `OnActivated` method to hide the **New** and **Edit** buttons unconditionally.

> [!NOTE]
> These changes will apply to Detail View and List View when [in-place editing](xref:113249#in-place-editing) is enabled. To apply the changes for a particular View, use the @DevExpress.ExpressApp.Blazor.Utils.BlazorViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Controller,System.Action{``0}) method.

[!include[<MySolution.Blazor.Server\Controllers\LookupActionVisibilityController.cs>](~/templates/platform_specific_file_path.md)]

[!include[blazorutils-customizeviewitemcontrol-1](~/templates/blazorutils-customizeviewitemcontrol-1.md)]
