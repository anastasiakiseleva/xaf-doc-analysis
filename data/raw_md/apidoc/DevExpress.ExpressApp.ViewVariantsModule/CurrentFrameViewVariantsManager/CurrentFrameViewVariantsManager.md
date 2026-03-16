---
uid: DevExpress.ExpressApp.ViewVariantsModule.CurrentFrameViewVariantsManager
name: CurrentFrameViewVariantsManager
type: Class
summary: Manages View Variants in the context of the current [](xref:DevExpress.ExpressApp.Frame).
syntax:
  content: 'public class CurrentFrameViewVariantsManager : ICurrentFrameViewVariantsManager, IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.CurrentFrameViewVariantsManager._members
  altText: CurrentFrameViewVariantsManager Members
---
The **CurrentFrameViewVariantsManager** object is used by the [](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController) Controller to display available View Variants and change the [Frame.View](xref:DevExpress.ExpressApp.Frame.View) property of the current [](xref:DevExpress.ExpressApp.Frame).

To customize this class behavior, create a custom class that implements the **CurrentFrameViewVariantsManager**, and pass an instance of this class to the [ChangeVariantController.CurrentFrameViewVariantsManager](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.CurrentFrameViewVariantsManager) property.