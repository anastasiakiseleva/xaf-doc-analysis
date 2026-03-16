---
uid: DevExpress.ExpressApp.Win.WinApplication.UseLightStyle
name: UseLightStyle
type: Property
summary: Enables the Light Style in a WinForms application.
syntax:
  content: |-
    [Browsable(false)]
    public bool UseLightStyle { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the Light Style is enabled for a WinForms application; otherwise, **false**.'
seealso: []
---
The **UseLightStyle** property is bound to [](xref:DevExpress.XtraEditors.WindowsFormsSettings.DockingViewStyle). 

| UseLightStyle value | WindowsFormsSettings.DockingViewStyle value |
|---|---|
| true | DockingViewStyle.Light |
| false | DockingViewStyle.Default |

The [Template Kit](xref:405447) enables the Light Style for all new XAF WinForms applications. [!include[default_settings_compatibility_mode_set_to_latest](~/templates/default_settings_compatibility_mode_set_to_latest.md)] 

The Light Style uses the following [templates](xref:112609):

* **LightStyleMainForm** - in applications with the Standard UI;
* **LightStyleMainRibbonForm** - in applications with the Ribbon UI.

The image below demonstrates the difference between a Layout with enabled and disabled Light Style:

![UseLightStyle_ListView](~/images/uselightstyle_listview131510.png)

The **UseLightStyle** property affects which built-in Controller XAF uses: the [ChooseSkinController](xref:113141#chooseskincontroller) or the [ConfigureSkinController](xref:113141#configureskincontroller).

| UseLightStyle value | Built-in Controller |
|---|---|
| true | ConfigureSkinController |
| false | ChooseSkinController |

The **ConfigureSkinController** provides new WinForms [skin](xref:DevExpress.ExpressApp.Win.SystemModule.IModelApplicationOptionsSkin.Skin) and [palette](xref:DevExpress.ExpressApp.Win.SystemModule.IModelApplicationOptionsPalette.Palette) runtime [skin selectors](xref:2399) for [Bar UI](xref:2500) and [Ribbon UI](xref:5361).


| WinForms UI | Skin selector | Palette selector |
|---|---|---|
| Bar UI | SkinDropDownButtonItem | BarButtonItem with a Dropdown Gallery |
| Ribbon UI | SkinDropDownButtonItem | SkinPaletteRibbonGalleryBarItem |

**Bar UI**

![WinForms-BarUI-LightStyle-SkinPaletteSelector](~/images/WinForms-BarUI-LightStyle-SkinPaletteSelector.png)

**Ribbon UI**

![WinForms-RibbonUI-SkinPaletteSelector](~/images/WinForms-RibbonUI-LightStyle-SkinPaletteSelector.png)

If you want to enable the Light Style for an existing application, refer to the [How to migrate a WinForms application to use the Light Style](https://supportcenter.devexpress.com/Ticket/Details/T577264/how-to-migrate-a-winforms-application-to-use-the-light-style) KB article. 
