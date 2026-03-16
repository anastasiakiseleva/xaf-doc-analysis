---
uid: DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled
name: CustomizationFormEnabled
type: Property
summary: Controls runtime layout customization and column chooser for a specific View.
syntax:
  content: |-
    [DefaultValue(true)]
    bool CustomizationFormEnabled { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "`true` to allow runtime customization of View Items' layout and enable column chooser; `false` to disable runtime customization and column chooser."
seealso:
- linkId: DevExpress.Persistent.Base.HideInUI
---
ASP.NET Core Blazor applications support runtime layout customization in Detail Views except for the cases described in the following article: [](xref:404353).

Windows Forms applications support runtime layout customization in Detail Views and Dashboard Views. For more information, refer to the following topic: [](xref:2307).

The column chooser allows users to hide, display, and rearrange columns in a [List Editor](xref:113189) at runtime.

Use the following nodes in [Application Model](xref:112579) to control these options in specific Views:

* **Views** | **\<Namespace\>** | **\<Class\>_DetailView** to control customization and column chooser in a specific Detail View.
* **Views** | **Unspecified** | **\<DashboardView\>** to control customization and column chooser in a specific Dashboard View.

To control these options for the entire application, use the following property: [IModelOptions.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelOptions.CustomizationFormEnabled).

> [!TIP]
> You can combine different flags of the @DevExpress.Persistent.Base.HideInUI attribute to hide a property on select customization forms.