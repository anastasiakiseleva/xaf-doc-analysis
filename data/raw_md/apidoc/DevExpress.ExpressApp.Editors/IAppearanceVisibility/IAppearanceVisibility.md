---
uid: DevExpress.ExpressApp.Editors.IAppearanceVisibility
name: IAppearanceVisibility
type: Interface
summary: Declares members implemented by the UI elements that can be made invisible or visible by a [conditional appearance rule](xref:113286).
syntax:
  content: 'public interface IAppearanceVisibility : IAppearanceBase'
seealso:
- linkId: DevExpress.ExpressApp.Editors.IAppearanceVisibility._members
  altText: IAppearanceVisibility Members
- linkId: DevExpress.ExpressApp.Editors.IAppearanceEnabled
- linkId: DevExpress.ExpressApp.Editors.IAppearanceFormat
---
The Conditional Appearance module allows you to make different UI elements visible/invisible when they are displayed in certain conditions. To allow the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) to make UI elements visible/invisible, these elements should implement the **IAppearanceVisibility** interface. This interface exposes the [IAppearanceVisibility.Visibility](xref:DevExpress.ExpressApp.Editors.IAppearanceVisibility.Visibility) property, to get or set the visibility state, and the [IAppearanceVisibility.ResetVisibility](xref:DevExpress.ExpressApp.Editors.IAppearanceVisibility.ResetVisibility) method, to reset the visibility state to the required initial value.

This interface is already implemented by base classes representing built-in XAF [Detail View Items](xref:112612), Layout Items, [Action](xref:112622) Appearance Items and auxiliary adapters that provide access to [List Editor](xref:113189) cells. Implement the **IAppearanceVisibility** interface in a custom class representing a UI element so that this element can also be made visible/invisible by the AppearanceController.