---
uid: DevExpress.Persistent.Base.ImageNameAttribute
name: ImageNameAttribute
type: Class
summary: Specifies the name of the image that is displayed for the target class' objects or target enumeration value.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Field | AttributeTargets.Interface, Inherited = false)]
    public class ImageNameAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.ImageNameAttribute._members
  altText: ImageNameAttribute Members
---
In XAF applications, you can associate business objects with images. For instance, these images are displayed in detail form headers. To assign an image to a particular business class, apply the **ImageName** attribute to this class. Pass the name of the required image as the attribute's _imageName_ parameter. This parameter's value will be set for the [IModelClass.ImageName](xref:DevExpress.ExpressApp.Model.IModelClass.ImageName) property of the [Application Model](xref:112580)'s **BOModel** | **_\<Class\>_** node. Note, you can set or change this property's value directly in the Application Model via the [Model Editor](xref:112582).

When this attribute is applied to a class, the specified image is displayed in detail forms, navigation control's items and **New** Action. When the **ImageName** attribute is applied to an enumeration value, the specified image is displayed by the Property Editors bound to properties of the enumeration type.

The **XAF** ships with a number of standard images embedded into the _DevExpress.Images.v<:xx.x:>_ assembly. To see the available images, browse the following _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.Images\Images_ folder. To assign one of these standard images to a class, pass the name of the image as the **ImageName** attribute's parameter or use the Model Editor. For details, refer to the following article: [](xref:404201).

To assign a custom image to a business class, create the _Images_ folder in one of your solution's projects and save the required image to this folder. In the **ImageName** attribute, pass the image name only (without extension). The required image will be found in the _Images_ folder. For details, refer to the [Assign a Custom Image](xref:404209) topic.

> [!NOTE]
> The image which is set for a business class via the **ImageName** attribute in code is not inherited.

For details on image managing in XAF, refer to the [](xref:112792) topic.
