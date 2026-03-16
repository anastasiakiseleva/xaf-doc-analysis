---
uid: DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties
name: CustomGetFullTextSearchProperties
type: Event
summary: Occurs when the **FullTextSearch** [Action](xref:112622) is executed. Allows you to specify the properties over which the search is performed.
syntax:
  content: public event EventHandler<CustomGetFullTextSearchPropertiesEventArgs> CustomGetFullTextSearchProperties
seealso:
- linkId: "112923"
---

The **FullTextSearch** Action searches the current [List View](xref:112611) for objects where property string representations include the value specified by a user.

The **FullTextSearch** Action performs a search based on the [FilterController.FullTextSearchTargetPropertiesMode](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextSearchTargetPropertiesMode) property value.

To override this behavior, handle the `CustomGetFullTextSearchProperties` event. In the event handler, pass a list of the required property names as the `Properties` parameter. Set the `Handled` argument to `true` to indicate that the `FullTextSearchTargetPropertiesMode` property's value must not be considered.

To determine properties used in default search operations, use the [FilterController.GetFullTextSearchProperties](xref:DevExpress.ExpressApp.SystemModule.FilterController.GetFullTextSearchProperties) method.

> [!NOTE]
> If you handle the [FilterController.CustomBuildCriteria](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomBuildCriteria) event and set the handler's `Handled` parameter to `true`, the `CustomGetFullTextSearchProperties` event is not triggered.

For more information about the **Filter by Text** Action, refer to the [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) property description.

> [!TIP]
> The **FullTextSearch** Action is also available in List Views used by Lookup Property Editors. To enable Search mode, use either of the following approaches:
> * Specify the [IModelClass.DefaultLookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultLookupEditorMode) option in Model Editor.
> * Apply a [LookupEditorModeAttribute](xref:DevExpress.Persistent.Base.LookupEditorModeAttribute) to the property.