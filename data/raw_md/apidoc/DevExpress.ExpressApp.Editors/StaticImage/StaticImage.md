---
uid: DevExpress.ExpressApp.Editors.StaticImage
name: StaticImage
type: Class
summary: An abstract class for a [View Item](xref:112612) that displays a static image.
syntax:
  content: 'public abstract class StaticImage : ViewItem'
seealso:
- linkId: DevExpress.ExpressApp.Editors.StaticImage._members
  altText: StaticImage Members
- linkId: DevExpress.ExpressApp.Editors.StaticText
- linkId: DevExpress.ExpressApp.Editors.ViewItemAttribute
- linkId: "112792"
- linkId: "404209"
---
The `StaticImage` class is an abstract class from which platform-specific Static Image View Items derive. The class itself derives from the [](xref:DevExpress.ExpressApp.Editors.ViewItem) class responsible for implementing basic functionality for items in a Detail View.

## Add a Default Static Image

To add a Static Image View Item to a Detail View, use the [Model Editor](xref:112830).

* Navigate to [!include[Node_Views_DetailView_Items](~/templates/node_views_detailview_items111383.md)].
* Right-click the node and select **Add…** | **StaticImage**. 
    
    ![StaticImage](~/images/model-editor-add-static-image.png)
* Specify the `ImageName` and `Id` properties for the newly added item. You can select an image from the Image Picker. Click the ellipsis button (…) on the right of the property value when the `ImageName` property is focused and browse the available images.
    
    ![StaticImageProperties](~/images/model-editor-set-image-name.png)
* Then, proceed to the [!include[Node_Views_DetailView_Layout](~/templates/node_views_detailview_layout111385.md)] node and customize the Detail View's layout. 
    
    ![StaticImageLayout](~/images/model-editor-customize-detail-view.png)

## Add a Custom Static Image

You may need to implement a custom Static Image View Item with a specific image-displaying control.

* Add a public class that inherits from `StaticImage` to a UI-specific [application project](xref:118045).
* Override the protected virtual `CreateControlCore` method and return an instance of the required control.
* Apply the `ViewItemAttribute` to the custom item. This will add a child node to the **ViewItems** node in the Application Model.

For more information, refer to the [View Items](xref:112612) and [How to: Implement a View Item](xref:405483) topics.

## Customize a Static Image's Size Options

If a `StaticImage` is displayed incorrectly in your application, choose the appropriate [ImageSizeMode](xref:DevExpress.Persistent.Base.ImageSizeMode) in the [Model Editor](xref:112582).
![SizeMode](~/images/model-editor-image-size-mode.png)


For SVG images, you can also specify [SvgImageHeight](xref:DevExpress.ExpressApp.Model.IModelStaticImage.SvgImageHeight) and [SvgImageWidth](xref:DevExpress.ExpressApp.Model.IModelStaticImage.SvgImageWidth). In WinForms applications, these properties work only with the following [ImageSizeMode](xref:DevExpress.Persistent.Base.ImageSizeMode) values: `AutoSize`, `CenterImage`, or `Normal`. In ASP.NET Core Blazor applications, the `SvgImageHeight` and `SvgImageWidth` properties do not depend on the `ImageSizeMode` property.
 