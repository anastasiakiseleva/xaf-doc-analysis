---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle
name: FormStyle
type: Property
summary: Specifies whether the Standard [Bar UI](xref:5361) or [Ribbon UI](xref:2492) is used in the Windows Forms Application.
syntax:
  content: |-
    [DefaultValue(RibbonFormStyle.Standard)]
    RibbonFormStyle FormStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.XtraBars.Ribbon.RibbonFormStyle
    description: '`Standard` to display [Bars UI](xref:5361); `Ribbon` to display the [Ribbon UI](xref:2492).'
seealso:
- linkId: "404212"
---
To specify the application form style, open the _Model.xafml_ file in the _MySolution.Win_ project. In the [Model Editor](xref:112582), navigate to the **Options** node and specify the `FormStyle` property value.

![Ribbon UI Setup in Model Editor, DevExpress](~/images/xaf-win-form-style-in-model-editor.png)

Result:

> [!ImageGallery]
> ![Ribbon UI](~/images/xaf-win-form-style-ribbon.png)
> ![Standard UI](~/images/xaf-win-form-style-standard.png)
