---
uid: DevExpress.ExpressApp.SystemModule.CustomGetFiltersEventArgs
name: CustomGetFiltersEventArgs
type: Class
summary: Arguments passed to the [FilterController.CustomGetFilters](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFilters) event.
syntax:
  content: 'public class CustomGetFiltersEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.CustomGetFiltersEventArgs._members
  altText: CustomGetFiltersEventArgs Members
---
The **CustomGetFilters** event occurs when the [](xref:DevExpress.ExpressApp.SystemModule.FilterController) is activated. You can handle this event to specify the Application Model's **Filters** node, containing the filter definitions to be used by the **FilterController**'s **SetFilter** Action for the currently processed List View. The **CustomGetFiltersEventArgs** class exposes a single [CustomGetFiltersEventArgs.Filters](xref:DevExpress.ExpressApp.SystemModule.CustomGetFiltersEventArgs.Filters) property, which specifies the **Filters** node to be used.