---
uid: DevExpress.ExpressApp.Editors.IAppearanceEnabled
name: IAppearanceEnabled
type: Interface
summary: Declares members implemented by the UI elements that can be disabled or enabled by a [conditional appearance rule](xref:113286).
syntax:
  content: 'public interface IAppearanceEnabled : IAppearanceBase'
seealso:
- linkId: DevExpress.ExpressApp.Editors.IAppearanceEnabled._members
  altText: IAppearanceEnabled Members
- linkId: DevExpress.ExpressApp.Editors.IAppearanceFormat
- linkId: DevExpress.ExpressApp.Editors.IAppearanceVisibility
---
The Conditional Appearance module allows you to enable/disable specific UI elements when they are displayed under certain conditions. To allow the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) to disable/enable UI elements, they should implement the **IAppearanceEnabled** interface. This interface exposes the [IAppearanceEnabled.Enabled](xref:DevExpress.ExpressApp.Editors.IAppearanceEnabled.Enabled) property, to get or set the enabled state, and the [IAppearanceEnabled.ResetEnabled](xref:DevExpress.ExpressApp.Editors.IAppearanceEnabled.ResetEnabled) method, to reset the enabled state to the required initial value.

This interface is already implemented by base classes representing built-in XAF [Detail View Items](xref:112612), Layout Items, [Action](xref:112622) Appearance Items and auxiliary adapters that provide access to [List Editor](xref:113189) cells. Implement the **IAppearanceEnabled** interface in a custom class representing a UI element so that this element can also be disabled/enabled by the AppearanceController.