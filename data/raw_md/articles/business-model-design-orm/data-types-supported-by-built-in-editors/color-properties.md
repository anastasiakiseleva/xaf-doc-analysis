---
uid: "113658"
seealso:
- linkId: "402188"
title: Color Properties
---
# Color Properties

XAF displays the @System.Drawing.Color and `Nullable<Color>` properties using a combo box (ASP.NET Core Blazor) or a drop-down window with a color table / color picker (Windows Forms).

## Examples
* [Color Properties in XPO](xref:113659)
* [Color Properties in EF Core](xref:113660)

## ASP.NET Core Blazor

XAF's ASP.NET Core Blazor UI implements `ColorPropertyEditor` to display @System.Drawing.Color properties.

![XAF Color Properties ASP.NET Core Blazor, DevExpress](~/images/blazor-color-properties-editor-devexpress.png)

[!include[blazor-editor-descendants](~/templates/blazor-editor-descendants.md)]

The following code snippet applies a custom CSS class to all `ColorPropertyEditor` controls in the application.

```csharp{7,9-10}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;

namespace YourSolutionName.Blazor.Server.Controllers;
public class CustomizeColorPropertiesController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<ColorPropertyEditor>(this, editor => {
            editor.ComponentModel.CssClass = "myCustomCss";
        });
    }
}
```

## Windows Forms

XAF's Windows Forms UI implements `ColorPropertyEditor` to display @System.Drawing.Color properties.

![XAF Color Properties WinForms](~/images/coloreditor_winforms117528.png)

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

{|
|-
! Control
! Repository Item
! Description
|-
| [](xref:DevExpress.XtraEditors.ColorEdit)
| [](xref:DevExpress.XtraEditors.Repository.RepositoryItemColorEdit)
| Displays @System.Drawing.Color properties. Use Alt + Down Arrow to expand the editor's drop-down window.
|}
