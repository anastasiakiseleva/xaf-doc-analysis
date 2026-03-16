---
uid: DevExpress.Persistent.Base.ObjectCaptionFormatAttribute
name: ObjectCaptionFormatAttribute
type: Class
summary: Specifies a caption format for the target business class' objects.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Interface, Inherited = true, AllowMultiple = false)]
    public class ObjectCaptionFormatAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.ObjectCaptionFormatAttribute._members
  altText: ObjectCaptionFormatAttribute Members
---
Currently, business object captions are only used for captions of the corresponding detail forms. By default, a caption format is specified by the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** node's [IModelClass.ObjectCaptionFormat](xref:DevExpress.ExpressApp.Model.IModelClass.ObjectCaptionFormat). This property's value is formed from the **BOModel** | **_\<Class\>_** node's [IModelClass.FriendlyKeyProperty](xref:DevExpress.ExpressApp.Model.IModelClass.FriendlyKeyProperty) and/or [IModelClass.DefaultProperty](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultProperty) properties.

![Tutorial_UIC_Lesson3_1](~/images/tutorial_uic_lesson3_1115477.png)

You can set a custom caption format directly in the Application Model via the [Model Editor](xref:112582). In addition, you can do it in code. For this purpose, apply the **ObjectCaptionFormat** attribute to the required business class. Specify the caption format as the attribute's [ObjectCaptionFormatAttribute.FormatString](xref:DevExpress.Persistent.Base.ObjectCaptionFormatAttribute.FormatString) parameter. This format will be set for the **ObjectCaptionFormat** property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** node, where it can be changed. The format specifyed in the Application Model will be used in the UI.

> [!NOTE]
> By default, the caption format set for a business class via the **ObjectCaptionFormat** attribute is set for its descendants as well.