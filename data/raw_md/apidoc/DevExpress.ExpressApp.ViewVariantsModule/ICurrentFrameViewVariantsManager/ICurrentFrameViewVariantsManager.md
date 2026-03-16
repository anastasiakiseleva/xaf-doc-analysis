---
uid: DevExpress.ExpressApp.ViewVariantsModule.ICurrentFrameViewVariantsManager
name: ICurrentFrameViewVariantsManager
type: Interface
summary: Implemented by classes that manage View Variants in the context of the current [](xref:DevExpress.ExpressApp.Frame).
syntax:
  content: 'public interface ICurrentFrameViewVariantsManager : IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.ICurrentFrameViewVariantsManager._members
  altText: ICurrentFrameViewVariantsManager Members
---
Objects that support the **ICurrentFrameViewVariantsManager** interface are used by the [](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController) Controller to display available View Variants and change the [Frame.View](xref:DevExpress.ExpressApp.Frame.View) property of the current [](xref:DevExpress.ExpressApp.Frame).

The default implementation of the **ICurrentFrameViewVariantsManager** used by **ChangeVariantController** is [](xref:DevExpress.ExpressApp.ViewVariantsModule.CurrentFrameViewVariantsManager). You can create a custom class that implements an **ICurrentFrameViewVariantsManager**, and pass an instance of this class to the [ChangeVariantController.CurrentFrameViewVariantsManager](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.CurrentFrameViewVariantsManager) property.