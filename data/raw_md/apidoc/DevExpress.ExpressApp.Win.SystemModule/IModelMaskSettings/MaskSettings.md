---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelMaskSettings.MaskSettings
name: MaskSettings
type: Property
summary: Specifies mask settings for a [Property Editor](xref:113097)'s control in the [Application Model](xref:112580).
syntax:
  content: |-
    [ModelBrowsable(typeof(MaskSettingsVisibilityCalculator))]
    string MaskSettings { get; set; }
  parameters: []
  return:
    type: System.String
    description: Mask settings for a [Property Editor](xref:113097)'s control.
seealso: []
---
The **MaskSettings** property is available in **WinForms** application projects.

Use the [Model Editor](xref:112582) to set the **MaskSettings** property value. In the Model Editor, select a View Item node that has a Property Editor. Find the **MaskSettings** option for this node. Click the ellipsis button in the **MaskSettings** editor to invoke the _Mask Settings_ dialog.

![Open the Mask Settings dialog](~/images/mask-settings.png)

Select the required mask type and choose one of the predefined expressions. You can also define a custom mask expression. See the following topic for more information: [How to Apply Masks](xref:583#how-to-apply-masks).

![Mask Settings](~/images/mask-settings-dialog.png)

> [!NOTE]
> The **MaskSettings** property does not prohibit users from saving an incorrect value to a database (for example, when they do not fill all the required digits in a phone number). Configure [Validation](xref:113684) settings to prevent data errors.