---
uid: DevExpress.ExpressApp.WinMessageOptions.ImageOptions
name: ImageOptions
type: Property
summary: Provides access to the `DevExpress.Utils.ImageOptions` object. This object contains image settings of a [notification](xref:118549) that the [](xref:DevExpress.XtraBars.ToastNotifications.ToastNotification) or [](xref:DevExpress.XtraBars.Alerter.AlertControl) displays in a WinForms application.
syntax:
  content: public object ImageOptions { get; set; }
  parameters: []
  return:
    type: System.Object
    description: An `ImageOptions` object that contains image settings of a notification the **ToastNotification** or **AlertControl** displays in a WinForms application.
seealso: []
---
The following code shows how to change and customize a notification's image:

<!--TODO: add file name & namespace to the code snippet -->

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
using DevExpress.ExpressApp;
using DevExpress.Utils;
using DevExpress.Utils.Svg;
//...
MessageOptions options = new MessageOptions();
ImageOptions imageOptions = new ImageOptions();
//imageOptions.Image = Image.FromFile(@"D:\Images\success.png");
// or
imageOptions.SvgImage = SvgImage.FromFile(@"D:\Images\success.svg");
imageOptions.SvgImageSize = new Size(50, 50);
options.Win.ImageOptions = imageOptions;
Application.ShowViewStrategy.ShowMessage(options);
```
***

You can use the following `DevExpress.Utils.ImageOptions` properties:

{|
|-
! Property
! Description
|-

| Image
| Specifies a raster image for a notification. 
|-

| SvgImage
| Specifies an SVG image for a notification.
|- 

| SvgImageSize
| Specifies the size of an SVG image specified in the `SvgImage` property.
|}
