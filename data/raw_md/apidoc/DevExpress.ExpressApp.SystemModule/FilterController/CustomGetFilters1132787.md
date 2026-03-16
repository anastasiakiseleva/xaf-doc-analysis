---
uid: DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFilters
name: CustomGetFilters
type: Event
summary: Occurs when the [](xref:DevExpress.ExpressApp.SystemModule.FilterController) is activated. Allows you to specify the [Application Model](xref:112580)'s [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] | **Filters** node, containing the filter definitions to be used by the **FilterController**'s **SetFilter** [Action](xref:112622) for the currently processed [List View](xref:112611).
syntax:
  content: public event EventHandler<CustomGetFiltersEventArgs> CustomGetFilters
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.FilterController.SetFilterAction
- linkId: "403238"
- linkId: "112998"
---
The FilterController exposes the **FilterAction** described in the [FilterController.SetFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.SetFilterAction) and [](xref:403238) help topics.
The [CustomGetFiltersEventArgs.Filters](xref:DevExpress.ExpressApp.SystemModule.CustomGetFiltersEventArgs.Filters) parameter refers to an Application Model node. All changes of this node are persisted to the  user's Model Differences,
so the **CustomGetFilters** event should not be used to modify this node. The event can be used only to conditionally switch the set of predefined filters by assigning the required Application Model's **Filters** node to the **Filters** parameter. Note that the value of the currently selected filter's **Id** property is saved to the specified node's **CurrentFilterID** property.