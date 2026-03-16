---
uid: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.CustomizeAppearance
name: CustomizeAppearance
type: Event
summary: Occurs before the [GridListEditor.GridView](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor.GridView)'s cell of the [](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor) has been repainted in a UI. Enables the appearance settings of individual cells to be changed.
syntax:
  content: public event EventHandler<CustomizeAppearanceEventArgs> CustomizeAppearance
seealso: []
---
The [](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor) implements the **ISupportAppearanceCustomization** interface and supports appearance customization via the [Conditional Appearance module](xref:113286). The **ISupportAppearanceCustomization** interface exposes a single member - the **CustomizeAppearance** event.

This event is not intended to be handled from your code.