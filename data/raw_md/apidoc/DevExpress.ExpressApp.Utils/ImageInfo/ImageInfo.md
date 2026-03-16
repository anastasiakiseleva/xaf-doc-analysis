---
uid: DevExpress.ExpressApp.Utils.ImageInfo
name: ImageInfo
type: Struct
summary: Supplies metadata information on an image used in an XAF application.
syntax:
  content: 'public struct ImageInfo : IEquatable<ImageInfo>'
seealso:
- linkId: DevExpress.ExpressApp.Utils.ImageInfo._members
  altText: ImageInfo Members
---
An `ImageInfo` instance is an image used in an XAF application. Its properties provide access to the image and associated metadata, such as image dimensions and name.

XAF uses the [](xref:DevExpress.ExpressApp.Utils.ImageLoader) class to manage images. To get an `ImageInfo` instance, use the `ImageLoader.Get...ImageInfo` methods. The following code snippet demonstrates how to use the [ImageInfo.Image](xref:DevExpress.ExpressApp.Utils.ImageInfo.Image) property to retrieve the specified image:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Utils;
using DevExpress.Persistent.Base;

namespace dxTestSolution.Module.Controllers {
    public class CustomBlazorController : ViewController {
        public CustomBlazorController() {
            var _actionName = "MyAction1";
            myAction = new SimpleAction(this, _actionName, PredefinedCategory.Edit);
            myAction.Caption = _actionName;
            myAction.ToolTip = myAction.Caption;
        }
        SimpleAction myAction;
        protected override void OnFrameAssigned() {
            base.OnFrameAssigned();
            string imageName = $"action_export_tortf";
            var imageInfo = ImageLoader.Instance.GetImageInfo(imageName);
            if (!imageInfo.IsEmpty) {
                myAction.ImageName = imageName;
                myAction.Execute += (s, e) => { /*Add your custome code here*/ };
            }
        }
    }
}
```

For general guidelines on how to use images in an XAF application, refer to the following topic: [](xref:112792).
