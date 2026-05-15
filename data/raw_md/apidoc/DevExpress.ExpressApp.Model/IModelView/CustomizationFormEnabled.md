---
uid: DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled
name: CustomizationFormEnabled
type: Property
summary: Enables/disables runtime layout customization and Column Chooser / Field List for a specific View.
syntax:
  content: |-
    [DefaultValue(true)]
    bool CustomizationFormEnabled { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "`true` to allow runtime customization of View Items' layout and enable Column Chooser / Field List; otherwise `false`."
seealso:
- linkId: DevExpress.Persistent.Base.HideInUI
- linkId: "404353"
- linkId: "2307"
---
XAF applications support runtime layout customization in Detail Views, List Views, and Dashboard Views. Additionally, the following customization forms are available:

* The **Column Chooser** allows users to hide, display, and rearrange columns in a [List Editor](xref:113189) at runtime.
* The **Field List** allows users to manage component structure in the Pivot Grid List Editor.

Use the `CustomizationFormEnabled` property to control availability of runtime layout customization and customization forms.

Use the following nodes in [Application Model](xref:112579) to control these options in specific Views:

* **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView**
* **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_DetailView**

To control these options for the entire application, use the [IModelOptions.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelOptions.CustomizationFormEnabled) property.

> [!TIP]
> You can combine different flags of the @DevExpress.Persistent.Base.HideInUI attribute to hide a property on select customization forms.