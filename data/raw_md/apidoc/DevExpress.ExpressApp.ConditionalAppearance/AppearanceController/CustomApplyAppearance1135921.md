---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomApplyAppearance
name: CustomApplyAppearance
type: Event
summary: This event occurs before the conditional appearance updates the target UI element.
syntax:
  content: public event EventHandler<ApplyAppearanceEventArgs> CustomApplyAppearance
seealso: []
---
The [AppearanceController.RefreshItemAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RefreshItemAppearance*) method raises this event. An `AppearanceObject` describes the resulting appearance that the event applies.

You can access and modify this object in the `CustomApplyAppearance` event handler with the [ApplyAppearanceEventArgs.AppearanceObject](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.AppearanceObject) property.

To identify the target item and context, use these parameters in the event handler:
* [ApplyAppearanceEventArgs.Item](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.Item)
* [ApplyAppearanceEventArgs.ItemName](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.ItemName)
* [ApplyAppearanceEventArgs.ItemType](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.ItemType)
* [ApplyAppearanceEventArgs.ContextObjects](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.ContextObjects)

> [!IMPORTANT]
> Set the `Handled` parameter to `true` if your code completely processes the appearance settings. Set it to `false` to allow default processing. Default processing can override your changes.

See the following table for supported appearance item types:

{|
|-

! Item
! Description
! Supported Appearance types
|-

| `AppearanceObjectAdapter`
| Accesses the arguments of the [GridView.RowCellStyle](xref:DevExpress.XtraGrid.Views.Grid.GridView.RowCellStyle) event in the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor). Use the [](xref:DevExpress.XtraGrid.Views.Grid.RowCellStyleEventArgs) object from the adapter's `Data` property for row cell or appearance settings.

Accesses the arguments of the [TreeList.NodeCellStyle](xref:DevExpress.XtraTreeList.TreeList.NodeCellStyle) event in the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor). Use the [](xref:DevExpress.XtraTreeList.GetCustomNodeCellStyleEventArgs) object from the adapter's `Data` property for node cell or appearance settings.
| `IAppearanceFormat`
|-

| `GridViewRowCellStyleEventArgsAppearanceAdapter`, `GridViewCancelEventArgsAppearanceAdapter`, `GridViewCancelEventArgsAppearanceAdapterWithReset`
| Accesses the [](xref:DevExpress.XtraGrid.Views.Grid.GridView) and `EventArgs` objects passed to [ColumnView.ShowingEditor](xref:DevExpress.XtraGrid.Views.Base.ColumnView.ShowingEditor) and [GridView.RowCellStyle](xref:DevExpress.XtraGrid.Views.Grid.GridView.RowCellStyle) events to customize grid cells and editors.
| `IAppearanceFormat`, `IAppearanceEnabled`
|-

| `NodeCellStyleEventArgsAppearanceObjectAdapter`
| Accesses the [](xref:DevExpress.XtraTreeList.TreeList) and [](xref:DevExpress.XtraTreeList.GetCustomNodeCellStyleEventArgs) objects when the system applies appearance to Tree List cells.
| `IAppearanceFormat`
|-

| `WinLayoutItemAppearanceAdapter`
| Accesses a `XAFLayoutItemInfo` object representing a layout item or group. The system creates this item with the `WinLayoutManager` and when the [AppearanceController.Refresh](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.Refresh) method runs. Use the adapter's `Data` property for access.
| `IAppearanceFormat`, `IAppearanceVisibility`
|-

| `DevExpress.ExpressApp.Editors.ColumnWrapper`
| This column appears in a [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) and [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor). The system applies conditional appearance to each column at creation.
| `IAppearanceVisibility`
|-

| [](xref:DevExpress.ExpressApp.Editors.PropertyEditor)
| The system applies conditional appearance to every [PropertyEditor class descendant](xref:113097) when controls are created and when the [AppearanceController.Refresh](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.Refresh) method runs.
| `IAppearanceEnabled`, `IAppearanceVisibility`
|-

| [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor)
| The system applies conditional appearance to every [DXPropertyEditor class descendant](xref:113097) at creation and when the [AppearanceController.Refresh](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.Refresh) method runs.
| `IAppearanceFormat`
|-

| [](xref:DevExpress.ExpressApp.Editors.StaticText)
| The system applies conditional appearance to Static Text Detail View Items at creation and when the [AppearanceController.Refresh](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.Refresh) method runs.
| `IAppearanceFormat`
|-

| `ActionAppearanceItem`
| The system applies conditional appearance to objects of this type when the [AppearanceController.Refresh](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.Refresh) method runs. Use the item's `Data` property to access the affected Action.
| `IAppearanceEnabled`, `IAppearanceVisibility`
|}

For event handler examples, refer to the following topic: [How to: Customize the Conditional Appearance Module Behavior](xref:113374).

> [!NOTE]
> [!include[CustomApplyAppearance_Note](~/templates/customapplyappearance_note111125.md)]