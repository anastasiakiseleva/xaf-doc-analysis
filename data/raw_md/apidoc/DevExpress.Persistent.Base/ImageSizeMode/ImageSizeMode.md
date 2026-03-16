---
uid: DevExpress.Persistent.Base.ImageSizeMode
name: ImageSizeMode
type: Enum
summary: Contains values that specify image size modes for images displayed by Image Property Editors.
syntax:
  content: public enum ImageSizeMode
seealso:
- linkId: "112792"
- linkId: "404209"
---
These enumeration values are used to set the [ImageEditorAttribute.ImageSizeMode](xref:DevExpress.Persistent.Base.ImageEditorAttribute.ImageSizeMode) property.

You can specify the appropriate value in the [Model Editor](xref:112582).

![SizeMode](~/images/SizeMode.png)

If you intend to customize an SVG image with [SvgImageHeight](xref:DevExpress.ExpressApp.Model.IModelStaticImage.SvgImageHeight) and [SvgImageWidth](xref:DevExpress.ExpressApp.Model.IModelStaticImage.SvgImageWidth) properties, choose the **AutoSize**, **CenterImage**, or **Normal** value.