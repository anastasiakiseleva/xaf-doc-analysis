---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelOptionsBlazor.FormStyle
name: FormStyle
type: Property
summary: Specifies whether the standard [Toolbar UI](xref:DevExpress.Blazor.DxToolbar) or [Ribbon UI](xref:DevExpress.Blazor.DxRibbon) is used in the Blazor Application.
syntax:
  content: |-
    [DefaultValue(FormStyle.Standard)]
    FormStyle FormStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.FormStyle
    description: The style of the Blazor Application.
seealso: []
---
To specify the application form style, open the _Model.xafml_ file in the _MySolution.Blazor.Server_ project. In the [Model Editor](xref:112582), navigate to the **Options** node and specify the `FormStyle` property value.

Note that when you create a new application, the `FormStyle` property is explicitly set to `Ribbon`.

![Ribbon UI Setup in Model Editor, DevExpress](~/images/xaf-blazor-form-style-option.png)

> [!ImageGallery]
> ![Ribbon UI](~/images/xaf-blazor-form-style-ribbon.png)
> ![Standard UI](~/images/xaf-blazor-form-style-standard.png)