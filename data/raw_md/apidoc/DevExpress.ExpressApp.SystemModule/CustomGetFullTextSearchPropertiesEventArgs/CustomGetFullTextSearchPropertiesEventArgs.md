---
uid: DevExpress.ExpressApp.SystemModule.CustomGetFullTextSearchPropertiesEventArgs
name: CustomGetFullTextSearchPropertiesEventArgs
type: Class
summary: Arguments passed to the [FilterController.CustomGetFullTextSearchProperties](xref:DevExpress.ExpressApp.SystemModule.FilterController.CustomGetFullTextSearchProperties) event.
syntax:
  content: 'public class CustomGetFullTextSearchPropertiesEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.CustomGetFullTextSearchPropertiesEventArgs._members
  altText: CustomGetFullTextSearchPropertiesEventArgs Members
---
The **CustomGetFullTextSearchProperties** event allows you to specify the properties over which the **FullTextSearch** [Action](xref:112622) performs its search. Since this event is triggered automatically by the [](xref:DevExpress.ExpressApp.SystemModule.FilterController), you do not need to instantiate **CustomGetFullTextSearchPropertiesEventArgs** objects.