---
uid: DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController
name: ChangeVariantController
type: Class
summary: Represents a [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **ChangeVariant** [Action](xref:112622).
syntax:
  content: 'public class ChangeVariantController : Controller, IFilterActionProvider'
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController._members
  altText: ChangeVariantController Members
- linkId: "113011"
- linkId: DevExpress.ExpressApp.ViewVariantsModule.CurrentFrameViewVariantsManager
---
The `ChangeVariantController` displays the **ChangeVariant** Action. This Action allows users to switch between predefined View Variants of a particular business object type.

In a Windows Forms application:

![ViewChangeActionInWindow](~/images/viewchangeactioninwindow115369.png)

The `ChangeVariantController` is shipped with the [View Variants](xref:113011) module and is activated for all [Views](xref:112611). You can use the [Model Editor](xref:112582) to customize the `ChangeVariantController` behavior via the **ActionDesign** | **Controllers** | **DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController** node. The **ChangeVariant** Action is accessible via the **ActionDesign** | **Actions** | **ChangeVariant** node.

For details on the **ChangeVariant** Action, refer to the following topic: [ChangeVariantController.ChangeVariantAction](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.ChangeVariantAction).

This Controller uses the [](xref:DevExpress.ExpressApp.ViewVariantsModule.CurrentFrameViewVariantsManager) object to populate the items of the **ChangeVariant** Action, switch the variant according to an end-user's selection and save the selected variant. By default, the last chosen variant identifier is stored with user customizations (in the _Model.User.xafml_ file).
Use the [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantInfo) to display a single variant.
Use the [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo) class to display a set of variants available for a particular varied View.