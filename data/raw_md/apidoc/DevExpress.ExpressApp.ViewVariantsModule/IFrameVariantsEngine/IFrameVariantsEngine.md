---
uid: DevExpress.ExpressApp.ViewVariantsModule.IFrameVariantsEngine
name: IFrameVariantsEngine
type: Interface
summary: Implemented by classes that provide methods to manage View Variants.
syntax:
  content: public interface IFrameVariantsEngine
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.IFrameVariantsEngine._members
  altText: IFrameVariantsEngine Members
- linkId: DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController
---
This interface declares methods used to get a list of available variants for a passed [](xref:DevExpress.ExpressApp.View) object, and to change the [Frame.View](xref:DevExpress.ExpressApp.Frame.View)  value of the passed [](xref:DevExpress.ExpressApp.Frame) object in accordance with the [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo) object that specifies the new View Variant.

Classes that implement this interface should properly manage Views in the application when calling [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) / [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*) methods.
The [](xref:DevExpress.ExpressApp.ViewVariantsModule.FrameVariantsEngine) is the built-in implementation of the **IFrameVariantsEngine** interface. You can add a custom class that implements the **IFrameVariantsEngine** and pass an instance of this class to the [ViewVariantsModule.FrameVariantsEngine](xref:DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule.FrameVariantsEngine) property.