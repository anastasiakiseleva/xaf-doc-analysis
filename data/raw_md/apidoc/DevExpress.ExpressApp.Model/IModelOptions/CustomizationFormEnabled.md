---
uid: DevExpress.ExpressApp.Model.IModelOptions.CustomizationFormEnabled
name: CustomizationFormEnabled
type: Property
summary: Enables/disables runtime layout customization and Column Chooser / Field List for the entire application.
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

Use the `CustomizationFormEnabled` property of the **Options** node in the [Application Model](xref:112579) to control availability of runtime layout customization and customization forms.

To control these options for a specific View, use the following property: [IModelView.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled).

> [!TIP]
> You can combine different flags of the @DevExpress.Persistent.Base.HideInUI attribute to hide a property on certain customization forms.
